# Achieving the cadence and cell-budget bounds

[Theorem and model](cadence_budget.md) · [Adaptive lower bounds](cadence_budget_converse.md)

The sensor has known commuting Hermitian jumps $`\mathstrut{L_1,\ldots,L_r}`$ and known signal operator $`\mathstrut{G=g(L_1,\ldots,L_r)}`$. All operators and the frequency band $`\mathstrut{[-W,W]}`$ are fixed. Write $`\mathstrut{s\ge1}`$ for the least total polynomial degree of $`\mathstrut{g}`$ on the joint spectrum and put $`\mathstrut{m=\lceil s/2\rceil}`$. The environment is inaccessible. The construction below uses a fixed sensor code and resettable boundary operations. Its persistent coherent memory fits in the sensor itself.

## A code that preserves the signal slope

Let $`\mathstrut{\mathscr P_k}`$ be the real span of the joint monomials of total degree at most $`\mathstrut{k}`$, evaluated on the sensor. Project $`\mathstrut{G}`$ orthogonally onto $`\mathstrut{\mathscr P_{2m-2}}`$ in the Hilbert–Schmidt inner product, and let $`\mathstrut{Q}`$ be the residual. By the definition of $`\mathstrut{s}`$, $`\mathstrut{2m-2\lt s}`$, so $`\mathstrut{Q\ne0}`$. The identity belongs to $`\mathstrut{\mathscr P_{2m-2}}`$, hence $`\mathstrut{Q}`$ has zero trace. In a common diagonal basis write $`\mathstrut{Q=\mathrm{diag}(q_i)}`$ and $`\mathstrut{b_Q=\sum_{q_i\gt 0}q_i=-\sum_{q_i\lt 0}q_i}`$. Define the code isometry $`\mathstrut{V}`$ by the real, disjointly supported vectors

```math
V|0\rangle=\sum_{q_i>0}\sqrt{q_i/b_Q}\,|i\rangle,
\qquad
V|1\rangle=\sum_{q_i<0}\sqrt{-q_i/b_Q}\,|i\rangle.
```

For any $`\mathstrut{A\in\mathscr P_{2m-2}}`$, the off-diagonal matrix elements of $`\mathstrut{V^\dagger A V}`$ vanish and the difference of its diagonal elements is $`\mathstrut{\mathrm{Tr}(AQ)/b_Q=0}`$. Thus the Knill–Laflamme conditions hold for the error space $`\mathstrut{\mathscr P_{m-1}}`$. The compressed signal $`\mathstrut{G_L=V^\dagger G V}`$ is diagonal and has gap

```math
\Delta_G=\langle0|G_L|0\rangle-\langle1|G_L|1\rangle
=\mathrm{Tr}(GQ)/b_Q=\mathrm{Tr}(Q^2)/b_Q>0.
```

The decoder can be chosen real. For $`\mathstrut{A,B\in\mathscr P_{m-1}}`$ define the scalar Gram form by $`\mathstrut{V^\dagger ABV=\langle A,B\rangle_V I_2}`$. It is a real positive semidefinite form. Choose representatives $`\mathstrut{p_a}`$ of an orthonormal basis of its quotient by the null space, with $`\mathstrut{p_0=I}`$. The error isometries $`\mathstrut{W_a=p_aV}`$ have orthogonal ranges and $`\mathstrut{W_0=V}`$. Let $`\mathstrut{P=\sum_aW_aW_a^\dagger}`$. One completely positive trace-preserving decoder is

```math
\mathcal R(X)=\sum_a W_a^\dagger X W_a+\mathrm{Tr}[(I-P)X]\,|0\rangle\langle0|.
```

For every $`\mathstrut{A\in\mathscr P_{m-1}}`$, each $`\mathstrut{W_a^\dagger AV}`$ is scalar and $`\mathstrut{(I-P)AV=0}`$. Zero Gram norm means $`\mathstrut{AV=0}`$, so the same statement holds for the entire error space, including its Gram null space.

## The exact logical coherence

With $`\mathstrut{c}`$ the chosen compensation frequency, set $`\mathstrut{\delta=\omega-c}`$. Since $`\mathstrut{G}`$ and all the jumps commute, the physical cell is the Gaussian dephasing channel followed by $`\mathstrut{\operatorname{Ad}_{e^{-ih\delta G}}}`$. The known rotation $`\mathstrut{e^{+ihcG}}`$ can be applied at the boundary immediately before decoding, with the same effect as the in-cell counterfield. The construction holds for either realization in this commuting model.

Write $`\mathstrut{J=\sum_{j=1}^r L_j^2}`$. An exact Kraus family at zero detuning is indexed by multi-indices $`\mathstrut{\mathbf k=(k_1,\ldots,k_r)\in\mathbb N^r}`$:

