# A four-level sensor separates fast correction from every fixed clock

The full finite-time noise algebra can contain a signal that lies outside
the infinitesimal Lindblad span. This page gives an explicit example and
compares **global mean-squared error under a hard sensing-time budget** in
the two control regimes. A local Fisher-information statement alone is
not used to infer the fast-clock global upper bound.

The fast-control HNLS criterion is inherited from
[Zhou, Zhang, Preskill and Jiang (2018)](https://doi.org/10.1038/s41467-017-02510-3).
The fixed-clock lower bound uses the [physical-channel converse](converse_proof.md)
and the channel RLD tools attributed there. See
[related work](../references/RELATED_WORK.md) for the scope of the comparison.

## 1. The signal passes HNLS but belongs to the full algebra

In a four-dimensional sensor, take

$$
L=\operatorname{diag}(-3,-1,1,3),\qquad
G=L^3=\operatorname{diag}(-27,-1,1,27).
\tag{F1}
$$

The physical generator at residual frequency $\delta=\omega-c$ is

$$
\mathcal L_\delta(\rho)=-i\delta[G,\rho]
+L\rho L-\frac12\{L^2,\rho\}.
$$

For one Hermitian jump, the real Hermitian infinitesimal Lindblad span is

$$
\mathcal S=\operatorname{span}_{\mathbb R}\{I,L,L^2\}.
$$

The signal $G$ is outside $\mathcal S$. Otherwise a monic cubic minus a
polynomial of degree at most two would vanish at all four distinct
eigenvalues of $L$, which is impossible. On the other hand, polynomial
interpolation at those four eigenvalues generates every diagonal matrix.
Thus $\mathcal A=C^*(I,L)$ is the full diagonal algebra and
$G\in\mathcal A$. The HNLS condition and the fixed-cadence criterion
therefore disagree for this explicit physical model.

Define the encoding isometry $V$ by

$$
V|0\rangle=\frac{\sqrt3}{2}|2\rangle+\frac12|4\rangle,
\qquad
V|1\rangle=\frac12|1\rangle+\frac{\sqrt3}{2}|3\rangle.
\tag{F2}
$$

The supports of these two codewords are disjoint in the eigenbasis of
$L$. Their moments are:

| Operator | Logical zero expectation | Logical one expectation |
|---|---:|---:|
| $I$ | $1$ | $1$ |
| $L$ | $0$ | $0$ |
| $L^2$ | $3$ | $3$ |
| $L^3=G$ | $6$ | $-6$ |

All off-diagonal code matrix elements of these operators vanish.
Consequently

$$
V^\dagger LV=0,\qquad
V^\dagger L^2V=3I_2,\qquad
V^\dagger GV=6Z.
\tag{F3}
$$

The first two identities give the Knill–Laflamme conditions for the
leading error space spanned by $I,L$. The last identity retains a
nontrivial logical Hamiltonian. No noiseless encoding ancilla is needed
for this code; a fixed reset apparatus may implement its boundary
recovery.

## 2. An explicit recovery and a finite-step approximation

Let $P=VV^\dagger$. The two subspaces spanned by $V$ and $LV/\sqrt3$
are orthogonal and each has dimension two, so

$$
P+\frac13LPL=I_4.
$$

The two Kraus operators

$$
R_0=V^\dagger,\qquad R_1=\frac1{\sqrt3}V^\dagger L
\tag{F4}
$$

therefore define a trace-preserving decoder
$\mathcal R(\sigma)=\sum_{a=0}^1R_a\sigma R_a^\dagger$ from the physical
sensor to the logical qubit. Re-encoding with $V$ prepares the next cell.
For a cell of length $h$, write the corrected logical channel as

$$
\Lambda_{\delta,h}=\mathcal R\circ e^{h\mathcal L_\delta}\circ\mathcal V,
\qquad \mathcal V(\rho)=V\rho V^\dagger.
$$

At $h=0$ it is the identity. The dissipative first derivative vanishes:
the recovered jump term is $3\rho$ and the two recovered anticommutator
terms sum to $-3\rho$. In the Hamiltonian derivative the $R_1$ term
vanishes because $R_1V=0$, leaving

$$
\left.\partial_h\Lambda_{\delta,h}\right|_{h=0}
=-i[6\delta Z,\cdot].
\tag{F5}
$$

This is a first-order correction statement. It is not an exact
finite-duration correction of the null channel: higher powers of $L$
belong to the finite-time Kraus span and fail the same code conditions.

For a valid current frequency interval of half-width $w\le W$ whose
center is the physical compensation $c$, one has $|\delta|\le W$.
On that domain,

$$
\|\mathcal L_\delta\|_\diamond\le18+54W,
\qquad
\|-i[6\delta Z,\cdot]\|_\diamond\le12W.
$$

For a channel semigroup with generator $\mathcal K$, the integral Taylor
remainder satisfies

$$
\|e^{h\mathcal K}-\mathrm{id}-h\mathcal K\|_\diamond
\le\frac{h^2}{2}\|\mathcal K\|_\diamond^2,
$$

because the semigroup factors in the second-derivative integral are
channels. Apply this before the fixed decoder and to the ideal logical
unitary, and use (F5). For

$$
\mathcal U_{\delta,h}=\operatorname{Ad}_{e^{-i6\delta hZ}},\qquad
C_W=\frac{(18+54W)^2+(12W)^2}{2},
$$

one obtains the uniform bound

$$
\|\Lambda_{\delta,h}-\mathcal U_{\delta,h}\|_\diamond
\le C_Wh^2,
\qquad |\delta|\le W.
\tag{F6}
$$

Both maps are channels, so telescoping $n$ repeated cells gives

$$
\|\Lambda_{\delta,h}^{n}-\mathcal U_{\delta,h}^{n}\|_\diamond
\le nC_Wh^2.
\tag{F7}
$$

Starting from logical $|+\rangle$ and measuring logical $Y$ after the
batch therefore gives an expectation within $nC_Wh^2$ of
$\sin(12nh\delta)$.

## 3. A global fast-clock protocol with every outcome charged

Take the fixed prior $[-W,W]$ and choose

$$
\beta=\frac14,\qquad r=\frac34,\qquad
s_0=\sin(\beta/4)>0,
\qquad
A=\frac{24\log(1/r)}{s_0^2}.
\tag{F8}
$$

For a chosen number of stages $K\ge1$, set

$$
w_j=Wr^j,\qquad
h_K=\min\!\left\{\frac{\beta}{24W},
\frac{6s_0w_K}{\beta C_W}\right\}.
\tag{F9}
$$

This cadence is constant during the whole run, but it depends on the
intended horizon through $K$. That is the additional resource in this
fast-clock comparison.

At stage $j$, the current interval is
$I_{j-1}=[c_j-w_{j-1},c_j+w_{j-1}]$. Hold the field at $c_j$ for each
batch, and choose the deterministic numbers

$$
n_j=\left\lfloor\frac{\beta}{12h_Kw_{j-1}}\right\rfloor,
\qquad
m_j=\left\lceil A(K-j+1)\right\rceil.
\tag{F10}
$$

Repeat $m_j$ independent preparations of logical $|+\rangle$, each with
$n_j$ corrected cells and a final $Y$ measurement. If the empirical
mean is nonnegative retain

$$
I_j=[c_j-w_{j-1}/2,c_j+w_{j-1}];
$$

otherwise retain

$$
I_j=[c_j-w_{j-1},c_j+w_{j-1}/2].
$$

Either interval has half-width $w_j=rw_{j-1}$ and lies inside its parent.
Return the center of $I_K$. The procedure is defined on every history,
and every field remains in the original band. It uses no rejection or
unpriced restart.

### 3.1 Conditional reliability of each stage

Conditional on all earlier intervals containing the true frequency,
$|\delta|\le w_{j-1}$. From the first part of (F9), the expression inside
the floor in (F10) is at least two. Hence

$$
\frac{\beta}{24h_Kw_{j-1}}
\le n_j\le\frac{\beta}{12h_Kw_{j-1}}.
\tag{F11}
$$

If $|\delta|\ge w_{j-1}/2$, the magnitude of the ideal phase lies between
$\beta/4$ and $\beta$. Its sine has the sign of $\delta$ and magnitude
at least $s_0$. The second part of (F9) and (F11) give

$$
n_jC_Wh_K^2
\le\frac{\beta C_Wh_K}{12w_{j-1}}
\le\frac{s_0w_K}{2w_{j-1}}
\le\frac{s_0}{2}.
\tag{F12}
$$

Thus the **actual** noisy measurement mean has the correct sign and
magnitude at least $s_0/2$ outside the central overlap. When
$|\delta|\le w_{j-1}/2$, both retained intervals already contain the
truth. For independent outcomes in $[-1,1]$, the one-sided Hoeffding
bound, centered on the actual mean, therefore gives conditional
exclusion probability

$$
p_j\le\exp(-m_js_0^2/8)
\le r^{3(K-j+1)}.
\tag{F13}
$$

The approximation (F6) is required only on histories before their first
failure. Later histories may have larger detuning, but no reliability
claim on them is needed: all later intervals stay inside the last good
interval, which controls their contribution to risk.

### 3.2 Global squared error, including rare failures

On complete success the squared error is at most $w_K^2$. If the first
exclusion occurs at stage $j$, all later estimates remain in
$I_{j-1}$, which did contain the truth. The error is then at most
$2w_{j-1}$. Using (F13), with $\ell=K-j+1$, gives

$$
\begin{aligned}
\sup_{\omega\in[-W,W]}
\mathbb E_\omega(\widehat\omega-\omega)^2
&\le w_K^2+4\sum_{j=1}^Kw_{j-1}^2r^{3(K-j+1)}\\
&=w_K^2\left(1+4\sum_{\ell=1}^Kr^\ell\right)\\
&\le13w_K^2.
\end{aligned}
\tag{F14}
$$

This uses conditional bounds, so no independence between adaptive
stages is assumed. It gives a global risk guarantee on a nonshrinking
prior band rather than a claim conditional on a successful preliminary
estimate.

### 3.3 Exact hard-budget choice

All repetitions, including those on failed histories, have the same
deterministic lengths. Their total sensing time is

$$
T_K=h_K\sum_{j=1}^Km_jn_j.
$$

Since $m_j\le(A+1)(K-j+1)$ and (F11) bounds $n_j$,

$$
T_K\le\frac{C_T}{w_K},\qquad
C_T=\frac{\beta(A+1)}{12}\frac{r}{(1-r)^2}.
\tag{F15}
$$

For a supplied budget $T$, choose

$$
K(T)=
\begin{cases}
0,&T<C_T/W,\\[2pt]
\left\lfloor\log_{1/r}(WT/C_T)\right\rfloor,&T\ge C_T/W.
\end{cases}
\tag{F16}
$$

At $K=0$, perform no experiment and return zero. Otherwise
$w_K\ge C_T/T$, so (F15) proves $T_K\le T$ on every history. Also
$w_K<C_T/(rT)$ in the second case. Equations (F14)–(F16), with the
constant-risk small-budget case included, therefore prove

$$
R_T^{\mathrm{fast}}\le
\frac{13C_T^2}{r^2T^2}.
\tag{F17}
$$

The constant is loose and the protocol is not optimized for efficiency;
its purpose is an explicit globally valid scaling comparison.

### 3.4 Resources and the lower bound

For large $T$, $w_K=\Theta(T^{-1})$ and the second term in (F9) is the
minimum, so $h_K=\Theta(T^{-1})$. The final batch alone and (F11) give

$$
T_K\ge h_Kn_K
\ge\frac{\beta r}{24w_K}.
$$

Together with (F15), this gives $T_K=\Theta(T)$. Hence **this
construction** uses $\Theta(T^2)$ corrected cells, $O(\log T)$ field
settings and $O(\log^2T)$ prepare-and-measure batches. No optimal
necessity claim is made for its number of recoveries. Boundary
operations and their reset apparatus remain ideal and uncharged in the
sensing-time model; charging a fixed cost per recovery would change
the resource comparison.

The spectral diameter of $G$ is $54$. For an arbitrary allowed strategy,
the Duhamel/hybrid argument bounds its final trace-norm difference at
two frequencies by $54T|\omega-\omega'|$, even if its cell lengths vary.
Choosing two frequencies a distance $1/(54T)$ apart and using the
two-point risk argument of the [grid converse](grid_lower.md) gives

$$
R_T^{\mathrm{fast}}\ge\frac{1}{16\cdot54^2T^2}
$$

once the two frequencies fit inside the band. Thus the fast model has
global minimax risk $\Theta(T^{-2})$.

## 4. Every fixed positive clock has finite information per cell

For a fixed $\tau>0$, signal and noise commute in the physical
eigenbasis, giving the exact channel

$$
\mathcal E_\delta^{(\tau)}(|j\rangle\langle k|)
=\exp\!\left[-\frac\tau2(l_j-l_k)^2
-i\delta\tau(g_j-g_k)\right]|j\rangle\langle k|.
\tag{F18}
$$

The normalized Choi matrix lives on the four-dimensional maximally
correlated subspace spanned by $|jj\rangle$. On that subspace it is

$$
J_\delta=\frac14D_\delta R_\tau D_\delta^\dagger,
\quad
(D_\delta)_{jj}=e^{-i\delta\tau g_j},
\quad
(R_\tau)_{jk}=e^{-\tau(l_j-l_k)^2/2}.
\tag{F19}
$$

The Gaussian kernel $R_\tau$ is strictly positive definite for
$\tau>0$. Indeed, its quadratic form is the integral of
$|\sum_jv_je^{ixl_j}|^2$ against an everywhere positive Gaussian
density. If this were zero, the exponential polynomial would vanish
everywhere by continuity. Its first four derivatives at zero give an
invertible Vandermonde system at the distinct $l_j$, forcing $v=0$.
The restricted Choi eigenvalues are therefore positive and independent
of detuning.

Let $Q=\operatorname{diag}(g_1,\ldots,g_4)$. The unnormalized Choi
operator is $\Gamma_\delta=4J_\delta$. Differentiating (F19), using its
support inverse and taking the output partial trace gives the exact
channel RLD information

$$
M_\tau:=\widehat I(\mathcal E_\delta^{(\tau)})
=\tau^2\max_j
\left([Q,R_\tau]R_\tau^{-1}[Q,R_\tau]^\dagger\right)_{jj}
<\infty.
\tag{F20}
$$

For clarity, the product inside the Choi formula is
$\tau^2D_\delta[Q,R_\tau]R_\tau^{-1}[Q,R_\tau]^\dagger D_\delta^\dagger$.
The output partial trace of $|jj\rangle\langle kk|$ vanishes for
$j\ne k$, leaving precisely its diagonal; the phases cancel there.
Thus (F20) is independent of both $\omega$ and the chosen field $c$.

The adaptive cq-history chain rule now gives
$I_{\mathrm{data}}\le NM_\tau$ even for unbounded classical field
amplitudes. The global Bayesian argument consequently yields

$$
R_T^{\mathrm{fixed}}
\ge\frac{1}{\lfloor T/\tau\rfloor M_\tau+\pi^2/W^2}
=\Omega(T^{-1}).
\tag{F21}
$$

In this commuting example, compensation contributes only a known
boundary unitary:

$$
\mathcal E_{\omega-c}^{(\tau)}
=\operatorname{Ad}_{e^{ic\tau G}}\circ
\mathcal E_\omega^{(\tau)}.
\tag{F22}
$$

Unlimited analog field resolution cannot change the fixed-clock
obstruction. It arises from the physical finite-time channel, not
from a failure to choose a suitable decoder.

## 5. Exact aliases and an alias-free SQL upper bound

Every pairwise difference $g_j-g_k$ is an even integer and the
difference between the middle two levels is $2$. Since all coefficients
in (F18) are nonzero, the fundamental frequency alias period is exactly

$$
P_\tau=\frac\pi\tau.
\tag{F23}
$$

Two frequencies differing by $P_\tau$ produce identical cell channels
for every fixed field value. The full adaptive output distributions
remain identical by induction on the boundary history. If the prior
band contains such a pair, any estimator therefore has worst-case
MSE at least $P_\tau^2/4$. One must not describe (F21) as attainable
SQL scaling on every arbitrarily broad band.

Now let the parameter lie in a fixed closed interval $I$ of length

$$
0<\ell<P_\tau.
\tag{F24}
$$

Prepare $(|2\rangle+|3\rangle)/\sqrt2$ before each single cell and use
$c=0$. Measure the two Pauli quadratures in this subspace: the usual
$X$ and the signed $Y$ with matrix elements
$i|2\rangle\langle3|-i|3\rangle\langle2|$. Their exact means are

$$
\mu(\omega)=\nu\big(\cos(2\tau\omega),\sin(2\tau\omega)\big),
\qquad \nu=e^{-2\tau}>0.
\tag{F25}
$$

For $x,y\in I$, the chord length and the monotonicity of $\sin u/u$
on $(0,\pi)$ give

$$
\|\mu(x)-\mu(y)\|_2
=2\nu|\sin(\tau(x-y))|
\ge k_I|x-y|,\qquad
k_I=\frac{2\nu\sin(\tau\ell)}\ell>0.
\tag{F26}
$$

For $N\ge2$, allocate $\lfloor N/2\rfloor$ independent cells to one
quadrature and the rest to the other, with empirical mean vector
$\widehat\mu$. The two bounded-sample variances imply

$$
\mathbb E\|\widehat\mu-\mu(\omega)\|_2^2\le\frac6N.
$$

Take $\widehat\omega$ to minimize
$\|\widehat\mu-\mu(x)\|_2$ over $x\in I$, with a fixed rule for ties.
The triangle inequality and the minimizing property give
$\|\mu(\widehat\omega)-\mu(\omega)\|_2
\le2\|\widehat\mu-\mu(\omega)\|_2$. Therefore

$$
\sup_{\omega\in I}
\mathbb E_\omega(\widehat\omega-\omega)^2
\le\frac{24}{k_I^2N}=O(T^{-1}).
\tag{F27}
$$

The version of (F21) with prior half-width $\ell/2$ supplies the matching
lower bound. Thus every fixed $\tau>0$ has global risk
$\Theta(T^{-1})$ on each fixed interval satisfying (F24), while the
fast-clock model has $\Theta(T^{-2})$ risk on any fixed finite band.

## 6. What the separation establishes

At infinitesimal times, correction of the leading errors only tests the
quadratic Lindblad span. At any fixed positive time, all finite jump
words contribute to the physical Kraus span. In this example their
algebra contains $G=L^3$, although the quadratic span does not. Equations
(F17) and (F21) turn that algebraic distinction into a global estimation
separation with explicit time accounting.

The fast construction improves its cadence as the horizon grows and
uses ideal boundary operations. The fixed-clock result permits every
adaptive boundary protocol, not just the displayed code. Neither is a
claim of fault tolerance under noisy gates, optimal prefactors or an
optimal recovery-count tradeoff. The [verification scripts](../verification/README.md)
check the code moments, exact physical channel, finite-cell tangent and
the actual sign margin at finite parameter values; the analytic argument
supplies the universal bounds.
