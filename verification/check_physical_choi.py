"""Independent numerical check of the analytical physical-channel Choi bounds.

This is supplementary verification, not a replacement for the proof in
science/grid_lower.md. Time is scaled so tau = 1.
"""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm_frechet


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
dL = -0.5j * (np.kron(I, Z) - np.kron(Z.T, I))


def choi(superoperator):
    result = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            eij = np.zeros((2, 2), dtype=complex)
            eij[i, j] = 1
            output = (superoperator @ eij.reshape(4, order="F")).reshape(
                (2, 2), order="F"
            )
            result += np.kron(output, eij) / 2
    return (result + result.conj().T) / 2


rows = []
for lam in (0.05, 0.2, 1.0, 3.0):
    for z in np.concatenate((-np.geomspace(1e-3, 100, 13), np.geomspace(1e-3, 100, 13))):
        L = z * dL + lam * (np.kron(X.T, X) - np.eye(4))
        E, dE = expm_frechet(L, dL)
        J, dJ = choi(E), choi(dE)
        eig_min = float(np.linalg.eigvalsh(J)[0])
        kappa = np.exp(-lam) * min(lam / 2, lam**2 / 8)
        event_bound = kappa / 2 * (1 - abs(np.sinc(z / (2 * np.pi))))
        coarse_bound = kappa / 64 * min(z**2, 1)
        derivative_norm = float(np.linalg.svd(dJ, compute_uv=False).sum())
        # A trace bound on channel RLD suffices for the proof.
        rld_trace = float(2 * np.trace(dJ @ np.linalg.solve(J, dJ)).real)
        rld_bound = 2 / coarse_bound
        assert abs(np.trace(J) - 1) < 1e-11
        assert eig_min >= event_bound * (1 - 1e-5)
        assert event_bound >= coarse_bound * (1 - 1e-7)
        assert derivative_norm <= 1 + 1e-11
        assert rld_trace <= rld_bound * (1 + 1e-9)
        rows.append(
            {
                "gamma_tau": lam,
                "delta_tau": float(z),
                "choi_min_eigenvalue": eig_min,
                "event_bound": float(event_bound),
                "coarse_bound": float(coarse_bound),
                "derivative_trace_norm": derivative_norm,
                "rld_trace_upper": rld_trace,
            }
        )

summary = {
    "cases": len(rows),
    "smallest_ratio_actual_to_event_bound": min(
        row["choi_min_eigenvalue"] / row["event_bound"] for row in rows
    ),
    "largest_derivative_trace_norm": max(
        row["derivative_trace_norm"] for row in rows
    ),
    "all_assertions_passed": True,
    "rows": rows,
}
(Path(__file__).parent / "results" / "physical_choi_check.json").write_text(
    json.dumps(summary, indent=2) + "\n"
)
print(json.dumps({k: v for k, v in summary.items() if k != "rows"}, indent=2))