```math
K_{\mathbf k}(h)=e^{-hJ/2}\prod_{j=1}^r\frac{h^{k_j/2}L_j^{k_j}}{\sqrt{k_j!}},
\qquad |\mathbf k|=\sum_j k_j.
```

At nonzero detuning, multiply each Kraus operator by $`\mathstrut{e^{-ih\delta G}}`$. The recovered channel $`\mathstrut{\Lambda_{\delta,h}=\mathcal R\circ\mathcal E_{\delta}^{(h)}\circ\mathcal V}`$, where $`\mathstrut{\mathcal V(X)=VXV^\dagger}`$, acts on $`\mathstrut{|0\rangle\langle1|}`$ by a scalar $`\mathstrut{f_h(\delta)}`$ and on its adjoint by the conjugate scalar. Indeed, the matrices $`\mathstrut{W_a^\dagger K_{\mathbf k}(h)e^{-ih\delta G}V}`$ are diagonal because the two codewords have disjoint supports. The complement reset term vanishes on the off-diagonal operator because $`\mathstrut{P}`$ preserves both support sectors, which are orthogonal. Logical populations therefore contribute no coherence. Complete positivity and trace preservation give $`\mathstrut{|f_h(\delta)|\le1}`$, by Cauchy–Schwarz over the two diagonal entries of the syndrome Kraus operators and their total squared norm bounds.

At $`\mathstrut{\delta=0}`$, let $`\mathstrut{u_{a\mathbf k,x}=\langle x|W_a^\dagger K_{\mathbf k}(h)V|x\rangle}`$ for $`\mathstrut{x\in\{0,1\}}`$. These numbers are real. Define $`\mathstrut{\ell_x=\sum_{\mathbf k}\|(I-P)K_{\mathbf k}(h)V|x\rangle\|^2}`$. Trace preservation gives $`\mathstrut{\sum_{a,\mathbf k}u_{a\mathbf k,x}^2=1-\ell_x}`$. Hence

```math
1-f_h(0)=\frac12\sum_{a,\mathbf k}(u_{a\mathbf k,0}-u_{a\mathbf k,1})^2
+\frac12(\ell_0+\ell_1).
```

This identity makes the logical coherence loss second order in the uncorrected Kraus amplitudes. To bound it, approximate each $`\mathstrut{K_{\mathbf k}(h)}`$ by $`\mathstrut{B_{\mathbf k}(h)\in\mathscr P_{m-1}}`$. When $`\mathstrut{|\mathbf k|\lt m}`$, keep the terms of the exponential series indexed by $`\mathstrut{t}`$ with $`\mathstrut{|\mathbf k|+2t\le m-1}`$, and otherwise use zero. All retained terms have total degree at most $`\mathstrut{m-1}`$. In the first case every omitted term has $`\mathstrut{h}`$ exponent $`\mathstrut{|\mathbf k|/2+t\ge m/2}`$. There are only finitely many indices with $`\mathstrut{|\mathbf k|\lt m}`$. For the remaining terms, with the operator norm throughout,

```math
\sum_{|\mathbf k|\ge m}\|K_{\mathbf k}(h)\|^2
\le \sum_{n\ge m}\frac{(h\sum_j\|L_j\|^2)^n}{n!}=O(h^m).
```

Consequently $`\mathstrut{\sum_{\mathbf k}\|K_{\mathbf k}-B_{\mathbf k}\|^2=O(h^m)}`$. Each difference of the two syndrome amplitudes and each complement amplitude depends only on $`\mathstrut{K_{\mathbf k}-B_{\mathbf k}}`$, since $`\mathstrut{B_{\mathbf k}}`$ belongs to the exactly corrected error space. There are finitely many syndromes independent of $`\mathstrut{h}`$, so the identity above gives $`\mathstrut{0\le1-f_h(0)=O(h^m)}`$.

A second allowed decoder completes each real codeword support to an orthonormal syndrome basis with shared labels for the corrected syndromes. It maps each support isometrically to its logical label tensored with a syndrome, then discards that syndrome. Extra basis vectors may use any remaining syndrome labels. The off-diagonal recovery factor is the overlap of the two resulting real syndrome–environment vectors at zero detuning. Both vectors have norm one, and their difference vanishes on the corrected polynomial terms. Therefore this completion also has coherence loss of order at most $`\mathstrut{h^m}`$ and the same leading signal slope. The finite-matrix check uses this completion.

For bounded $`\mathstrut{\delta}`$, the finite-dimensional channel exponential also gives a uniform derivative expansion

```math
\partial_\delta\Lambda_{\delta,h}=-ih\,\mathcal R[G,\mathcal V(\,·\,)]+O(h^2)
=-ih[G_L,\,\cdot\,]+O(h^2).
```

