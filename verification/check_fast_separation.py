"""Finite checks of the four-level fast/fixed separation.

This independently reconstructs the physical Lindblad exponential, compares it
with the exact Schur channel, and applies the displayed decoder repeatedly.
The global sign checks evaluate the actual corrected channel, not an idealized
phase model. Finite sampling of parameters is not a proof of the theorems.
Run from any working directory; results are stored beside this script.
"""

from pathlib import Path
import json

import numpy as np
from scipy.linalg import expm_frechet


I4 = np.eye(4, dtype=complex)
I2 = np.eye(2, dtype=complex)
L = np.diag([-3.0, -1.0, 1.0, 3.0]).astype(complex)
G = L @ L @ L
Z = np.diag([1.0, -1.0]).astype(complex)
Y = np.array([[0.0, -1.0j], [1.0j, 0.0]])
V = np.zeros((4, 2), dtype=complex)
V[1, 0], V[3, 0] = np.sqrt(3) / 2, 0.5
V[0, 1], V[2, 1] = 0.5, np.sqrt(3) / 2
R0, R1 = V.conj().T, V.conj().T @ L / np.sqrt(3)
R = (R0, R1)
PLUS = np.full((2, 2), 0.5, dtype=complex)
ELL = np.diag(L).real
GVAL = np.diag(G).real
DG = -1.0j * (np.kron(I4, G) - np.kron(G.T, I4))
DISSIPATOR = np.kron(L.conj(), L) - 0.5 * (
    np.kron(I4, L @ L) + np.kron((L @ L).T, I4)
)


def decode(matrix):
    return sum(k @ matrix @ k.conj().T for k in R)


def schur_factors(delta, duration):
    return np.exp(
        -duration * (ELL[:, None] - ELL[None, :]) ** 2 / 2
        - 1.0j * delta * duration * (GVAL[:, None] - GVAL[None, :])
    )


def corrected_superoperator(delta, duration):
    factors = schur_factors(delta, duration)
    channel = np.zeros((4, 4), dtype=complex)
    for j in range(2):
        for i in range(2):
            eij = np.zeros((2, 2), dtype=complex)
            eij[i, j] = 1
            out = decode(factors * (V @ eij @ V.conj().T))
            channel[:, i + 2 * j] = out.reshape(4, order="F")
    return channel


def recovered_derivative(delta):
    result = np.zeros((4, 4), dtype=complex)
    generator = DISSIPATOR + delta * DG
    for j in range(2):
        for i in range(2):
            eij = np.zeros((2, 2), dtype=complex)
            eij[i, j] = 1
            physical = V @ eij @ V.conj().T
            derivative = (generator @ physical.reshape(16, order="F")).reshape(
                (4, 4), order="F"
            )
            result[:, i + 2 * j] = decode(derivative).reshape(4, order="F")
    return result


def choi(superoperator):
    result = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            eij = np.zeros((4, 4), dtype=complex)
            eij[i, j] = 1
            out = (superoperator @ eij.reshape(16, order="F")).reshape(
                (4, 4), order="F"
            )
            result += np.kron(out, eij) / 4
    return (result + result.conj().T) / 2


code_errors = {
    "encoding_isometry": float(np.linalg.norm(V.conj().T @ V - I2)),
    "jump_compression": float(np.linalg.norm(V.conj().T @ L @ V)),
    "jump_square_compression": float(np.linalg.norm(V.conj().T @ L @ L @ V - 3 * I2)),
    "signal_compression": float(np.linalg.norm(V.conj().T @ G @ V - 6 * Z)),
    "decoder_trace_preservation": float(
        np.linalg.norm(sum(k.conj().T @ k for k in R) - I4)
    ),
}
assert max(code_errors.values()) < 1e-12
design = np.stack((np.ones(4), ELL, ELL**2), axis=1)
projection = design @ np.linalg.lstsq(design, GVAL, rcond=None)[0]
hnls_residual = float(np.linalg.norm(GVAL - projection))
assert hnls_residual > 1

derivative_errors = []
for delta in (-1.0, -0.1, 0.0, 0.3, 1.0):
    expected = -6.0j * delta * (np.kron(I2, Z) - np.kron(Z.T, I2))
    error = float(np.linalg.norm(recovered_derivative(delta) - expected))
    assert error < 1e-12
    derivative_errors.append(error)

fixed_rows = []
correlated = np.array([0, 5, 10, 15])
for tau in (0.02, 0.1, 0.5, 1.0):
    kernel = np.exp(-tau * (ELL[:, None] - ELL[None, :]) ** 2 / 2)
    minimum_kernel_eigenvalue = float(np.linalg.eigvalsh(kernel)[0])
    assert minimum_kernel_eigenvalue > 0
    commutator = G @ kernel - kernel @ G
    exact_information = float(
        tau**2 * np.max(np.diag(commutator @ np.linalg.solve(kernel, commutator.conj().T)).real)
    )
    for delta in (-100.0, -0.7, 0.0, 0.6, 100.0):
        channel, derivative = expm_frechet(
            tau * (DISSIPATOR + delta * DG), tau * DG
        )
        exact_channel = np.diag(schur_factors(delta, tau).reshape(16, order="F"))
        channel_error = float(np.max(np.abs(channel - exact_channel)))
        assert channel_error < 2e-11
        J, dJ = choi(channel), choi(derivative)
        gamma = 4 * J[np.ix_(correlated, correlated)]
        dgamma = 4 * dJ[np.ix_(correlated, correlated)]
        # Partial trace keeps the diagonal on the maximally correlated support.
        measured_information = float(
            np.max(np.diag(dgamma @ np.linalg.solve(gamma, dgamma)).real)
        )
        information_relative_error = abs(measured_information - exact_information) / max(
            1.0, exact_information
        )
        assert information_relative_error < 2e-8
        fixed_rows.append(
            {
                "tau": tau,
                "delta": delta,
                "kernel_min_eigenvalue": minimum_kernel_eigenvalue,
                "physical_channel_max_entry_error": channel_error,
                "rld_information": measured_information,
                "rld_formula_relative_error": information_relative_error,
            }
        )

