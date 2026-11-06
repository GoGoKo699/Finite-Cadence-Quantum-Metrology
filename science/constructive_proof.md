# A fixed recovery cadence outside the noise algebra

This page proves the constructive direction of the [model and main results](model.md). It gives one fixed encoding and recovery, computes the exact finite-cell signal tangent, and uses an adaptive physical counterfield to attain a global mean-squared error of order $T^{-2}$ under a deterministic sensing-time budget. Every prepared batch and every failed localization stage is included in that budget.

The [converse](converse_proof.md) supplies the negative direction for the actual noise algebra. The [four-level example](fast_fixed_separation.md) makes the distinction from arbitrarily fast recovery explicit. The separate [grid upper bound](grid_upper.md) quantifies finite compensation resolution in a transverse-qubit model.

## 1. Statement and quantifiers

Let the sensor have finite dimension $d$, known Hermitian signal generator $G$, and parameter-independent Hermitian noise directions $F_j$. During a cell of duration $\tau$, the sensor evolves according to

$$
\begin{aligned}
\mathcal E^{(\tau)}_{\omega,c,\gamma}
&=\exp\!\left[\tau\left(\mathcal D_\gamma-i(\omega-c)[G,\cdot]\right)\right],\\
\mathcal D_\gamma(X)
&=\sum_j\gamma_j\left(F_jXF_j-\tfrac12\{F_j^2,X\}\right).
\end{aligned}
\tag{C1}
$$

The unknown frequency belongs to the fixed band $[-W,W]$, where $W>0$. The rates are fixed throughout the experiment, may be unknown, and obey known bounds $0\le\gamma_j\le\Gamma_j<\infty$. A known additional Hamiltonian drift is assumed physically canceled; an unknown drift is not part of this model.

Define the known envelope algebra

$$
\mathcal A_F=C^*(I,F_1,\ldots,F_m).
\tag{C2}
$$

**Constructive theorem.** If $G\notin\mathcal A_F$, there exist an encoding, a decoder and a sufficiently small $\tau>0$, all chosen independently of the eventual budget $T$ and of the actual rates, such that

$$
\sup_{\omega\in[-W,W],\;0\le\gamma_j\le\Gamma_j}
\mathbb E_{\omega,\gamma}(\widehat\omega-\omega)^2
\le \frac{C}{T^2}
\tag{C3}
$$

for every $T>0$, with a fixed constant $C$. The construction uses one active sensor, a persistent noiseless encoding ancilla of dimension at most $d$, ideal operations at cell boundaries, and a classical calibrated field $-cG$ acting physically throughout each cell. The field is constant within each prepared batch and always satisfies $|c|\le W$. The environment and its noise record are inaccessible.

The ancillary dimension bound concerns the coherent encoding memory. A fixed finite recovery/reset apparatus may also be used at the boundaries; its size does not grow with $T$. The statement charges sensing time. It assumes ideal instantaneous boundary operations, noiseless memory and exactly calibrated compensation, rather than a fault-tolerant implementation of those resources.

For known actual jumps $L_j$, take $F_j=L_j$ and $\gamma_j=\Gamma_j=1$. Then $\mathcal A_F$ is the actual algebra $\mathcal A=C^*(I,L_1,\ldots,L_m)$. Combining this theorem with the converse gives an equivalence for the **existence of a sufficiently small, once-chosen fixed cadence**. It does not assert attainability for every supplied cadence and prior band. When some unknown rates can vanish, the actual algebra can shrink; the envelope condition here is a uniform sufficient condition, not a necessary condition for each such realization.

## 2. An explicit code and a rate-independent decoder

Use the Hilbert–Schmidt inner product $\langle X,Y\rangle=\operatorname{Tr}(X^\dagger Y)$ and its orthogonal projection $\Pi_{\mathcal A_F}$. Set

$$
\begin{aligned}
Q&=G-\Pi_{\mathcal A_F}G=Q_+-Q_-,\\
s&=\operatorname{Tr}Q_+=\operatorname{Tr}Q_->0,\\
\rho_0&=Q_+/s,\qquad \rho_1=Q_-/s.
\end{aligned}
\tag{C4}
$$

