"""Check finite instances of the commuting Gaussian cadence-budget proof.

The exact Schur channel, Gaussian trajectory overlaps and Kraus gauge are
computed separately. The finite checks do not establish the minimax rates.
"""

import json
from itertools import product
from math import factorial, prod
from pathlib import Path

import numpy as np
from scipy.special import gammainc


def degree_indices(bounds):
    """Return monomial exponents ordered by increasing total degree."""
    return sorted(product(*(range(bound) for bound in bounds)), key=lambda a: (sum(a), a))


def monomials(points, indices):
    powers = np.asarray(indices)
    return np.prod(points[:, None, :] ** powers[None, :, :], axis=-1)


def total_degree_indices(jumps, degree):
    return [a for a in degree_indices([degree + 1] * jumps) if sum(a) <= degree]


def gaussian_amplitudes(points, duration, indices):
    degrees = np.asarray([sum(a) for a in indices])
    factorials = np.asarray([prod(factorial(k) for k in a) for a in indices], dtype=float)
    attenuation = np.exp(-duration * np.sum(points**2, axis=1) / 2)
    return attenuation[:, None] * monomials(points, indices) * (
        duration**degrees / factorials
    ) ** 0.5


def add_orthonormal_vector(columns, candidate):
    residual = candidate.copy()
    for _ in range(2):
        for column in columns:
            residual -= np.dot(column, residual) * column
    norm = np.linalg.norm(residual)
    if norm < 1e-10:
        return False
    columns.append(residual / norm)
    return True


def syndrome_basis(weighted_polynomials):
    columns = []
    kept = []
    for index, candidate in enumerate(weighted_polynomials.T):
        if add_orthonormal_vector(columns, candidate):
            kept.append(index)
    for candidate in np.eye(weighted_polynomials.shape[0]):
        add_orthonormal_vector(columns, candidate)
    return np.column_stack(columns), kept


def prepare_code(points, signal, order):
    count, jumps = points.shape
    corrected = total_degree_indices(jumps, order - 1)
    moment_design = monomials(points, total_degree_indices(jumps, 2 * order - 2))
    coeffs, *_ = np.linalg.lstsq(moment_design, signal, rcond=None)
    residual = signal - moment_design @ coeffs
    assert np.linalg.norm(residual) > 1e-3
    positive = residual > 1e-10
    negative = residual < -1e-10
    assert np.all(positive | negative)

    branches = []
    for support in (positive, negative):
        weight = np.abs(residual[support])
        weight /= weight.sum()
        codeword = np.sqrt(weight)
        weighted = codeword[:, None] * monomials(points[support], corrected)
        basis, kept = syndrome_basis(weighted)
        assert np.max(np.abs(basis.T @ basis - np.eye(len(weight)))) < 2e-12
        embedded = np.zeros((count, len(weight)))
        embedded[support, :] = basis
        vector = np.zeros(count)
        vector[support] = codeword
        branches.append((embedded, vector, embedded.T @ (vector[:, None] * monomials(points, corrected)), kept))

    basis_plus, plus, moments_plus, kept_plus = branches[0]
    basis_minus, minus, moments_minus, kept_minus = branches[1]
    assert kept_plus == kept_minus
    width = max(basis_plus.shape[1], basis_minus.shape[1])
    basis_plus = np.pad(basis_plus, ((0, 0), (0, width - basis_plus.shape[1])))
    basis_minus = np.pad(basis_minus, ((0, 0), (0, width - basis_minus.shape[1])))
    moments_plus = np.pad(moments_plus, ((0, width - moments_plus.shape[0]), (0, 0)))
    moments_minus = np.pad(moments_minus, ((0, width - moments_minus.shape[0]), (0, 0)))
    moment_error = float(np.max(np.abs(moments_plus - moments_minus)))
    assert moment_error < 2e-12
    assert np.max(np.abs(basis_plus @ basis_plus.T + basis_minus @ basis_minus.T - np.eye(count))) < 2e-12
    gap = float((plus**2 - minus**2) @ signal)
    assert abs(gap) > 1e-3
    return (basis_plus, plus, basis_minus, minus), gap, moment_error, len(kept_plus)