beta, contraction = 0.25, 0.75
margin = float(np.sin(beta / 4))
repetition_constant = 24 * np.log(1 / contraction) / margin**2
time_constant = beta * (repetition_constant + 1) / 12 * contraction / (1 - contraction) ** 2
fast_rows, budget_rows = [], []
for band in (0.02, 0.2, 0.8):
    remainder_constant = ((18 + 54 * band) ** 2 + (12 * band) ** 2) / 2
    for stages in (1, 3, 9):
        final_width = band * contraction**stages
        step = min(beta / (24 * band), 6 * margin * final_width / (beta * remainder_constant))
        cells_used = 0
        for stage in range(1, stages + 1):
            width = band * contraction ** (stage - 1)
            cells = int(np.floor(beta / (12 * step * width)))
            repetitions = int(np.ceil(repetition_constant * (stages - stage + 1)))
            cells_used += cells * repetitions
            assert cells >= 1
            assert cells >= beta / (24 * step * width) - 1e-10
            bound = cells * remainder_constant * step**2
            assert bound <= margin / 2 + 1e-12
            for fraction in (-1.0, -0.5, 0.0, 0.5, 1.0):
                delta = fraction * width
                logical_channel = corrected_superoperator(delta, step)
                output = (
                    np.linalg.matrix_power(logical_channel, cells) @ PLUS.reshape(4, order="F")
                ).reshape((2, 2), order="F")
                actual_mean = float(np.trace(Y @ output).real)
                phase = 12 * cells * step * delta
                ideal_mean = float(np.sin(phase))
                error = abs(actual_mean - ideal_mean)
                trace_error = float(abs(np.trace(output) - 1))
                assert trace_error < 2e-8
                assert error <= bound + 2e-8
                if fraction:
                    assert beta / 4 - 1e-12 <= abs(phase) <= beta + 1e-12
                    assert np.sign(fraction) * actual_mean >= margin / 2 - 2e-8
                fast_rows.append(
                    {
                        "prior_half_width": band,
                        "stages": stages,
                        "stage": stage,
                        "residual_fraction": fraction,
                        "cell_duration": step,
                        "cells_per_batch": cells,
                        "actual_y_mean": actual_mean,
                        "ideal_y_mean": ideal_mean,
                        "phase": phase,
                        "absolute_mean_error": error,
                        "proved_mean_error_bound": bound,
                        "output_trace_error": trace_error,
                    }
                )
        actual_time = step * cells_used
        time_bound = time_constant / final_width
        assert actual_time <= time_bound * (1 + 1e-12)
        last_width = band * contraction ** (stages - 1)
        assert actual_time >= beta / (24 * last_width) * (1 - 1e-12)
        budget_rows.append(
            {
                "prior_half_width": band,
                "stages": stages,
                "corrected_cells": cells_used,
                "actual_sensing_time": actual_time,
                "proved_time_bound": time_bound,
                "cell_duration": step,
            }
        )

summary = {
    "status": "pass",
    "all_assertions_passed": True,
    "scope": "Four-level code/tangent, physical fixed-cell channel and RLD formula, actual fast-protocol sign means, deterministic budgets; finite checks only.",
    "code_errors": code_errors,
    "hnls_span_residual": hnls_residual,
    "largest_logical_tangent_error": max(derivative_errors),
    "fixed_channel_cases": len(fixed_rows),
    "fast_sign_cases": len(fast_rows),
    "budget_cases": len(budget_rows),
    "required_sign_margin": margin / 2,
    "smallest_signed_outer_mean": min(
        np.sign(row["residual_fraction"]) * row["actual_y_mean"]
        for row in fast_rows if row["residual_fraction"]
    ),
    "largest_mean_error_to_bound_ratio": max(
        row["absolute_mean_error"] / row["proved_mean_error_bound"] for row in fast_rows
    ),
    "largest_output_trace_error": max(row["output_trace_error"] for row in fast_rows),
    "largest_physical_channel_error": max(row["physical_channel_max_entry_error"] for row in fixed_rows),
    "largest_rld_formula_relative_error": max(row["rld_formula_relative_error"] for row in fixed_rows),
    "fixed_rows": fixed_rows,
    "fast_rows": fast_rows,
    "budget_rows": budget_rows,
}
destination = Path(__file__).resolve().parent / "results" / "fast_separation_checks.json"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({key: value for key, value in summary.items() if not key.endswith("_rows")}, indent=2))