The projection preserves adjoints because the algebra is adjoint closed. Thus $Q$ is Hermitian. The inclusion of $I$ in the algebra makes $Q$ traceless, and $G\notin\mathcal A_F$ makes it nonzero. Its positive and negative parts have orthogonal supports and equal positive trace.

Purify $\rho_0$ and $\rho_1$ using disjoint ancilla supports. Their purifications define orthonormal codewords $|0_L\rangle$ and $|1_L\rangle$, and an isometry $V:\mathbb C^2\to\mathbb C^d\otimes\mathcal H_A$. The required ancilla dimension is

$$
\dim\mathcal H_A
=\operatorname{rank}Q_++\operatorname{rank}Q_-
\le d.
\tag{C5}
$$

Disjoint ancilla supports imply $\langle0_L|(X\otimes I_A)|1_L\rangle=0$ for **every** sensor operator $X$. For $A\in\mathcal A_F$, the difference of diagonal matrix elements is $\operatorname{Tr}(AQ)/s=0$. Consequently

$$
V^\dagger(A\otimes I_A)V=\alpha_A I_2
\qquad(A\in\mathcal A_F).
\tag{C6}
$$

Since $A^\dagger B\in\mathcal A_F$ whenever $A,B\in\mathcal A_F$, this is the Knill–Laflamme condition for the entire error space $\mathcal A_F$.

For completeness, a single decoder can be constructed directly. Choose a basis $E_1,\ldots,E_a$ of the algebra and form its positive semidefinite scalar Gram matrix

$$
V^\dagger(E_\alpha^\dagger E_\beta\otimes I_A)V
=C_{\alpha\beta}I_2.
\tag{C7}
$$

Let $U^\dagger C U=\operatorname{diag}(\lambda_a)$ and define $D_a=\sum_\alpha E_\alpha U_{\alpha a}$. For each $\lambda_a>0$, set

$$
W_a=\frac{(D_a\otimes I_A)V}{\sqrt{\lambda_a}}.
\tag{C8}
$$

Then $W_a^\dagger W_b=\delta_{ab}I_2$. Zero-eigenvalue combinations satisfy $(D_a\otimes I_A)V=0$ and need no recovery branch. Let $P_{\rm err}=\sum_{\lambda_a>0}W_aW_a^\dagger$. A decoder from the joint physical space to the logical qubit is

$$
\mathcal R(\sigma)
=\sum_{\lambda_a>0}W_a^\dagger\sigma W_a
+\operatorname{Tr}[(I-P_{\rm err})\sigma]\,|0\rangle\langle0|.
\tag{C9}
$$

This map is completely positive and trace preserving. The first term reverses the mutually orthogonal error isometries; the second gives a trace-preserving extension on their unused complement.

To verify the universal correction property, expand any Kraus operator $K_\mu\in\mathcal A_F$ in the $D_a$ basis. On the code,

$$
(K_\mu\otimes I_A)V
=\sum_{\lambda_a>0}k_{\mu a}\sqrt{\lambda_a}\,W_a.
\tag{C10}
$$

The decoder maps its contribution to $\sum_a|k_{\mu a}|^2\lambda_a\rho$. If the physical channel is trace preserving, summing (C10) over its Kraus operators gives $\sum_{\mu,a}|k_{\mu a}|^2\lambda_a=1$. Therefore

$$
\mathcal R\circ(\mathcal N\otimes\mathrm{id}_A)\circ\mathcal V
=\mathrm{id}_2,
\qquad \mathcal V(\rho)=V\rho V^\dagger,
\tag{C11}
$$

for every channel with Kraus operators in $\mathcal A_F$. The basis, Gram matrix and decoder depend only on the code and algebra. They do not depend on the rates, their Kraus weights, $\tau$, the field value, or $T$.

At a boundary one applies this decoder and re-encodes with $V$. Equivalently one implements the corresponding recovery into the code space. Both descriptions induce the same logical cell channel.

## 3. Exact correction at the compensated point

Write $L_j=\sqrt{\gamma_j}F_j$ and $\delta=\omega-c$. Hermitian Lindblad noise admits a parameter-independent Brownian-unitary representation. In Itô form,

