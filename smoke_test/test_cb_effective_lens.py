#!/usr/bin/env python3
"""Compare C++ cb_effective_parameters / cb_to_vbm_frame with the Python snippet."""
from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]


def effective_parameters(sb, qb, sp, qp, psi):
    """Angles: radians. Lengths: Einstein radius of M1+M2.
    qb = M2/M1; qp = mp/(M1+M2).
    """
    m1, m2 = 1 / (1 + qb), qb / (1 + qb)
    zp = sp * np.exp(1j * psi)
    d1, d2 = np.conj(zp + m2 * sb), np.conj(zp - m1 * sb)

    caustic_reference = zp - m1 / d1 - m2 / d2
    gamma = m1 / d1**2 + m2 / d2**2
    if abs(gamma) == 0:
        raise ValueError("Zero shear has no finite effective separation.")
    s_eff = abs(gamma) ** -0.5
    psi_eff = np.angle(gamma) / 2
    psi_eff += np.pi * np.round((psi - psi_eff) / np.pi)

    host_position = caustic_reference - np.exp(1j * psi_eff) * (s_eff - 1 / s_eff)
    return s_eff, qp, psi_eff, host_position


def to_vbm_frame(z, s_eff, q, psi_eff, host_position):
    z_vbm = 1 / np.sqrt(1 + q) * (
        np.exp(-1j * psi_eff) * (z - host_position) + q * s_eff / (1 + q)
    )
    return z_vbm


CASES = [
    (1.2, 0.7, 3.4, 0.001, 0.3, 0.1, -0.2),
    (0.8, 1.4, 2.1, 0.01, -0.9, -0.4, 0.5),
    (1.0, 1.0, 5.0, 1e-4, 1.2, 0.0, 0.0),
]


def main() -> int:
    exe = REPO_ROOT / "bin" / "test_cb_effective_lens.x"
    if not exe.is_file():
        print(f"missing {exe}", file=sys.stderr)
        return 1

    for sb, qb, sp, qp, psi, y1, y2 in CASES:
        s_eff, qp_out, psi_eff, host = effective_parameters(sb, qb, sp, qp, psi)
        z_vbm = to_vbm_frame(y1 + 1j * y2, s_eff, qp, psi_eff, host)
        proc = subprocess.run(
            [str(exe), str(sb), str(qb), str(sp), str(qp), str(psi), str(y1), str(y2)],
            check=True,
            capture_output=True,
            text=True,
        )
        parts = [float(x) for x in proc.stdout.split()]
        names = ["s_eff", "qp", "psi_eff", "host_re", "host_im", "y1_vbm", "y2_vbm"]
        got = dict(zip(names, parts))
        expected = {
            "s_eff": float(s_eff),
            "qp": float(qp_out),
            "psi_eff": float(psi_eff),
            "host_re": float(host.real),
            "host_im": float(host.imag),
            "y1_vbm": float(z_vbm.real),
            "y2_vbm": float(z_vbm.imag),
        }
        for name, exp in expected.items():
            err = abs(got[name] - exp)
            tol = 1e-10 * max(1.0, abs(exp))
            if not math.isfinite(got[name]) or err > tol:
                print(f"mismatch {name}: cpp={got[name]} py={exp} err={err}", file=sys.stderr)
                return 1
        print(
            f"ok sb={sb} qb={qb} sp={sp} qp={qp} psi={psi} "
            f"s_eff={s_eff:.8g} psi_eff={psi_eff:.8g}"
        )
    print("C++ effective-lens helpers match the Python snippet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
