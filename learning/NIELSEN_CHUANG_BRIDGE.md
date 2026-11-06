# From Nielsen–Chuang to finite-cadence quantum sensing

[Repository overview](../README.md) · [30-milestone map](MILESTONES.md) · [Exact model and results](../science/model.md)

Imagine a clock whose hand advances at an unknown rate. A longer observation can reveal that rate more precisely, but a full revolution can hide how many turns occurred. A quantum sensor has a related difficulty: the unknown signal writes a relative phase, noise disrupts that phase, and a final measurement supplies only a random outcome. This project asks how accurately the rate can be learned when error correction is available only at regularly spaced boundaries.

Two controls have different roles. The **correction interval** determines how long noise and signal act before the next recovery. A **physical compensation field** subtracts a current estimate of the signal during that interval. The main result identifies when one sufficiently small interval, chosen once, can support inverse-square mean-squared error as the total sensing time grows. The grid result quantifies how accurately the compensation field must then be selectable. The full statements and their hypotheses are in the [model](../science/model.md).

## The selected source and how to use it

The educational anchor is **Michael A. Nielsen and Isaac L. Chuang, _Quantum Computation and Quantum Information_, 10th Anniversary Edition, Cambridge University Press (2010), ISBN 9781107002173**. The [publisher record](https://www.cambridge.org/highereducation/books/quantumcomputation-and-quantuminformation/01E10196D0A682A6AEFFEA52D53BE9AE), [chapter contents](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE/contents/729A1063B8E18926B2B83C43A9D3F892), and [detailed contents](https://assets.cambridge.org/97811070/02173/toc/9781107002173_toc.pdf) identify the edition and section pointers below.

Consult these parts as their concepts become useful. The bridge supplies the project's additional steps, and the [milestone map](MILESTONES.md) organizes its scientific story. The explanations below are original; the contents pointers do not imply that the textbook contains the research theorems proved here.

| Anchor location | Foundation to bring into this project | Next project connection |
|---|---|---|
| §§2.1–2.2 | Vectors, matrices, tensor products, unitary dynamics and measurement probabilities | A sensor, an ancilla, a signal generator and a measured phase |
| §§2.4–2.5 | Mixed states, reduction to a subsystem and purification | Encode two carefully chosen sensor states using noiseless ancillary space |
| §§8.2.2–8.2.4 | Describing an unobserved environment through a completely positive quantum operation | The exact physical cell and its Kraus operators |
| §8.4.1 | Continuous-time noise described by a generator | Exponentiate the simultaneous signal-plus-noise generator for a whole cell |
| §9.2.1 | Operational distinguishability of two states | Why nearby frequencies cannot be separated arbitrarily well with a fixed sensing budget |
| §10.3, especially §10.3.1 | A code corrects a linear space of errors through conditions on error products | Correct the full algebra generated during a finite cell, then preserve a useful signal tangent |

The selected anchor supplies the quantum-information foundation. The channel RLD information bound, its adaptive chain rule, the exact finite-time support argument, and the global statistical budget argument need additional derivations or research theorems. Their roles are identified below and in the [attribution map](../references/RELATED_WORK.md).

## 1. Translate the objects into an experiment

A pure state vector describes amplitudes for measurement outcomes. A density operator $`\mathstrut{\rho}`$ also describes mixtures and is the object evolved by a noisy channel. The dagger in $`\mathstrut{G^\dagger}`$ means conjugate transpose; a Hermitian matrix satisfies $`\mathstrut{G=G^\dagger}`$ and can generate a physical Hamiltonian. We use units with $`\mathstrut{\hbar=1}`$.

The unknown real number is $`\mathstrut{\omega}`$, known initially only to lie in $`\mathstrut{[-W,W]}`$. The known matrix $`\mathstrut{G}`$ specifies how it acts: the signal Hamiltonian is $`\mathstrut{\omega G}`$. The controller supplies $`\mathstrut{-cG}`$, leaving residual detuning $`\mathstrut{\delta=\omega-c}`$. This control changes the physical evolution even though $`\mathstrut{\omega}`$ itself is unchanged.

| Notation here | Operational meaning |
|---|---|
| $`\mathstrut{G}`$ | Known signal direction; the unknown quantity is its coefficient $`\mathstrut{\omega}`$ |
| $`\mathstrut{L_j}`$ | Actual Hermitian noise operators, with their fixed rates absorbed into them |
| $`\mathstrut{F_j,\gamma_j}`$ | Known directions and possibly unknown rates, with $`\mathstrut{L_j=\sqrt{\gamma_j}F_j}`$ |
| $`\mathstrut{\tau}`$ | Duration of one complete sensing cell |
| $`\mathstrut{\mathcal E_{\omega,c}^{(\tau)}}`$ | Physical channel for that cell, before recovery |
| $`\mathstrut{V}`$ | Isometry encoding a logical qubit into sensor plus ancilla |
| $`\mathstrut{\mathcal R}`$ | Decoder to the logical qubit; re-encoding prepares the next cell |
| $`\mathstrut{\Lambda_\delta}`$ | Corrected logical channel for one physical cell |
| $`\mathstrut{T}`$, $`\mathstrut{N=\lfloor T/\tau\rfloor}`$ | Hard sensing-time budget and maximum number of whole cells |

A channel can be written as $`\mathstrut{\mathcal N(\rho)=\sum_a K_a\rho K_a^\dagger}`$, with $`\mathstrut{\sum_a K_a^\dagger K_a=I}`$ for trace preservation. The matrices $`\mathstrut{K_a}`$ are Kraus operators. Their labels can describe mathematical alternatives in an unobserved environment; writing them down does not give the experimenter access to those alternatives. An ancilla is an additional quantum system. Here it is noiseless and does not sense $`\mathstrut{\omega}`$ inside a cell, so the joint cell is $`\mathstrut{\mathcal E_{\omega,c}^{(\tau)}\otimes\mathrm{id}_A}`$.

The performance criterion is

```math
R_T^*=\inf_{\mathsf P}\sup_{\omega\in[-W,W]}
\mathbb E_\omega[(\widehat\omega-\omega)^2].
```

For each allowed protocol $`\mathstrut{\mathsf P}`$, take its worst mean-squared error across the fixed band; then choose the best protocol. The expectation includes every outcome, including an incorrect early decision. Heisenberg order means this **mean-squared error** scales as $`\mathstrut{T^{-2}}`$; the corresponding root-mean-square error scales as $`\mathstrut{T^{-1}}`$. SQL order means mean-squared error $`\mathstrut{T^{-1}}`$. These statements do not assume an unbiased estimator. See [the access model](../science/model.md#allowed-operations-and-resources).

## 2. A whole noisy cell differs from a leading-error approximation

For Hermitian jumps, the physical cell is

```math
\begin{aligned}
\mathcal D(\rho)
&=\sum_j\left(L_j\rho L_j-\frac12\{L_j^2,\rho\}\right),\\
\mathcal E_{\omega,c}^{(\tau)}
&=\exp\!\left[\tau\bigl(\mathcal D-i\delta[G,\cdot]\bigr)\right].
\end{aligned}
```

The commutator $`\mathstrut{[A,B]=AB-BA}`$ describes the Hamiltonian action; the anticommutator $`\mathstrut{\{A,B\}=AB+BA}`$ occurs in the dissipator. The exponential solves the dynamics over the full interval. When the signal and noise actions do not commute, this is generally different from applying a noise channel and a separate signal rotation in succession. Consequently, a rotation after the cell cannot generally replace a field present throughout it.

The short-time expansion contains leading errors involving the identity and individual jumps. A positive-duration cell also contains trajectories with two, three, or any finite number of jumps. Their products matter even if high-count trajectories are unlikely. The relevant algebra is

```math
\mathcal A=C^*(I,L_1,\ldots,L_m).
```

In this finite-dimensional Hermitian setting, $`\mathstrut{\mathcal A}`$ is the complex linear span of all finite words in the jumps, including the empty word $`\mathstrut{I}`$. It is closed under multiplication and adjoints. This is a larger object than the real Hermitian span of the leading operators and their quadratic combinations used in fast-control sensing. The distinction between those spaces is the source of the [four-level separation](../science/fast_fixed_separation.md).

At zero detuning, all Kraus operators of the noise-only cell can be taken in $`\mathstrut{\mathcal A}`$. When $`\mathstrut{G\in\mathcal A}`$, the [converse](../science/converse_proof.md#2-exact-finite-time-kraus-support) proves the stronger statement that the exact physical Kraus span equals $`\mathstrut{\mathcal A}`$ at every detuning. That second claim uses the signal's membership in the algebra; it must not be transferred to arbitrary $`\mathstrut{G}`$.

## 3. From error correction to a signal-preserving algebra code

The code condition associated with the anchor's error-correction theory is

```math
V^\dagger(E_a^\dagger E_b\otimes I_A)V
=C_{ab}I_2.
```

The left side describes what an error product does inside the logical two-dimensional space. Its being a scalar multiple of the identity means the corresponding error information does not distinguish logical zero from logical one. A recovery can then reverse the errors without learning the encoded quantum information. The matrix $`\mathstrut{C}`$ describes overlaps of error sectors, so different errors need not have distinct, perfectly distinguishable syndromes.

For a complete algebra, a convenient sufficient condition is

```math
V^\dagger(A\otimes I_A)V=\alpha_A I_2
\qquad\text{for every }A\in\mathcal A.
```

Every product $`\mathstrut{E_a^\dagger E_b}`$ remains in the algebra, so this single condition covers the entire error space. The sensing requirement adds another demand: the signal must still act differently on the two logical states.

The [explicit construction](../science/constructive_proof.md#2-an-explicit-code-and-a-rate-independent-decoder) achieves both demands by removing the algebra component of $`\mathstrut{G}`$:

```math
Q=G-\Pi_{\mathcal A}G=Q_+-Q_-.
```

Here $`\mathstrut{\Pi_{\mathcal A}}`$ is orthogonal projection using the matrix inner product $`\mathstrut{\langle X,Y\rangle=\mathrm{Tr}(X^\dagger Y)}`$. The positive and negative parts $`\mathstrut{Q_+}`$ and $`\mathstrut{Q_-}`$ have disjoint supports. Because $`\mathstrut{I\in\mathcal A}`$, the residual $`\mathstrut{Q}`$ is traceless, so these parts have the same trace $`\mathstrut{s>0}`$ when $`\mathstrut{G\notin\mathcal A}`$.

Normalize them to density operators $`\mathstrut{\rho_0=Q_+/s}`$ and $`\mathstrut{\rho_1=Q_-/s}`$. Their expectation difference against every algebra element is zero, but their signal expectation difference is positive. Purify the two states using disjoint ancilla supports. This makes every off-diagonal sensor matrix element between the codewords vanish, while preserving the equal diagonal expectations for all algebra elements. The resulting code therefore corrects the algebra and retains a logical signal difference. Its persistent ancilla dimension is at most the sensor dimension.

Diagonalizing the scalar Gram matrix $`\mathstrut{C}`$ gives orthogonal error isometries. The decoder reverses those isometries and has a trace-preserving extension on their unused complement. It corrects every trace-preserving channel whose Kraus operators belong to the algebra. The recovery therefore depends on the algebra and code, rather than on the probabilities of individual errors.

This last fact explains the unknown-rate extension. For known directions $`\mathstrut{F_j}`$ with fixed unknown $`\mathstrut{0\le\gamma_j\le\Gamma_j}`$, construct the code for the envelope $`\mathstrut{\mathcal A_F=C^*(I,F_1,\ldots,F_m)}`$. If $`\mathstrut{G\notin\mathcal A_F}`$, one decoder works for the whole rate box. If a rate vanishes, the actual noise algebra can shrink. Membership in the envelope alone therefore cannot establish a converse for every such realization. See [the separate rate quantifiers](../science/model.md#unknown-rates-along-known-directions).

## 4. Worked example: a qubit, one ancilla and unknown jump times

Take a sensor qubit with $`\mathstrut{G=Z/2}`$ and $`\mathstrut{L=\sqrt\gamma X}`$, with $`\mathstrut{\gamma>0}`$. The Pauli matrix $`\mathstrut{Z}`$ distinguishes the basis states, while $`\mathstrut{X}`$ interchanges them. The noise algebra is the span of $`\mathstrut{I}`$ and $`\mathstrut{X}`$, so $`\mathstrut{Z/2}`$ lies outside it.

Use one noiseless ancilla and encode

```math
|0_L\rangle=|0\rangle_S|0\rangle_A,
\qquad
|1_L\rangle=|1\rangle_S|1\rangle_A.
```

Both codewords have even parity. A sensor flip carries them to the odd-parity sector. At each boundary, measure $`\mathstrut{Z_SZ_A}`$ and apply $`\mathstrut{X_S}`$ when the result is odd. This reveals a parity error without distinguishing logical zero from logical one. The two-dimensional error space is corrected because $`\mathstrut{V^\dagger X_SV=0}`$ and $`\mathstrut{X_S^2=I}`$.

The fixed recovery exactly corrects the noise-only cell at $`\mathstrut{\delta=0}`$, including cells with several flips. Away from zero, the **times** of those flips affect the accumulated phase. In a Poisson representation, a flip reverses the sign with which the residual signal acts. A no-jump trajectory accumulates signed sensing time $`\mathstrut{S=\tau}`$. If exactly one jump occurs at time $`\mathstrut{t}`$, then

```math
S=t-(\tau-t)=2t-\tau.
```

The final parity correction removes the flip, but the remaining logical phase depends on $`\mathstrut{S}`$. Parity does not reveal $`\mathstrut{t}`$. For an arbitrary trajectory,

```math
S=\int_0^\tau(-1)^{N_\gamma(t)}\,dt,
\qquad -\tau\le S\le\tau.
```

Here $`\mathstrut{N_\gamma(t)}`$ counts jumps in the mathematical representation. The experimental protocol never reads this record. Averaging the residual phases gives the exact corrected coherence multiplier

```math
f(z)=\mathbb E e^{-izR},
\qquad z=\tau(\omega-c),\quad R=S/\tau,
\quad \lambda=\gamma\tau.
```

The [exact response](../science/grid_upper.md#2-exact-corrected-cell) derives $`\mathstrut{f}`$ from a two-state telegraph process. In particular,

```math
a=\mathbb E R=\frac{1-e^{-2\lambda}}{2\lambda}>0,
\qquad
\left|e^{iaz}f(z)-1\right|
\le\frac{\mathrm{Var}(R)}2 z^2.
```

The continuous value at zero rate is $`\mathstrut{a=1}`$. The first-order response is a useful phase with slope $`\mathstrut{a}`$; the spread of unobserved phases contributes only a quadratic mismatch near $`\mathstrut{z=0}`$. Perfect compensation sets $`\mathstrut{z=0}`$ and makes every trajectory's residual phase vanish. Improving the estimate of $`\mathstrut{\omega}`$ therefore improves the quality of subsequent longer sensing batches.

To read the signal, prepare $`\mathstrut{|+_L\rangle=(|00\rangle+|11\rangle)/\sqrt2}`$, run $`\mathstrut{n}`$ cells with a recovery after **each** cell, and finally measure logical $`\mathstrut{X}`$ or $`\mathstrut{Y}`$. The logical density operator is

```math
\rho_L^{(n)}=\frac12
\begin{pmatrix}
1&f(z)^n\\
(f(z)^*)^n&1
\end{pmatrix}.
```

Thus the two means are $`\mathstrut{\mathbb EX=\mathrm{Re}[f(z)^n]}`$ and $`\mathstrut{\mathbb EY=-\mathrm{Im}[f(z)^n]}`$. The physical observables $`\mathstrut{X_SX_A}`$ and $`\mathstrut{Y_SX_A}`$ realize these logical measurements. Each result is $`\mathstrut{+1}`$ or $`\mathstrut{-1}`$; many independent preparations estimate its mean. Measuring both quadratures using $`\mathstrut{m}`$ independent preparations for each costs exactly $`\mathstrut{2mn}`$ cells, or $`\mathstrut{2mn\tau}`$ sensing time. This accounting is used in the grid theorem.

This example gives the mechanism and actual operations. Its exact response has prior antecedents, including [FIXED21](../references/SOURCES.md#fixed21); the linked proof supplies the present estimation and resource argument.

## 5. From a correctable point to a global estimate

For a general algebra code, write the encoding channel as $`\mathstrut{\mathcal V(\rho)=V\rho V^\dagger}`$ and define $`\mathstrut{\Lambda_\delta=\mathcal R\circ(\mathcal E_\delta^{(\tau)}\otimes\mathrm{id}_A)\circ\mathcal V}`$. Exact correction gives $`\mathstrut{\Lambda_0=\mathrm{id}_2}`$. The signal derivative at that point is a logical Hamiltonian generated by

```math
B_\tau=\int_0^\tau e^{t\mathcal D^\dagger}(G)\,dt,
\qquad H_L=V^\dagger(B_\tau\otimes I_A)V.
```

The adjoint dissipator describes evolution of observables rather than states. Its integral accounts for the signal acting throughout the noisy cell. Replacing this quantity by $`\mathstrut{\tau G}`$ would generally miss the finite-time change in signal response.

Hermitian noise makes the dissipator self-adjoint and negative semidefinite in the matrix inner product. It preserves both the algebra and its orthogonal complement. Each eigenvalue of the integrated exponential is positive, which gives the logical gap

```math
b_\tau=\frac{\langle Q,\int_0^\tau e^{t\mathcal D}(Q)\,dt\rangle}{s}>0.
```

The [tangent and remainder argument](../science/constructive_proof.md#4-the-exact-finite-cell-signal-tangent) goes further than a derivative: it bounds the difference between $`\mathstrut{n}`$ actual corrected cells and the corresponding logical unitary by $`\mathstrut{4n\delta^2\tau^2\|G\|^2}`$ in diamond norm. This norm controls distinguishability even with an ancillary system. A fixed logical $`\mathstrut{Y}`$ measurement consequently has a mean close to $`\mathstrut{\sin(nb_\tau\delta)}`$.

Suppose the current valid frequency interval is $`\mathstrut{[c-w,c+w]}`$. Choose the physical field to be its center and take a batch length proportional to $`\mathstrut{1/(\tau w)}`$. In the outer portions of the interval, the desired phase then stays in a known range with the correct sign. Meanwhile the accumulated quadratic error is of order $`\mathstrut{\tau w}`$, so it becomes smaller as localization improves. A sufficiently small once-chosen $`\mathstrut{\tau}`$ makes the first stage reliable as well. Known lower and upper bounds on $`\mathstrut{b_\tau}`$ suffice; the actual rate need not be known for this continuous-field sign test.

The estimator retains one of two overlapping intervals:

```math
I_+=[c-w/2,c+w],\qquad
I_-=[c-w,c+w/2].
```

Both have half-width $`\mathstrut{3w/4}`$. A point near the center belongs to both, so a nearly zero mean need not be reliably assigned a sign. A point outside that overlap is excluded only by an incorrect sign decision. Every retained interval lies inside its predecessor, even after a failure.

That nesting turns local reliability into a global mean-squared-error bound. If the first exclusion is at stage $`\mathstrut{j}`$, the final estimate and truth are still at most $`\mathstrut{2w_{j-1}}`$ apart. Earlier mistakes would cost more, so early stages receive more repetitions. The [weighted first-failure calculation](../science/constructive_proof.md#8-global-risk-without-an-uncharged-accurate-prior) gives

```math
\mathbb E(\widehat\omega-\omega)^2
\le w_K^2+4\sum_{j=1}^K w_{j-1}^2p_j
\le13w_K^2.
```

The chosen repetitions make the total sensing time at most $`\mathstrut{B/w_K}`$ for a fixed constant $`\mathstrut{B}`$. A deterministic stopping depth then gives $`\mathstrut{w_K}`$ of order $`\mathstrut{1/T}`$ while keeping every history within $`\mathstrut{T}`$. This proves the global $`\mathstrut{O(T^{-2})}`$ upper bound from the original fixed band. A two-frequency discrimination argument supplies the matching lower order; no preliminary accurate estimate is provided for free.

The construction keeps its code, quantum readout and correction interval fixed. Its compensation values become more accurate as the intervals shrink. It uses at most $`\mathstrut{T/\tau}`$ corrected cells, $`\mathstrut{O(\log T)}`$ field settings and $`\mathstrut{O((\log T)^2)}`$ independent prepared/read batches. These are ideal sensing-time resources; boundary operation duration and implementation errors are outside the model.

## 6. Why a converse requires the entire physical channel

A poor response after one decoder would only show a limitation of that decoder. The [general converse](../science/converse_proof.md) instead studies the channel before any recovery. For $`\mathstrut{G\in\mathcal A}`$, its trajectory Kraus operators have exact span $`\mathstrut{\mathcal A}`$ at every detuning. The proof uses a positive trajectory integral and continuity to reach every finite jump word. It does not assign positive probability to simultaneous jumps or to a jump exactly at a boundary.

The Choi state packages this channel into one positive matrix:

```math
J_\delta=(\mathcal E_\delta^{(\tau)}\otimes\mathrm{id})
(|\Phi_d\rangle\langle\Phi_d|),
\qquad
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{a=1}^d|aa\rangle.
```

Its support is the vectorized Kraus span. Support means the subspace with nonzero eigenvalues, rather than the entire ambient matrix space. The support stays fixed as $`\mathstrut{\delta}`$ varies. On the compact range allowed by the fixed frequency band and bounded compensation field, its smallest eigenvalue **within that support** stays positive.

This is the hypothesis needed for a finite channel right-logarithmic-derivative Fisher-information bound. RLD information measures statistical sensitivity through a derivative and an inverse on the support. Its channel formula and chain rule are research inputs from [Katariya–Wilde, Propositions 29 and 38](../references/SOURCES.md#rld21), beyond the selected textbook foundation. The project establishes their applicability to the physical cell and then keeps the full classical history together with all quantum memory.

In each fixed history branch, the controller's chosen number $`\mathstrut{c(h)}`$ is held fixed when differentiating with respect to $`\mathstrut{\omega}`$. The distribution of histories itself can depend on $`\mathstrut{\omega}`$; its information is retained. The chain rule bounds the additional information per cell by one constant $`\mathstrut{M}`$, even with arbitrary adaptive boundary instruments and noiseless memory. After $`\mathstrut{N}`$ cells, the data Fisher information is at most $`\mathstrut{NM}`$.

A smooth prior inside the fixed band and an integration-by-parts argument convert that statement into

```math
R_T^*\ge\frac1{NM+\pi^2/W^2}.
```

This Bayesian, or van Trees, step is proved in [the converse's global-risk section](../science/converse_proof.md#5-global-risk-without-an-unbiasedness-assumption). It applies to biased estimators as well. The consequence is an $`\mathstrut{\Omega(T^{-1})}`$ obstruction for each fixed positive clock and fixed bounded compensation range. It does not establish SQL attainability: indistinguishable frequencies, or a scalar signal generator, can leave a constant error floor.

## 7. What a finite compensation grid changes

Return to the transverse qubit, now with known $`\mathstrut{\gamma>0}`$. Suppose the physical field takes values only on a calibrated lattice of spacing $`\mathstrut{\Delta}`$. Its nearest point can remain displaced from the current interval center even when the frequency interval is very narrow. The exact response $`\mathstrut{f}`$ then has a known reference phase, and residual within-cell phase spread limits the useful coherent batch length.

The [grid construction](../science/grid_upper.md#5-one-refinement-stage-using-two-fixed-measurements) uses dimensionless frequency $`\mathstrut{x=\tau\omega}`$, field $`\mathstrut{u=\tau c}`$, mesh $`\mathstrut{h=\tau\Delta}`$ and interval half-width $`\mathstrut{w}`$. Writing $`\mathstrut{f(z)=|f(z)|e^{-i\phi(z)}}`$, it chooses a nearest field point to center $`\mathstrut{q}`$, sets $`\mathstrut{d=q-u}`$ and forms

```math
\widehat\mu=\cos\theta\,\overline Y-\sin\theta\,\overline X,
\qquad \theta=n\phi(d).
```

These are sample means from the same two fixed quantum observables in the worked example. The subtraction aligns their expected phase with the interval center using classical processing. It leaves the useful sign of $`\mathstrut{x-q}`$ while the actual physical field remains on the grid. The nonlinear phase $`\mathstrut{\phi}`$ depends on the known rate, which is why the unknown-rate continuous-field theorem does not automatically provide this grid upper bound.

Choosing $`\mathstrut{n}`$ of order $`\mathstrut{1/(w+h^2)}`$ keeps sufficient visibility. As the interval becomes finer than the field spacing, additional independent repetitions continue to improve the estimate. The grid therefore imposes a statistical cost, rather than a fixed estimation floor. Both quadrature sets and every wrong refinement are charged; the cost bound is of order $`\mathstrut{1/w_K+h^2/w_K^2}`$ cells. In physical units this yields

```math
R_T^*=\Theta\!\left(T^{-2}+\frac{\tau\Delta^2}{T}\right)
```

under the [stated small-band conditions](../science/grid_upper.md#4-fixed-band-and-grid-range), available nearest grid points, and $`\mathstrut{0<\Delta\le\Delta_0\le W}`$.

The matching [lower bound](../science/grid_lower.md) does not use the parity decoder. At every nonzero detuning the unrecovered physical qubit channel has full Choi rank, whose smallest eigenvalue opens quadratically near zero. Inside a suitable lattice gap, every available field remains a distance of order $`\mathstrut{\Delta}`$ from the signal. A uniform channel-information bound then applies to every allowed adaptive strategy, including changing grid values after every cell. Boundary dithering is included; switching fields inside a cell would change the access model.

At fixed $`\mathstrut{\tau}`$, retaining Heisenberg order requires $`\mathstrut{\Delta=O(T^{-1/2})}`$; dimensionally the comparison is $`\mathstrut{\tau\Delta^2\lesssim T^{-1}}`$. A fixed nonzero mesh eventually gives SQL order. The constants depend on positive noise; at zero rate this particular grid obstruction disappears. The exponent has established noisy-phase-estimation antecedents, credited in [GLOBAL22 and related work](../references/RELATED_WORK.md#why-the-calibrated-grid-requires-a-physical-channel-bound).

## 8. Why faster correction is a separate resource

The four-level example uses

```math
L=\mathrm{diag}(-3,-1,1,3),\qquad G=L^3.
```

The cubic signal cannot be a combination of $`\mathstrut{I,L,L^2}`$: a cubic polynomial cannot agree with a quadratic at four distinct points unless their difference is zero, which its leading coefficient prevents. Yet $`\mathstrut{G}`$ plainly belongs to the full algebra generated by $`\mathstrut{L}`$. An explicit code has equal expectations of $`\mathstrut{I,L,L^2}`$ in its two logical states and different expectations of $`\mathstrut{G}`$. It therefore corrects the leading infinitesimal errors while retaining a signal. This is the setting of the inherited fast-control [HNLS criterion](../references/SOURCES.md#hnls18).

For that code, the error of one short corrected cell is bounded by a constant times $`\mathstrut{h^2}`$. The [global fast protocol](../science/fast_fixed_separation.md#3-a-global-fast-clock-protocol-with-every-outcome-charged) chooses $`\mathstrut{h(T)=\Theta(T^{-1})}`$, controls the accumulated remainder, and pays for all localization trials. It attains $`\mathstrut{\Theta(T^{-2})}`$ error and uses $`\mathstrut{\Theta(T^2)}`$ recovery applications in this construction. A fixed positive $`\mathstrut{h=\tau}`$ belongs to a different regime: the full algebra converse applies, even with unlimited compensation amplitude in this commuting example.

Its exact channel also repeats with frequency period $`\mathstrut{\pi/\tau}`$. On an identifiable interval shorter than this period, two quadratures attain SQL order. A band containing an alias pair has a positive error floor. The [alias analysis](../science/fast_fixed_separation.md#5-exact-aliases-and-an-alias-free-sql-upper-bound) explains why a local phase response or an SQL lower bound alone cannot settle global estimation.

## 9. Assemble the scientific account

Three questions organize the result. **Which errors can occur during a complete cell?** Their algebra controls exact correction and the physical-channel support argument. **Which useful signal remains near a corrected point?** The integrated tangent and quadratic remainder control reliable longer sensing batches. **How is that local behavior paid for and used globally?** Nested intervals, weighted failure probabilities and deterministic budgets answer this without an accurate initial estimate.

The selected textbook provides the language of states, channels, purification, distinguishability and error correction. The project connects those foundations to a precise finite-cadence sensing model. The [constructive proof](../science/constructive_proof.md), [converse](../science/converse_proof.md), [grid pair](../science/grid_upper.md) and [fast/fixed example](../science/fast_fixed_separation.md) supply the specialist arguments; the [primary-source index](../references/SOURCES.md) distinguishes inherited tools from these derivations. The [30 milestones](MILESTONES.md) connect the same story from individual objects to the full result.

The guarantees assume Hermitian parameter-independent Markovian noise, a known signal direction, noiseless ancillary memory, ideal boundary operations and a calibrated field acting throughout each cell. They do not analyze faulty recovery, unknown field bias, general non-Hermitian jumps, inaccessible persistent bath memory or observed jump records. The [finite verification suite](../verification/README.md) checks concrete identities and parameter cases. The universal conclusions depend on the written proofs and their hypotheses.
