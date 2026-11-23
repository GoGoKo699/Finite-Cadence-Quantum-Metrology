# Lower bounds for a hard correction budget

[Theorem and model](cadence_budget.md) · [Matching construction](cadence_budget_protocol.md)

The proof treats the physical sensor before any coding. It allows arbitrary parameter-independent boundary instruments, noiseless memory and feedback as specified in the model. Take $`\mathstrut{Q=\sum_j L_j^2}`$ and $`\mathstrut{L^\alpha=\prod_j L_j^{\alpha_j}}`$ for a multi-index $`\mathstrut{\alpha}`$.

## Exact Kraus expansion and a uniform information bound

An exact Kraus family for a cell is

```math
K_\alpha(h,\omega)
=e^{-hQ/2}\frac{h^{|\alpha|/2}L^\alpha}{\sqrt{\alpha!}}e^{-ih\omega G}.
```

Indeed, on a joint-basis matrix element between tuples $`\mathstrut{\ell_i}`$ and $`\mathstrut{\ell_j}`$, summing the exponential series gives the damping factor $`\mathstrut{e^{-h\|\ell_i-\ell_j\|^2/2}}`$ times the signal phase $`\mathstrut{e^{-ih\omega(g_i-g_j)}}`$. The Gaussian series is absolutely convergent at every finite $`\mathstrut{h}`$.

Choose a monomial basis adapted to the nested spaces $`\mathstrut{\mathcal A_a}`$. Expand $`\mathstrut{e^{hQ}G}`$ in this finite basis. The coefficient $`\mathstrut{c_a(h)}`$ of any basis element of degree $`\mathstrut{a}`$ obeys

```math
c_a(h)=O\!\left(h^{\max\{0,\lceil(a-s)/2\rceil\}}\right).
```

The coefficient is analytic at zero, and $`\mathstrut{Q^jG\in\mathcal A_{2j+s}}`$ makes all its Taylor coefficients below the stated order vanish. For each monomial $`\mathstrut{L^\alpha}`$ of degree $`\mathstrut{a}`$, split $`\mathstrut{\alpha=\beta+\gamma}`$ with $`\mathstrut{|\beta|=\lfloor a/2\rfloor}`$ and $`\mathstrut{|\gamma|=\lceil a/2\rceil}`$. Then

```math
K_\beta^\dagger K_\gamma =
e^{-hQ}\frac{h^{a/2}}{\sqrt{\beta!\gamma!}}L^\alpha.
```

Put $`\mathstrut{c_a(h)\sqrt{\beta!\gamma!}\,h^{1-a/2}}`$ at the corresponding Kraus-index pair, split equally between the two entries when the indices differ. Summing over the basis gives a finite-support Hermitian matrix $`\mathstrut{F_h}`$ with $`\mathstrut{\sum_{\beta,\gamma}(F_h)_{\beta\gamma}K_\beta^\dagger K_\gamma=hG}`$.

Let $`\mathstrut{V_{h,\omega}}`$ be the Kraus isometry and apply an environment gauge $`\mathstrut{e^{i(\omega-\omega_0)F_h}}`$ when differentiating at $`\mathstrut{\omega_0}`$. Its derivative $`\mathstrut{\dot V_h}`$ satisfies $`\mathstrut{V_h^\dagger\dot V_h=0}`$. The ungauged squared derivative has norm $`\mathstrut{O(h^2)}`$. The norm squared contributed by one balanced pair in the gauge is bounded by a constant times

```math
|c_a(h)|^2h^{2-a+\lfloor a/2\rfloor}
=|c_a(h)|^2h^{2-\lceil a/2\rceil}.
```

For $`\mathstrut{a\le s}`$ the exponent is at least $`\mathstrut{2-m}`$. For $`\mathstrut{a\gt s}`$, the Taylor factor compensates for the larger degree since $`\mathstrut{\lceil a/2\rceil-\lceil s/2\rceil\le\lceil(a-s)/2\rceil}`$. The finite sum, including the ungauged derivative, therefore satisfies

```math
\|\dot V_h^\dagger\dot V_h\|\le C h^{2-m}\qquad(0\lt h\le h_0).
```

This bound is uniform in the operating frequency on the band. The gauge is used only to bound information. It does not expose an environment operation to the controller.

There is also a uniform zero-drift derivative bound for $`\mathstrut{h\ge h_0}`$. Use one Kraus column vector $`\mathstrut{v_i}`$ per distinct joint tuple, with Gram matrix $`\mathstrut{C_h=(\langle v_i,v_j\rangle)_{i,j}}`$. The Gaussian kernel on distinct tuples is strictly positive definite for $`\mathstrut{h\gt 0}`$: its quadratic form is the integral of the squared modulus of a finite sum of distinct Fourier characters against a strictly positive Gaussian density. Signal phases conjugate it by a diagonal unitary. Its least eigenvalue is uniformly positive on $`\mathstrut{[h_0,\infty)}`$, using continuity on compact intervals and convergence to the identity at infinity. Its frequency derivative is uniformly bounded because each off-diagonal derivative has a factor $`\mathstrut{h(g_i-g_j)}`$ times Gaussian decay in $`\mathstrut{h}`$.