For the first equality, expand the derivative of the exponential in $`\mathstrut{h}`$. The leading term is the derivative of its linear term. All remaining terms are bounded by $`\mathstrut{O(h^2)}`$ uniformly on the fixed band of detunings. For the second equality, $`\mathstrut{W_a^\dagger V=0}`$ for $`\mathstrut{a\ne0}`$, so only the $`\mathstrut{W_0=V}`$ syndrome contributes, and the complement term vanishes because $`\mathstrut{(I-P)V=0}`$. In particular $`\mathstrut{f'_h(\delta)=-ih\Delta_G+O(h^2)}`$ for $`\mathstrut{|\delta|\le W}`$.

## A uniformly invertible Ramsey response

Prepare logical $`\mathstrut{|+\rangle}`$, run $`\mathstrut{n}`$ cells with the same value of $`\mathstrut{c}`$, and decode and re-encode between cells. A logical $`\mathstrut{Y}`$ measurement has expectation

```math
Q_{h,n}(\delta)=-\operatorname{Im}[f_h(\delta)^n].
```

Write $`\mathstrut{t=nh}`$. There are fixed positive constants $`\mathstrut{h_0,\eta_0,\zeta}`$ such that, for $`\mathstrut{0\lt h\le h_0}`$, $`\mathstrut{nh^m\le\eta_0}`$ and $`\mathstrut{|\delta|\le W}`$ with $`\mathstrut{t|\delta|\le\zeta}`$,

```math
Q_{h,n}(0)=0,\qquad \partial_\delta Q_{h,n}(\delta)\ge (\Delta_G/2)t.
```

To see this, use $`\mathstrut{|f_h(\delta)-1|\le C(h^m+h|\delta|)}`$ from the zero-detuning estimate and the derivative expansion. Then $`\mathstrut{|f_h(\delta)^{n-1}-1|\le(n-1)|f_h(\delta)-1|\le C(\eta_0+\zeta)}`$, since $`\mathstrut{|f_h|\le1}`$. Differentiating $`\mathstrut{Q_{h,n}}`$ and taking $`\mathstrut{h_0,\eta_0,\zeta}`$ small makes the derivative error less than half of $`\mathstrut{\Delta_G nh}`$. Also $`\mathstrut{f_h(0)}`$ is real. The bound is on the measured response itself, so the estimator below can use its exact inverse, with no systematic error from a linearized response.

## Global estimation and failure accounting

Assume $`\mathstrut{T\ge1}`$, reducing $`\mathstrut{h_0}`$ if necessary. Define the time scale $`\mathstrut{H=h^{1-m}}`$. Choose a small fixed $`\mathstrut{a\gt 0}`$ below $`\mathstrut{\eta_0}`$ and set $`\mathstrut{b=a\min\{T,H\}}`$. Take $`\mathstrut{h_0\le1}`$ and $`\mathstrut{h_0\le a/2}`$ so $`\mathstrut{b\ge2h}`$. A Ramsey batch of time $`\mathstrut{t\le b}`$ then satisfies $`\mathstrut{nh^m=t/H\le a}`$. The following protocol uses at most $`\mathstrut{T}`$ sensing time and has squared risk $`\mathstrut{O(1/(Tb))}`$.

Start with the interval $`\mathstrut{I_0=[-W,W]}`$. A current interval with center $`\mathstrut{c}`$ and half-width $`\mathstrut{w}`$ needs refinement only if $`\mathstrut{w\gt \zeta/b}`$. In that case use sensing time

```math
t_j=h\left\lfloor\frac{\zeta}{2hw}\right\rfloor.
```

Choosing $`\mathstrut{h_0\le\zeta/(4W)}`$ ensures $`\mathstrut{\zeta/(4w)\le t_j\le\zeta/(2w)\lt b/2}`$. Conditional on the true frequency remaining in the current interval, the Ramsey response is increasing throughout that interval. If $`\mathstrut{|\omega-c|\ge w/2}`$, its sign is the sign of $`\mathstrut{\omega-c}`$ and its magnitude is at least $`\mathstrut{\Delta_G\zeta/16}`$. From repeated independent preparations and measurements at this time, take the empirical sign. On a nonnegative sign retain $`\mathstrut{[c-w/2,c+w]}`$. On a negative sign retain $`\mathstrut{[c-w,c+w/2]}`$. The new half-width is $`\mathstrut{\rho w}`$, with $`\mathstrut{\rho=3/4}`$. A frequency in the overlap cannot be lost. Outside the overlap, Hoeffding's inequality guarantees a conditional first-miss probability at most

```math
p_j=(b/T)(t_j/b)^3
```