$$
dU_\delta(t)
=\left(-i\delta G-\tfrac12\sum_jL_j^2\right)U_\delta(t)\,dt
-i\sum_jL_jU_\delta(t)\,dW_j(t),
\qquad U_\delta(0)=I.
\tag{C12}
$$

Averaging $U_\delta\rho U_\delta^\dagger$ gives precisely (C1). At $\delta=0$, every path unitary belongs to $\mathcal A_F$: finite products generated by the $L_j$ lie in the algebra, and its finite-dimensional closure contains their stochastic limits. Hence (C11) corrects the null cell **exactly**, for every $\tau>0$.

Define

$$
\Lambda_\delta
=\mathcal R\circ
\bigl(\mathcal E^{(\tau)}_{\omega,c,\gamma}\otimes\mathrm{id}_A\bigr)
\circ\mathcal V.
\tag{C13}
$$

Then $\Lambda_0=\mathrm{id}_2$. The Brownian paths are a mathematical representation of the channel, not an observed record available to the estimator. The physical within-cell operation remains exactly the joint channel in (C13), without ancillary control during the cell.

## 4. The exact finite-cell signal tangent

For a fixed Brownian path, the relative unitary $A_\delta(t)=U_0(t)^\dagger U_\delta(t)$ obeys the ordinary differential equation

$$
\frac{dA_\delta}{dt}
=-i\delta\,U_0(t)^\dagger G U_0(t)A_\delta(t).
\tag{C14}
$$

The stochastic terms cancel. Differentiating at zero gives

$$
iU_0(\tau)^\dagger
\left.\partial_\delta U_\delta(\tau)\right|_0
=\int_0^\tau U_0(t)^\dagger G U_0(t)\,dt.
\tag{C15}
$$

The pathwise derivative has norm at most $\tau\|G\|$, so averaging and differentiation are justified by this uniform bound. If $K_\mu(\delta)$ denotes the path Kraus family, with sums interpreted as integrals when necessary, then

$$
\begin{aligned}
B_\tau
&=i\sum_\mu K_\mu(0)^\dagger K_\mu'(0)\\
&=\int_0^\tau e^{t\mathcal D_\gamma^\dagger}(G)\,dt.
\end{aligned}
\tag{C16}
$$

In particular $B_\tau=\tau G$ when the noise vanishes, fixing the sign convention.

Let $R_\ell$ be Kraus operators of the fixed decoder. Exact correction gives

$$
R_\ell(K_\mu(0)\otimes I_A)V=\lambda_{\ell\mu}I_2.
\tag{C17}
$$

Differentiating the corrected channel, its left-acting first-order coefficient is