Choose the matrix $`\mathstrut{B}`$ with columns $`\mathstrut{v_i}`$ invertible on this finite tuple space. The column derivative $`\mathstrut{D=\tfrac12(B^\dagger)^{-1}\partial_\omega C_h}`$ realizes the Gram derivative and gives $`\mathstrut{\langle v_i,\dot v_i\rangle=0}`$ for every $`\mathstrut{i}`$ because the Gram diagonal is constant. Any difference from another differentiable factorization at that point is an environment gauge: subtract their column derivatives, multiply on the right by $`\mathstrut{B^{-1}}`$, and use equality of Gram derivatives to get a skew-Hermitian generator. Thus the Kraus isometry has a zero-drift derivative with squared norm at most a fixed constant for all $`\mathstrut{h\ge h_0}`$. Degenerate joint eigenspaces use repeated copies of the same column and add no constraint.

## Uniform-cadence risk lower bound

Purify the input, all instruments and all retained records, including an immutable copy of each classical outcome used to choose a control. Pad a stopped strategy with identity calls. The derivative of the final purified state is a sum over the differentiated cell. Terms differentiated at distinct cells are orthogonal. In their inner product the later cell contributes $`\mathstrut{V_h^\dagger\dot V_h=0}`$, also for each classical history when operations between cells are controlled by that history. Therefore the final purified state, and hence any accessible estimator record, have Fisher information bounded by $`\mathstrut{4CNh^{2-m}}`$ with $`\mathstrut{N\le T/h}`$. Here we use the pure-state Fisher bound $`\mathstrut{4\|\partial_\omega\psi\|^2}`$ and monotonicity under discarding systems and measuring.

Van Trees with one fixed smooth prior inside the band bounds worst-case error below by the inverse of the prior information plus the prior average of that Fisher information. The prior contributes a finite sensor-independent constant for fixed $`\mathstrut{W}`$. This yields $`\mathstrut{R_h^*(T)\ge c h^{m-1}/T}`$ uniformly for small $`\mathstrut{h}`$ and large $`\mathstrut{T}`$. The time bound below supplies the other term when it is stronger.

## Arbitrary feedback-chosen durations

For $`\mathstrut{m\ge2}`$ introduce a cutoff $`\mathstrut{0\lt H\le h_0}`$. Use the ungauged derivative on branches with $`\mathstrut{h\lt H}`$, whose norm is at most $`\mathstrut{C H}`$. On branches with $`\mathstrut{h\ge H}`$, use a zero-drift derivative with squared norm at most $`\mathstrut{C H^{2-m}}`$, by the two gauge bounds. For a fixed operating point this is a direct sum of branch isometries controlled by the orthogonal immutable records. Each branch uses a gauge at its chosen duration, which is fixed given that record. The derivative insertion supported on long branches satisfies $`\mathstrut{V^\dagger\dot V_{\rm long}=0}`$ as an operator, including the short branches where it is zero.

Long insertions at different stages are therefore orthogonal even when the classification into short and long depends on the record. Their sum has norm at most $`\mathstrut{C\sqrt{M H^{2-m}}}`$. For short insertions the triangle inequality gives $`\mathstrut{C M H}`$. Together these bound the Fisher information by

```math
F\le C'\left[(MH)^2+M H^{2-m}\right].
```

Choose $`\mathstrut{H=M^{-1/m}}`$ for sufficiently large $`\mathstrut{M}`$. The two terms both have order $`\mathstrut{M^{2-2/m}}`$, so van Trees gives $`\mathstrut{R^*(T,M)\ge c M^{-2+2/m}}`$. This argument is valid with continuously valued classical records: the branch isometries and their gauges are measurable in the duration, and the orthogonality and squared norm sums are integrals over the same retained record measure.

For $`\mathstrut{m=1}`$ use the zero-drift derivative on every branch. Its squared norm is bounded by $`\mathstrut{C\min\{h,1\}}`$. Orthogonality now gives the sum of the squared norms, each averaged over the actual branch weights at that stage. On every history $`\mathstrut{\sum_i\min\{h_i,1\}\le\min\{T,M\}}`$. The Fisher information is consequently at most $`\mathstrut{C'\min\{T,M\}}`$, giving both terms of the $`\mathstrut{m=1}`$ lower bound.

## Elapsed-time limit with adaptive stopping

In the natural Kraus isometry the unknown frequency acts by $`\mathstrut{e^{-ih\omega G}}`$, so the derivative norm of one cell is at most $`\mathstrut{h\|G\|}`$. At a history with remaining exposure cap $`\mathstrut{B}`$, suppose the next duration is $`\mathstrut{h}`$. Each continuation after the next boundary instrument has remaining cap at most $`\mathstrut{B-h}`$. Induct on the remaining number of cells. The controlled continuation has derivative norm at most $`\mathstrut{(B-h)\|G\|}`$ by the induction hypothesis, since its blocks act on orthogonal classical-history records. The boundary instrument is parameter independent, and differentiating the product with the current cell adds at most $`\mathstrut{h\|G\|}`$. A stopped branch has derivative zero. Randomized choices known to the controller are another direct sum over orthogonal records. Thus the whole protocol has a purification with derivative norm at most $`\mathstrut{T\|G\|}`$, including when the duration or stopping time depends on earlier outcomes.

Integrating this bound between two frequencies gives total variation at most $`\mathstrut{T\|G\|\,|\omega-\omega\prime|}`$ for the final estimator records. Choose two frequencies in the fixed band separated by a sufficiently small constant over $`\mathstrut{T}`$. Their record laws have total variation bounded away from one. Testing which frequency is nearer to any proposed estimate gives worst-case squared error at least $`\mathstrut{c/T^2}`$.

The [upper bound](cadence_budget_protocol.md) matches these orders. The channel-extension method and Bayesian information step follow the [primary comparisons](../references/RELATED_WORK.md#correction-budgets-for-commuting-dephasing). The balanced small-cell gauge and the adaptive elapsed-time and cell-budget bounds use the specific commuting model.