def check_syndrome(points, signal, duration, order, code, projected_gap):
    basis_plus, plus, basis_minus, minus = code
    overlap_weights = np.outer(plus, minus) * (basis_plus @ basis_minus.T)
    squared_noise_gap = np.sum((points[:, None, :] - points[None, :, :]) ** 2, axis=-1)
    signal_gap = signal[:, None] - signal[None, :]
    kernel = np.exp(-duration * squared_noise_gap / 2)
    # expm1 computes 1 - f_h(0) without subtraction of nearby floating-point values.
    loss = -np.sum(overlap_weights * np.expm1(-duration * squared_noise_gap / 2))
    scaled_slope = np.sum(overlap_weights * kernel * signal_gap)

    # The overlap identity is checked via a separate sum over trajectory labels.
    indices = total_degree_indices(points.shape[1], 15)
    amplitudes = gaussian_amplitudes(points, duration, indices)
    cutoff_tail = gammainc(16, duration * np.sum(points**2, axis=1))
    assert max(cutoff_tail) < 2e-23
    amp_plus = basis_plus.T @ (plus[:, None] * amplitudes)
    amp_minus = basis_minus.T @ (minus[:, None] * amplitudes)
    squared_residual = np.linalg.norm(amp_plus - amp_minus) ** 2 / 2
    overlap_error = abs(loss - squared_residual)
    assert overlap_error < 2e-14

    slope_errors = []
    for detuning in (-0.7, 0.0, 0.6):
        phase = np.exp(-1j * detuning * duration * signal)
        adjusted = phase[:, None] * amplitudes
        branch_plus = basis_plus.T @ (plus[:, None] * adjusted)
        branch_minus = basis_minus.T @ (minus[:, None] * adjusted)
        branch_derivative_plus = basis_plus.T @ (plus[:, None] * (-1j * duration * signal[:, None]) * adjusted)
        branch_derivative_minus = basis_minus.T @ (minus[:, None] * (-1j * duration * signal[:, None]) * adjusted)
        recovered = np.vdot(branch_minus, branch_plus)
        derivative = np.vdot(branch_minus, branch_derivative_plus) + np.vdot(branch_derivative_minus, branch_plus)
        weighted_kernel = overlap_weights * kernel * np.exp(-1j * detuning * duration * signal_gap)
        assert abs(recovered - np.sum(weighted_kernel)) < 2e-12
        derivative_error = abs(derivative + 1j * duration * np.sum(weighted_kernel * signal_gap))
        assert derivative_error < 2e-12
        slope_errors.append(float(derivative_error))

    assert loss > 0
    assert 0.90 < scaled_slope / projected_gap < 1.10
    return {
        "duration": duration,
        "loss_over_h_to_order": float(loss / duration**order),
        "slope_over_h_times_projected_gap": float(scaled_slope / projected_gap),
        "syndrome_overlap_absolute_error": float(overlap_error),
        "maximum_tangent_absolute_error": max(slope_errors),
        "discarded_trajectory_weight_upper": float(max(cutoff_tail)),
    }


def balanced_split(exponents):
    left_degree = sum(exponents) // 2
    left = []
    for exponent in exponents:
        picked = min(left_degree, exponent)
        left.append(picked)
        left_degree -= picked
    return tuple(left), tuple(a - b for a, b in zip(exponents, left))