$$
\begin{aligned}
A_L
&=\sum_{\ell,\mu}\lambda_{\ell\mu}^*
R_\ell(K_\mu'(0)\otimes I_A)V\\
&=V^\dagger\sum_{\ell,\mu}
(K_\mu(0)^\dagger\otimes I_A)R_\ell^\dagger R_\ell
(K_\mu'(0)\otimes I_A)V\\
&=V^\dagger\sum_\mu
(K_\mu(0)^\dagger K_\mu'(0)\otimes I_A)V.
\end{aligned}
\tag{C18}
$$

The final equality uses trace preservation of the full decoder, including its extension off the correctable space. Thus

$$
\Lambda_0'(\rho)=-i[H_L,\rho],
\qquad H_L=V^\dagger(B_\tau\otimes I_A)V.
\tag{C19}
$$

There is no parameter-dependent recovery in this calculation. Disjoint ancilla supports make $H_L$ diagonal in the logical basis. Its eigenvalue difference, in logical-zero minus logical-one order, is

$$
b_\tau=\frac{\operatorname{Tr}(QB_\tau)}s.
\tag{C20}
$$

## 5. Positivity of the tangent and uniform rate bounds

For Hermitian jumps,

$$
\mathcal D_\gamma(X)
=-\tfrac12\sum_j[L_j,[L_j,X]],
\qquad
\langle X,\mathcal D_\gamma X\rangle
=-\tfrac12\sum_j\|[L_j,X]\|_{\rm HS}^2.
\tag{C21}
$$

Therefore $\mathcal D_\gamma=\mathcal D_\gamma^\dagger$ is self-adjoint and negative semidefinite on operator Hilbert space. It preserves $\mathcal A_F$; self-adjointness then makes $\mathcal A_F^\perp$ invariant as well. Define

$$
F_\tau(\mathcal D_\gamma)=\int_0^\tau e^{t\mathcal D_\gamma}\,dt.
\tag{C22}
$$

Each of its eigenvalues is $\int_0^\tau e^{t\lambda}dt>0$ for an eigenvalue $\lambda\le0$ of the dissipator. Orthogonality of $Q$ to the algebra now yields

$$
b_\tau
=\frac{\langle Q,F_\tau(\mathcal D_\gamma)Q\rangle}{s}
>0.
\tag{C23}
$$

Thus the physical tangent cannot vanish on this fixed code at any finite positive cadence. This local fact alone is not a global estimation theorem; the localization construction below also controls nonlinear response and phase aliases.

Set

$$
\begin{aligned}
q&=\frac{\|Q\|_{\rm HS}^2}{s}>0,
&g&=\|G\|,\\
M&=2\sum_j\Gamma_j\|F_j\|^2,
&a_{\min}(\tau)&=
\begin{cases}
(1-e^{-M\tau})/M,&M>0,\\
\tau,&M=0.
\end{cases}
\end{aligned}
\tag{C24}
$$

The spectrum of every allowed $\mathcal D_\gamma$ lies in $[-M,0]$, because the Hilbert–Schmidt operator norm of a commutator with $F_j$ is at most $2\|F_j\|$. Therefore

$$
q\,a_{\min}(\tau)\le b_\tau\le q\tau.
\tag{C25}
$$

In particular, $M\tau\le1$ implies $q\tau/2\le b_\tau\le q\tau$. These bounds require only the rate bounds, not the actual values. Although the true logical slope is unknown, its sign and a positive lower bound are known.

## 6. A uniform quadratic cell remainder

Let $\mathcal K=-i[G,\cdot]$, for which $\|\mathcal K\|_\diamond\le2g$. Iterating the Duhamel identity once gives

$$
\|\Lambda_\delta-\mathrm{id}_2-\delta\Lambda_0'\|_\diamond
\le\tfrac12\delta^2\tau^2\|\mathcal K\|_\diamond^2
\le2\delta^2\tau^2g^2.
\tag{C26}
$$

All intervening semigroups are completely positive and trace preserving for real $\delta$, so their diamond norms are one. Encoding and decoding are also channels. This argument gives a bound for every real $\delta$; it is not a formal truncation with an unspecified remainder.

The unitary logical channel $\mathcal U_\delta=\operatorname{Ad}(e^{-i\delta H_L})$ has the same first derivative. Since $\|H_L\|\le\tau g$, its second-order remainder has the same upper bound. Hence

$$
\begin{aligned}
\|\Lambda_\delta-\mathcal U_\delta\|_\diamond
&\le4\delta^2\tau^2g^2,\\
\|\Lambda_\delta^n-\mathcal U_\delta^n\|_\diamond
&\le4n\delta^2\tau^2g^2
\qquad(n\ge1).
\end{aligned}
\tag{C27}
$$

The second inequality is a telescoping sum of channel products. The corrected channel need not be an exact dephasing channel away from $\delta=0$; (C27) is enough.

Prepare $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$ and measure the same logical Pauli $Y$ after $n$ cells. With the usual $Y$ convention, its ideal mean is $\sin(nb_\tau\delta)$. The actual mean $\mu_n(\delta)$ satisfies

$$
|\mu_n(\delta)-\sin(nb_\tau\delta)|
\le4n\delta^2\tau^2g^2.
\tag{C28}
$$

## 7. A sign test with one fixed cadence

Fix

$$
\beta=\tfrac14,\qquad r=\tfrac34,
\qquad s_0=\sin(\beta/8)>0.
\tag{C29}
$$

Choose $\tau>0$ once so that

$$
M\tau\le1,\qquad
q\tau W\le\beta/2,\qquad
\frac{4\beta\tau g^2 W}{q}\le s_0/2.
\tag{C30}
$$

Every fixed finite model and prior band with $q>0$ admits such a choice. These conditions do not depend on $T$ or on the actual rates.

Suppose the current interval is $I=[c-w,c+w]$, where $w\le W$. Hold the physical field at $c$ and use

$$
n(w)=\left\lfloor\frac{\beta}{q\tau w}\right\rfloor.
\tag{C31}
$$

The quantity inside the floor is at least two, so

$$
\frac{\beta}{2q\tau w}\le n(w)\le\frac{\beta}{q\tau w}.
\tag{C32}
$$

For a true point in either outer quarter, $w/2\le|\delta|\le w$, (C25) and (C32) imply

$$
\beta/8\le|n(w)b_\tau\delta|\le\beta.
\tag{C33}
$$

The ideal mean has the sign of $\delta$ and magnitude at least $s_0$. Its error in (C28) is at most $4\beta\tau g^2w/q\le s_0/2$. Thus

$$
\operatorname{sgn}(\delta)\,\mu_{n(w)}(\delta)\ge s_0/2
\qquad(w/2\le|\delta|\le w).
\tag{C34}
$$

This conclusion is uniform over the rate family and the entire relevant part of the interval. The measurement does not require knowledge of $b_\tau$.

Repeat the prepared batch independently $m$ times and let $\overline Y$ be the mean of the $\pm1$ readouts. If $\overline Y\ge0$, retain $[c-w/2,c+w]$; otherwise retain $[c-w,c+w/2]$. A zero mean can use either convention. Both intervals contain the central overlap $[c-w/2,c+w/2]$ and have half-width $rw$.

Excluding a true point outside the overlap requires a wrong sign. Hoeffding's one-sided inequality and (C34) give

$$
\Pr\{\text{truth excluded}\mid\text{truth in current interval}}
\le e^{-ms_0^2/8}.
\tag{C35}
$$

Every returned interval is nested in its predecessor on every history, including failed histories. Its center remains inside $[-W,W]$, which establishes the stated field-amplitude bound.

## 8. Global risk without an uncharged accurate prior

For a target of $K$ refinement stages, let $w_j=Wr^j$. At stage $j$ use $n_j=n(w_{j-1})$ and

$$
\begin{aligned}
C_{\rm rep}&=\frac{24\log(1/r)}{s_0^2},\\
m_j&=\left\lceil C_{\rm rep}(K-j+1)\right\rceil.
\end{aligned}
\tag{C36}
$$

Then the conditional probability of exclusion at stage $j$ is at most $p_j=r^{3(K-j+1)}$. Return the center of the last interval.

If there is no exclusion, the error magnitude is at most $w_K$. If the first exclusion is at stage $j$, both the truth and the final estimate belong to the preceding interval: the truth had not yet been excluded, and all later intervals remain nested. Their distance is therefore at most $2w_{j-1}$. No behavior after the first failure needs to be declared successful. It follows that

$$
\begin{aligned}
\sup_{\omega,\gamma}\mathbb E(\widehat\omega-\omega)^2
&\le w_K^2+4\sum_{j=1}^K w_{j-1}^2r^{3(K-j+1)}\\
&=w_K^2\left(1+4\sum_{k=1}^Kr^k\right)\\
&\le13w_K^2.
\end{aligned}
\tag{C37}
$$

The early stages are repeated more often because their first errors would be more costly. This weighting prevents a fixed global failure probability from dominating the desired risk.

## 9. Exact budget choice and resource accounting

The deterministic sensing time used by the $K$-stage protocol is

$$
T_K=\tau\sum_{j=1}^Km_jn_j.
\tag{C38}
$$

All trials, their noisy cells, and their failures appear in this sum. Since $m_j\le(C_{\rm rep}+1)(K-j+1)$, (C32) gives

$$
\begin{aligned}
T_K
&\le\frac{\beta(C_{\rm rep}+1)}q
\sum_{j=1}^K\frac{K-j+1}{w_{j-1}}\\
&\le\frac{B}{w_K},\\
B&=\frac{\beta(C_{\rm rep}+1)}q\frac{r}{(1-r)^2}.
\end{aligned}
\tag{C39}
$$

The last step uses $w_{j-1}=w_Kr^{-(K-j+1)}$ and $\sum_{k\ge1}kr^k=r/(1-r)^2$.

For a given hard budget $T$, choose

$$
K(T)=
\begin{cases}
0,&T<B/W,\\[2pt]
\left\lfloor\dfrac{\log(WT/B)}{\log(1/r)}\right\rfloor,
&T\ge B/W.
\end{cases}
\tag{C40}
$$

For $K=0$, return the initial midpoint and use no sensing time. In the second branch, $B/T\le w_K<B/(rT)$, so (C39) ensures $T_K\le T$ on every history. Combining with (C37) gives $13B^2/(r^2T^2)$. For the first branch, $W^2\le B^2/T^2$, which supplies the same all-budget upper bound after enlarging the constant if necessary.

The quantum code, decoder, ancilla dimension, preparation and final measurement remain fixed. The number of independent prepared/read batches is at most

$$
\sum_{j=1}^Km_j
\le(C_{\rm rep}+1)\frac{K(K+1)}2=O((\log T)^2).
\tag{C41}
$$

There are at most $K=O(\log T)$ field settings and at most $T/\tau$ recovery cells. The compensation's digital specification can become more accurate with $T$; the present theorem does not assume a fixed finite set of physical field values. The grid theorem addresses that additional restriction in its stated qubit setting.

## 10. Matching total-time lower bound

Let $\nu=\lambda_{\max}(G)-\lambda_{\min}(G)>0$. A scalar shift of $G$ changes no channel and gives $\|{-i[G,\cdot]}\|_\diamond\le\nu$. Duhamel's formula therefore bounds any fixed-field cell by

$$
\|\mathcal E^{(\tau)}_{\omega,c,\gamma}
-\mathcal E^{(\tau)}_{\omega',c,\gamma}\|_\diamond
\le\tau\nu|\omega-\omega'|.
\tag{C42}
$$

Treat the complete classical history and quantum memory as the state of an adaptive protocol. Boundary instruments and the rule assigning $c$ from that history are parameter-independent maps. Replacing the cells one at a time in the two experiments yields the hybrid bound

$$
\|\rho_\omega^{\rm out}-\rho_{\omega'}^{\rm out}\|_1
\le T\nu|\omega-\omega'|.
\tag{C43}
$$

This bound includes ancillary systems, all retained outcomes and classical adaptation. Stopping before the budget is spent can be padded with parameter-independent idle operations.

Choose two frequencies separated by $\varepsilon=\min\{2W,1/(\nu T)\}$ inside the prior band. Their trace distance is at most $1/2$. Any estimate induces a nearest-point binary test, whose error forces a squared estimation error of at least $\varepsilon^2/4$. The optimal average testing error is at least $(1-1/2)/2=1/4$. Thus the minimax risk is bounded below by

$$
\frac{\varepsilon^2}{16}
=\min\!\left\{\frac{W^2}{4},\frac1{16\nu^2T^2}\right\}.
\tag{C44}
$$

It applies at any fixed allowed rate realization and hence also to the nuisance-rate minimax problem. Together with (C3), it establishes the asymptotic $\Theta(T^{-2})$ risk of the permitted model.

## 11. Attribution and boundaries

Algebraic error correction, channel Hamiltonian tangents, total-generator discrimination bounds, and weighted global localization are established ingredients. Their roles and the closest finite-rate sensing results are documented in [the related-work comparison](../references/RELATED_WORK.md) and [source list](../references/SOURCES.md). The finite-cadence statement here depends on the exact simultaneous semigroup, the positive integrated tangent, and the explicitly paid global protocol; none of those ingredients should be replaced by an uncharged local-QFI claim.

The positive theorem does not cover non-Hermitian jumps, unknown noise directions, uncontrolled Hamiltonian drift, faulty boundary operations, noisy memory, fixed calibration bias, access to a noise trajectory, or compensation that is applied only as a boundary rotation. Nor does it claim that an arbitrary supplied cadence avoids aliases on an arbitrary prior band. The [converse](converse_proof.md) concerns the actual generated algebra and states an $\Omega(T^{-1})$ obstruction, with SQL attainment requiring an additional identifiability argument.
