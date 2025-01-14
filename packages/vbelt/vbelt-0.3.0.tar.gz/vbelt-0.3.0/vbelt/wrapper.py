# vbelt: The VASP user toolbelt.
# Copyright (C) 2023  Théo Cavignac
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import sys
import os.path

from .misc import naturaldelta

from .script_utils import (
    script,
    error,
    positional,
    flag,
    optional,
    error_catch,
    PerfCounterCollec,
)


@script(
    positional("CHGCAR", help="file to extract data from"),
    flag("--split", help="split CHGCAR into up and down channels"),
    flag("--spin", help="extract the spin density"),
    flag("--total", help="extract the total density"),
    flag("--timing", help="show the timing informations"),
)
def charge_extract(opts):
    from .charge_utils import Charge

    pc = PerfCounterCollec()

    with pc.reading:
        if opts.chgcar == "-":
            chg = Charge.from_file(sys.stdin)
            name = "CHGCAR"
        else:
            with open(opts.chgcar) as f:
                chg = Charge.read_from(f)
            name = opts.chgcar

    out_prefix, ext = os.path.splitext(name)

    if opts.split:
        if chg.dif_part is None:
            error("There is no spin data available in the input file.")

        with pc.processing:
            up, down = chg.split()

        with pc.writing, open(out_prefix + ".up" + ext, "w") as f:
            up.write_to(f)

        with pc.writing, open(out_prefix + ".down" + ext, "w") as f:
            down.write_to(f)

    elif opts.spin:
        if chg.dif_part is None:
            error("There is no spin data available in the input file.")

        with pc.writing, open(out_prefix + ".spin" + ext, "w") as f:
            chg.dif_part.write_to(f)

    elif opts.total:
        with pc.writing, open(out_prefix + ".total" + ext, "w") as f:
            chg.total_only().write_to(f)

    else:
        error("No action required.")

    if opts.timing:
        print(pc.summary())


@script(
    positional("COEF_A", type=float, help="coeficient for the first file"),
    positional("CHGCAR_A", help="first file to extract data from"),
    positional("COEF_B", type=float, help="coeficient for the second file"),
    positional("CHGCAR_B", help="second file to extract data from"),
)
def charge_combine(opts):
    from .charge_utils import Charge

    if opts.chgcar_a == "-":
        chg_a = Charge.from_file(sys.stdin)
        name = "CHGCAR"
    else:
        with open(opts.chgcar_a) as f:
            chg_a = Charge.read_from(f)
        name = opts.chgcar_a

    prefix_out = name

    if opts.chgcar_b == "-":
        chg_b = Charge.from_file(sys.stdin)
    else:
        with open(opts.chgcar_b) as f:
            chg_b = Charge.read_from(f)

    chg_sum = opts.coef_a * chg_a + opts.coef_b * chg_b

    with open(prefix_out + ".sum", "w") as f:
        chg_sum.write_to(f)


@script(
    positional("OUTCAR", default="OUTCAR", type=str, help="VASP output file"),
    optional(
        "--tol",
        type=float,
        default=None,
        help="Maximum converged force ampliture (A/eV)",
    ),
    flag("--silent", "-q", help="quite mode, just use the return code"),
)
def check_forces(opts):
    import numpy as np
    from .forces import read_forces

    with error_catch(), open(opts.outcar) as f:
        species, forces, tol = read_forces(f)

    if opts.tol is not None:
        tol = opts.tol

    of = 0

    norms = np.linalg.norm(forces, axis=-1)
    (non_conv_where,) = np.where(norms > tol)
    non_conv_where = set(non_conv_where)

    if not opts.silent:
        for sp, n in species:
            print(f"{sp:2} {n:3}")

    if not opts.silent:
        print("       ---        X          Y          Z")
        print("===========================================")
        for sp, n in species:
            for j, (x, y, z) in enumerate(forces[of : of + n], start=of):
                if j in non_conv_where:
                    m = [" ", " ", " "]
                    m[np.argmax(np.abs([x, y, z]))] = "<"
                    print(
                        f"{sp:2} {j+1:3} >>> {x: .05f} {m[0]} {y: .05f} {m[1]} {z: .05f} {m[2]}"
                    )
                else:
                    print(f"{sp:2} {j+1:3}     {x: .05f}   {y: .05f}   {z: .05f}  ")
            of += n

    if non_conv_where:
        if not opts.silent:
            print(
                f"Convergence not reached: max force {np.max(norms):.05} eV/A > {tol:.02}."
            )
        return 1
    else:
        if not opts.silent:
            print("Convergence reached.")
        return 0


@script(
    positional("OUTCAR", default="OUTCAR", type=str, help="VASP output file"),
    flag("--silent", "-q", help="quite mode, just use the return code"),
)
def check_end(opts):
    from .outcar import normal_end

    with error_catch(), open(opts.outcar) as f:
        res = normal_end(f)

    if not opts.silent:
        if res:
            print("Computation ended normally.")
        else:
            print("Computation ended early.")

    return 0 if res else 1


