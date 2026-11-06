"""Finite checks for exact-channel margins in science/grid_upper.md.

These checks do not prove the theorem. They evolve the signed-telegraph process
using a 2x2 matrix exponential independently of the closed form used in the note.
"""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm


def telegraph_characteristic(lam, residual):
    generator = np.array([
        [-lam - 1j * residual, lam],
        [lam, -lam + 1j * residual],
    ], dtype=complex)
    return np.sum(expm(generator)[:, 0])


kappa, r = 1 / 16, 3 / 4
count = 0
min_margin_ratio = float("inf")
min_visibility = 1.0
max_classical_projection_error = 0.0
worst = None
for lam in [0.0, 0.01, 0.1, 1.0, 5.0, 20.0]:
    a = 1.0 if lam == 0 else -np.expm1(-2 * lam) / (2 * lam)
    bound = min(0.5, a / 4)
    w0 = min(bound / 8, kappa / 8)
    h0 = w0
    assert w0 + h0 / 2 <= bound
    assert w0 + h0 * h0 <= kappa / 2
    amplitude = a * np.exp(-kappa) / (2 * np.pi)
    for h in [0.0, h0, h0 / 10, h0 / 100]:
        for stage in range(40):
            w = w0 * r**stage
            n = int(np.floor(kappa / (w + h * h)))
            assert n >= 1
            for center_fraction in [-0.5, -0.2, 0.0, 0.2, 0.5]:
                d = center_fraction * h
                reference = -np.angle(telegraph_characteristic(lam, d))
                theta = n * reference
                for fraction in [-1.0, -0.5, 0.5, 1.0]:
                    residual = d + fraction * w
                    char = telegraph_characteristic(lam, residual)
                    phase = -np.angle(char)
                    visibility = abs(char)**n
                    mean = visibility * np.sin(n * (phase - reference))
                    ex = visibility * np.cos(n * phase)
                    ey = visibility * np.sin(n * phase)
                    projected = np.cos(theta) * ey - np.sin(theta) * ex
                    ratio = np.sign(fraction) * mean / (amplitude * n * w)
                    count += 1
                    if ratio < min_margin_ratio:
                        min_margin_ratio = float(ratio)
                        worst = dict(lam=lam, h=h, stage=stage, d=d,
                                     e=fraction*w, cycles=n)
                    min_visibility = min(min_visibility, float(visibility))
                    max_classical_projection_error = max(
                        max_classical_projection_error, float(abs(mean-projected)))

result = {
    "kind": "finite numerical checks, not a universal proof",
    "checked_cases": count,
    "minimum_ratio_of_signed_mean_to_proved_margin": min_margin_ratio,
    "minimum_visibility": min_visibility,
    "proved_visibility_lower_bound": float(np.exp(-kappa)),
    "maximum_fixed_xy_projection_identity_error": max_classical_projection_error,
    "worst_margin_case": worst,
}
assert min_margin_ratio >= 1 - 1e-8
assert min_visibility >= np.exp(-kappa) - 1e-8
assert max_classical_projection_error < 1e-8
(Path(__file__).parent / "results" / "grid_upper_checks.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