def check_balanced_gauge(points, bounds, signal, duration, order):
    indices = degree_indices(bounds)
    total_order = max((sum(a) + 1) // 2 for a in indices)
    active = total_degree_indices(points.shape[1], total_order)
    active_index = {a: k for k, a in enumerate(active)}
    q = np.sum(points**2, axis=1)
    polynomial = np.linalg.solve(monomials(points, indices), np.exp(duration * q) * signal)
    gauge = np.zeros((len(active), len(active)))
    max_imbalance = 0
    for coefficient, a in zip(polynomial, indices):
        b, c = balanced_split(a)
        max_imbalance = max(max_imbalance, abs(sum(b) - sum(c)))
        factor = float(prod(factorial(k) for k in (*b, *c))) ** 0.5
        entry = coefficient * factor * duration ** (1 - sum(a) / 2)
        ib, ic = active_index[b], active_index[c]
        if ib == ic:
            gauge[ib, ic] += entry
        else:
            gauge[ib, ic] += entry / 2
            gauge[ic, ib] += entry / 2

    amps = gaussian_amplitudes(points, duration, active)
    gauged_amps = amps @ gauge
    natural = duration * signal[:, None] * amps
    gauge_error = np.max(np.abs(np.sum(amps * gauged_amps, axis=1) - duration * signal))
    assert max_imbalance <= 1
    assert np.array_equal(gauge, gauge.T)
    assert gauge_error < 2e-12
    total_tail = gammainc(total_order + 1, duration * q)
    # Kraus labels outside the active gauge retain only the natural derivative.
    alpha = np.sum((natural - gauged_amps) ** 2, axis=1) + (duration * signal) ** 2 * total_tail
    return {"duration": duration, "beta_residual": float(gauge_error),
            "alpha_scaled": float(max(alpha) * duration ** (order - 2))}


def check_long_gauge(points, signal, duration):
    noise_distance = np.sum((points[:, None, :] - points[None, :, :]) ** 2, axis=-1)
    gram = np.exp(-duration * noise_distance / 2)
    gram_tangent = -1j * duration * (signal[:, None] - signal[None, :]) * gram
    root = np.linalg.cholesky(gram)
    derivative = np.linalg.solve(root, gram_tangent.T / 2).T
    mixed = derivative @ root.T
    drift_error = float(np.max(np.abs(np.diag(mixed))))
    tangent_error = float(np.max(np.abs(mixed + mixed.conj().T - gram_tangent)))
    assert max(drift_error, tangent_error) < 1e-11
    return {"duration": duration, "gram_minimum_eigenvalue": float(np.linalg.eigvalsh(gram)[0]),
            "beta_residual": drift_error, "channel_tangent_maximum_error": tangent_error,
            "alpha_norm": float(np.max(np.sum(np.abs(derivative)**2, axis=1)))}


def check_instance(name, points, bounds, signal, signal_degree):
    order = (signal_degree + 1) // 2
    code, gap, moment_error, corrected_rank = prepare_code(points, signal, order)
    lower_design = monomials(points, total_degree_indices(points.shape[1], signal_degree - 1))
    fitted = lower_design @ np.linalg.lstsq(lower_design, signal, rcond=None)[0]
    assert np.linalg.norm(fitted - signal) > 1e-3

    durations = (0.04, 0.02, 0.01, 0.005)
    syndrome = [check_syndrome(points, signal, h, order, code, gap) for h in durations]
    gauges = [check_balanced_gauge(points, bounds, signal, h, order) for h in durations]
    losses = [row["loss_over_h_to_order"] for row in syndrome]
    alpha_scaled = [row["alpha_scaled"] for row in gauges]
    assert max(losses) <= 1.5 * min(losses)
    assert max(alpha_scaled) <= 1.5 * min(alpha_scaled)

    return {"example": name, "joint_spectrum": points.tolist(), "signal_values": signal.tolist(),
            "minimum_degree": signal_degree, "order": order, "projected_signal_gap": gap,
            "matched_moment_error": moment_error, "corrected_syndrome_rank": corrected_rank,
            "syndrome": syndrome, "balanced_gauge": gauges,
            "long_gauge": [check_long_gauge(points, signal, h) for h in (0.2, 0.4, 1.0, 8.0)]}


def main():
    cubic = np.linspace(-1, 1, 4)[:, None]
    quintic = np.linspace(-1, 1, 6)[:, None]
    grid = np.array(list(product(np.linspace(-1, 1, 4), (-1.0, 0.0, 1.0))))
    instances = [
        check_instance("cubic", cubic, (4,), cubic[:, 0] ** 3, 3),
        check_instance("quintic", quintic, (6,), quintic[:, 0] ** 5, 5),
        check_instance("two-jump quintic", grid, (4, 3), grid[:, 0] ** 3 * grid[:, 1] ** 2, 5),
    ]
    results = {
        "scope": "Deterministic matrix checks on three spectra, with four durations per trajectory and gauge check.",
        "all_assertions_passed": True,
        "spectra": len(instances),
        "syndrome_cases": sum(len(row["syndrome"]) for row in instances),
        "detuning_tangent_cases": sum(3 * len(row["syndrome"]) for row in instances),
        "balanced_gauge_cases": sum(len(row["balanced_gauge"]) for row in instances),
        "long_gauge_cases": sum(len(row["long_gauge"]) for row in instances),
        "instances": instances,
    }
    results_path = Path(__file__).resolve().parent / "results"
    results_path.mkdir(exist_ok=True)
    (results_path / "cadence_budget_check.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({key: value for key, value in results.items() if key != "instances"}, indent=2))


if __name__ == "__main__":
    main()
