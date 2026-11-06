# Reproduce the finite checks

These deterministic matrix calculations test vulnerable identities and representative parameter regimes. The [scientific proofs](../science/model.md) establish the general claims. Passing the suite does not independently prove a universal noise-algebra classification or an asymptotic minimax theorem.

## Run

From the repository root, with Python 3:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checked dependency versions are pinned in `requirements.txt`. The runner prints one `PASS` line per successful script, stops on a failure and writes `results/summary.json`. Individual scripts also write their detailed results. Floating-point residuals can vary slightly across numerical libraries and platforms; each script checks scientifically relevant tolerances.

| Script | Independent calculation | Scope |
|---|---|---|
| `check_algebra.py` | Builds the explicit Gram-matrix decoder and compares a Frechet derivative of the physical semigroup with the integrated Heisenberg tangent | 18 cases across a noncommuting $`\mathstrut{M_2\otimes I}`$ algebra and a diagonal qutrit algebra, including zero rates; also checks the four-level HNLS residual and Gaussian kernel positivity |
| `check_exact_cycle.py` | Exponentiates the full sensor–ancilla density-matrix generator and applies parity recovery | 72 exact-channel comparisons and 13,020 finite sign-margin cases |
| `check_grid_upper.py` | Uses an independent two-state telegraph generator to evaluate visibility, phase and classical X/Y processing | 19,200 parameter/width/offset cases; zero rate is included as an identity check, not as a matched-grid lower-bound claim |
| `check_physical_choi.py` | Exponentiates the unrecovered qubit channel and its Frechet derivative, then forms its Choi matrix | 104 cases testing the analytical positive-eigenvalue, derivative and RLD upper bounds |
| `check_fast_separation.py` | Checks the explicit four-level code and its recovered finite-cell response | Finite global-fast-protocol margins and error bounds; the script reports its actual sampled scope |

The source uses column-stacking for numerical superoperators and explicitly constructs Choi matrices in output-factor-first tensor order. This convention does not change the abstract support or information statements.

## What the checks do not settle

The arbitrary-ancilla adaptive converse uses the cited channel RLD chain rule and the written full-history argument. Numerical eigenvalues do not prove exact Kraus support for all parameters. A finite margin grid does not prove a uniform inequality, and no finite simulation establishes the infinite-horizon rate. The global upper bounds therefore give explicit constants, first-failure risk accounting and deterministic budget selection in their proof files.

These calculations assume the exact mathematical model. They do not simulate faulty recovery, calibration drift, non-Markovian baths, hidden environment monitoring or subcell controls. No laboratory performance or optimal gate count is inferred from them.