using $`\mathstrut{O(1+\ln(T/b)+\ln(b/t_j))}`$ independent measurements at stage $`\mathstrut{j}`$. Every batch consumes its full prescribed time on every history.

Let $`\mathstrut{J_*}`$ be the number of refinements, fixed by the initial width and the stopping width. If $`\mathstrut{J_*\gt 0}`$, the last parent width lies in $`\mathstrut{(\zeta/b,\zeta/(\rho b)]}`$. It follows that $`\mathstrut{t_j/b}`$ is bounded above and below by constants times $`\mathstrut{\rho^{J_*-j}}`$. Multiplying the measurement counts by their times and summing the geometric series and its first moment bounds the total localization time by $`\mathstrut{C b(1+\ln(T/b))}`$. Choose $`\mathstrut{a}`$ small enough that $`\mathstrut{C a(1+\ln(1/a))\le1/2}`$, which ensures the localization time is at most $`\mathstrut{T/2}`$ because $`\mathstrut{b/T\le a}`$. The constant $`\mathstrut{C}`$ uses the fixed response margin and $`\mathstrut{\rho}`$ and can be chosen independently of $`\mathstrut{a}`$.

After localization, the last interval has half-width at most $`\mathstrut{\zeta/b}`$. Take its center $`\mathstrut{c}`$ as the compensation, set $`\mathstrut{t_f=h\lfloor b/h\rfloor\in[b/2,b]}`$, and use $`\mathstrut{\lfloor T/(2t_f)\rfloor}`$ independent Ramsey measurements. This count is of order $`\mathstrut{T/b}`$ for $`\mathstrut{a\le1/4}`$. Use the exact monotone response on the last interval. Clip the empirical mean to the range of the response there, invert it, and add $`\mathstrut{c}`$. Conditional on previous localization outcomes that retained the true frequency, clipping does not increase the deviation from the true response. The inverse has Lipschitz constant at most $`\mathstrut{2/(\Delta_G t_f)}`$, so the conditional mean-squared error is $`\mathstrut{O(1/(Tb))}`$, by the variance of the mean of independent sign measurements. The estimate always lies in the last interval.

If a first miss occurs at stage $`\mathstrut{j}`$, that stage's parent interval still contains the true frequency and every later interval. The squared error is therefore at most $`\mathstrut{4w^2=O(1/t_j^2)}`$, where $`\mathstrut{w}`$ is the parent half-width. The risk contribution over all first misses is bounded by

```math
\sum_{j=1}^{J_*}O(t_j^{-2})p_j
=O\!\left(\frac{1}{Tb}\sum_{j=1}^{J_*}\frac{t_j}{b}\right)
=O\!\left(\frac{1}{Tb}\right).
```

These bounds are uniform on the original band and do not require a correct initial estimate or an uncharged restart. They prove

```math
R_h^*(T)\le C'\max\{T^{-2},h^{m-1}/T\}
```

for all $`\mathstrut{T\ge1}`$ and $`\mathstrut{0\lt h\le h_0}`$. When $`\mathstrut{m=1}`$ the coherence time scale is constant and the same argument gives the standard quantum limit $`\mathstrut{O(T^{-1})}`$.

## Achievability under a hard cell cap

Suppose at most $`\mathstrut{M}`$ complete cells and at most $`\mathstrut{T}`$ sensing time are available. A common-duration strategy already attains the variable-clock bound. For $`\mathstrut{m\ge2}`$ choose a fixed $`\mathstrut{h_1\in(0,\min\{1,h_0\}]}`$ and set

```math
h=h_1M^{-1/m},\qquad T_{\mathrm{eff}}=\min\{T,Mh\}.
```

Run the fixed-duration estimator with budget $`\mathstrut{T_{\mathrm{eff}}}`$. Its cell count is at most $`\mathstrut{\lfloor T_{\mathrm{eff}}/h\rfloor\le M}`$. Since $`\mathstrut{Mh=h_1M^{1-1/m}\le h^{1-m}}`$, it stays within the inverse-square regime and gives

```math
R^*(T,M)\le C''\max\{T^{-2},M^{-2+2/m}\}.
```

For $`\mathstrut{m=1}`$, take $`\mathstrut{h=h_1}`$ and $`\mathstrut{T_{\mathrm{eff}}=\min\{T,Mh_1\}}`$. The fixed-duration standard quantum limit yields $`\mathstrut{R^*(T,M)\le C''\max\{T^{-1},M^{-1}\}}`$. These conclusions use sufficiently large $`\mathstrut{T}`$ and $`\mathstrut{M}`$ so $`\mathstrut{T_{\mathrm{eff}}\ge1}`$. The constants are independent of both budgets. Boundary operations consume no sensing time in the stated model, and all the cells used for localization and final estimation count toward both caps.