@script(
    positional("DIR", default=".", type=str, help="VASP computation directory"),
    flag("--silent", "-q", help="quite mode, just use the return code"),
    optional("--osz", type=str, default=None, help="path to the OSZICAR file."),
    optional("--out", type=str, default=None, help="path to the OUTCAR file."),
    optional(
        "--tol", type=float, default=None, help="Tolerance on the energy residue."
    ),
)
def check_conv(opts):
    from .outcar import converged

    if opts.osz is None:
        osz = os.path.join(opts.dir, "OSZICAR")
    else:
        osz = opts.osz

    if opts.out is None:
        out = os.path.join(opts.dir, "OUTCAR")
    else:
        out = opts.out

    with error_catch():
        res, tol, residue = converged(osz, out, tol=opts.tol)

    if not opts.silent:
        if res:
            print(f"Computation converged with tolerance {tol}.")
        elif residue is None:
            print("Abnormal ending of the computation.")
        else:
            print(f"Computation did not converge: {residue} > {tol}.")

    return 0 if res else 1


@script(
    positional("DIR", default=".", type=str, help="VASP computation directory"),
    optional("--dos", type=str, default=None, help="path to the DOSCAR file."),
    optional("--out", type=str, default=None, help="path to the OUTCAR file."),
    optional("--width", "-w", type=int, default=80, help="width of the plot."),
    optional("--height", type=int, default=50, help="height of the plot."),
    optional("--min", type=float, default=None, help="Lower energy bound of the plot"),
    optional("--max", type=float, default=None, help="Higher energy bound of the plot"),
)
def termdos(opts):
    """Dirty plot a dos in a terminal.

    Remark: Requires PyDEF
    """
    from pydef import load_cell

    if opts.dos is None:
        dos = os.path.join(opts.dir, "DOSCAR")
    else:
        dos = opts.dos

    if opts.out is None:
        out = os.path.join(opts.dir, "OUTCAR")
    else:
        out = opts.out

    with error_catch():
        cell = load_cell(out, dos)

    with error_catch():
        cell.load_dos()

    fermi = cell.fermi_energy
    if fermi is None:
        fermi = cell.fermi_level

    if fermi is None:
        print("No Fermi level found. Energy axis is unshifted.")
        fermi = 0.0

    for line in draw_dos(
        opts.height,
        opts.width,
        cell.dos_energy - fermi,
        cell.total_dos,
        low_bound=opts.min,
        high_bound=opts.max,
    ):
        print(line)


def draw_dos(nx, ny, energy, dos, low_bound=None, high_bound=None):
    import numpy as np

    if not np.all(np.diff(energy) > 0):
        raise ValueError("Energy axis not strictly increasing.")

    _low_bound = low_bound or np.min(energy)
    _high_bound = high_bound or np.max(energy)

    x = np.linspace(_low_bound, _high_bound, nx)

    y = np.interp(x, energy, dos)

    maxy = np.max(dos)

    quant = [quantize(ny, d, maxy) for d in y]

    prev_prev = quant[0]
    prev = quant[0]

    wrapped = []

    for n in quant[1:]:
        wrapped.append((prev_prev, prev, n))
        prev_prev = prev
        prev = n

    wrapped.append((prev_prev, prev, n))

    for e, (nprev, n, nnext) in zip(x, wrapped):
        if e % 10:
            prefix = f"{e:>7.3f} |"
        else:
            prefix = " " * 7 + " |"

        d1 = (n - nprev) // 2
        d2 = (nnext - n) // 2

        if d1 == d2 == 0:
            yield prefix + " " * n + "|"
        if d1 * d2 > 0:  # same sign
            if d1 > 0:
                yield prefix + " " * n + "<" + "=" * min(d1, d2)
            else:
                k = n + max(d1, d2)
                yield prefix + " " * k + "=" * (n - k) + ">"
        else:
            if d1 > 0:
                k1 = n - d1
                k2 = d2 - n
                yield prefix + " " * k1 + "°" * (n - k1) + "\\" + "." * k2
            else:
                k2 = n - d1
                k1 = d1 - n
                yield prefix + " " * k2 + "." * (n - k2) + "/" + "°" * k2


def quantize(ny, val, max):
    return int(ny * val / max)


@script(
    positional("PATH", default=".", help="Computation directory"),
)
def report(opts):
    import numpy as np
    from datetime import datetime, timedelta
    from .outcar_utils import get_val, get_int, get_float
    from .outcar import converged
    from .forces import read_forces

    outcar = os.path.join(opts.path, "OUTCAR")
    oszicar = os.path.join(opts.path, "OSZICAR")

    last_tot = "0.0"

    with open(outcar) as f:
        date, time = get_val(f, "date").split()
        ncore = get_int(f, "running on", after="total cores")

        for line in f:
            if line.startswith("--------------------------------------- Iteration"):
                break

        for line in f:
            if "free  energy" in line:# line.startswith("  free  energy"):
                last_tot = line
            elif line.startswith(" total amount of memory"):
                break

        try:
            elapsed = timedelta(seconds=get_float(f, "Elapsed time (sec):"))
        except Exception:
            pass

    dt = datetime.fromisoformat(date.replace('.', '-') + ' ' + time)
    ago = datetime.now() - dt
    total_energy = float(last_tot.split("=")[1].split()[0].strip())

    print("At", time, "on", date, f"({naturaldelta(ago)} ago)")
    print("Running on", ncore, "cores")

    conv, _, _ = converged(oszicar, outcar)
    if conv:
        print(f"Computation converged within {naturaldelta(elapsed)}.")
    else:
        print("Computation did not converge.")

    with error_catch(), open(outcar) as f:
        species, forces, tol = read_forces(f)

    max_f = np.max(np.linalg.norm(forces))

    print(f"Total energy: {total_energy:0.05f} eV")
    print(f"Maximum residual force: {max_f:0.02e}")
