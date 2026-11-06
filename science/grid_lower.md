# The unavoidable cost of a discrete physical field

This page proves the lower bound matching the [calibrated-grid construction](grid_upper.md).
It bounds the unrecovered physical channel, so changing the recovery code,
retaining more syndrome data, dithering between grid values at cell boundaries,
or using larger noiseless memory cannot evade it. The information-theoretic
ingredients are the channel RLD formula and chain rule of
[Katariya and Wilde](https://arxiv.org/abs/2004.10708); their attribution and
the other prior ingredients are discussed in [related work](../references/RELATED_WORK.md).

## 1. Model and uniform statement

One sensor evolves during a cell of duration $\tau>0$ according to

$$
\frac{d\rho}{dt}=-i[(\omega-c)Z/2,\rho]
+\gamma(X\rho X-\rho).
\tag{L1}
$$

The rate is strictly positive. For uniform constants, fix
$0<\gamma_-\le\gamma\le\Gamma<\infty$. The signal belongs to the fixed
band $[-W,W]$, with $W>0$. During each cell the field is a classical
number in a subset of the uniform lattice

$$
\mathcal G_{\Delta,a}=a+\Delta\mathbb Z,
\qquad \Delta>0,
$$

and is held constant for the whole cell. The offset $a$ is arbitrary.
Between cells the strategy may use arbitrary parameter-independent
instruments, quantum memory, noiseless ancillas, and feedback. The noise
environment is inaccessible; no operations or field switches are permitted
inside a cell. Every history uses at most $N=\lfloor T/\tau\rfloor$ cells.

For

$$
0<\Delta\le\min\{W,4/\tau\},\qquad
T\ge\max\{\tau,1/(2W)\},
\tag{L2}
$$

every allowed protocol has minimax mean-squared error at least

$$
R(T,\Delta;\gamma)
\ge\frac{1}{32T^2}
+\frac{\tau\Delta^2}{2T(C_R+16\pi^2)},
\tag{L3}
$$

where $C_R$ is given explicitly below and depends only on the fixed
positive rate range and $\tau$. The bound is uniform in the lattice offset
and in every adaptive choice of field values. A field-amplitude bound is
unnecessary for this lower bound.

Intersecting (L2) with the small fixed-domain conditions of the upper
construction gives, for known $\gamma>0$,

$$
R(T,\Delta;\gamma)
=\Theta\!\left(T^{-2}+\frac{\tau\Delta^2}{T}\right),
\qquad 0<\Delta\le\Delta_0\le W.
\tag{L4}
$$

The upper bound also requires available grid points nearest to the
successive interval centers; a finite field range covering the band with
the requisite endpoint margin suffices. Its domain can be larger than
the common domain of the matched statement (L4). The explicit
$\Delta_0\le W$ ensures an entire lattice gap lies inside the band for
every offset, as used below.

The lower bound remains valid if the true rate is supplied to the
estimator. The matching upper bound presently uses that rate in its
classical phase processing. Thus (L4) does not by itself establish the
same upper bound for an unknown rate. The continuous-field,
unknown-bounded-rate result is proved separately in the
[constructive account](constructive_proof.md).

## 2. The full physical Choi matrix loses rank only at zero detuning

Write $\delta=\omega-c$, and let $N(t)$ be a Poisson process of rate
$\gamma$. Its trajectory unitary is

$$
U_{\mathrm{path}}=X^{N(\tau)}e^{-i\delta S Z/2},\qquad
S=\int_0^\tau(-1)^{N(t)}\,dt.
\tag{L5}
$$

The jump probabilities are independent of $\delta$, because the jump
operator is $\sqrt\gamma X$. Equation (L5) is a representation of the
unmonitored channel and does not make the trajectory record available
to the estimator.

Use the normalized, output-first Choi matrix

$$
J_\delta=(\mathcal E_\delta^{(\tau)}\otimes\mathrm{id})
(|\Phi_2\rangle\langle\Phi_2|),\qquad
|\Phi_2\rangle=(|00\rangle+|11\rangle)/\sqrt2.
$$

For a Pauli operator $P$, abbreviate the normalized vector
$|P\rangle\!\rangle/\sqrt2$ as $|P)$; these four vectors are orthonormal.
An even-parity path contributes the unit vector

$$
\cos(\delta S/2)|I)-i\sin(\delta S/2)|Z),
$$

and an odd-parity path contributes

$$
\cos(\delta S/2)|X)-\sin(\delta S/2)|Y).
$$

The latter sign follows from $XZ=-iY$. Therefore $J_\delta$ is a direct
sum of a block on the $I,Z$ subspace and a block on the $X,Y$ subspace.
All other trajectory contributions are positive, so lower-bounding each
block using only selected jump counts is valid.

Exactly one jump gives the unnormalized density of $S$

$$
p_1(s)=\frac{\gamma e^{-\gamma\tau}}2,
\qquad -\tau\le s\le\tau.
\tag{L6}
$$

For exactly two jumps at $t_1<t_2$, one has
$S=\tau-2(t_2-t_1)$. Integrating over $t_1$ and using the Jacobian of this
change of variables gives

$$
p_2(s)=\frac{\gamma^2e^{-\gamma\tau}}4(\tau+s),
\qquad -\tau\le s\le\tau.
\tag{L7}
$$

On the common interval $[-\tau/2,\tau/2]$, both densities are at least

$$
\kappa_\gamma=e^{-\gamma\tau}
\min\!\left\{\frac\gamma2,\frac{\gamma^2\tau}8\right\}.
$$

The integral of the projector onto either trigonometric vector over
this symmetric interval has eigenvalues

$$
\frac\tau2\pm\frac{\sin(\delta\tau/2)}\delta,
$$

with its removable value at $\delta=0$ understood by continuity.
Consequently

$$
\lambda_{\min}(J_\delta)
\ge\frac{\kappa_\gamma\tau}{2}
\left[1-\left|\operatorname{sinc}(\delta\tau/2)\right|\right],
\qquad \operatorname{sinc}x=\frac{\sin x}{x}.
\tag{L8}
$$

The bracket is strictly positive whenever $\delta\ne0$, including large
detunings. Thus the **unrecovered physical channel** has full Choi rank
at every nonzero residual frequency. At zero detuning it has exactly
rank two: the positive even and odd Poisson probabilities multiply
$|I)(I|$ and $|X)(X|$.

The elementary global bound

$$
1-|\operatorname{sinc}x|\ge\frac18\min\{x^2,1\}
\tag{L9}
$$

can be checked as follows. For $|x|\le1$, the alternating sine bound gives
$1-\operatorname{sinc}x\ge19x^2/120$. On $[1,\pi]$, the positive function
$\sin x/x$ decreases and is at most $\sin1<7/8$. For $|x|\ge\pi$,
$|\operatorname{sinc}x|\le1/\pi<7/8$. Evenness covers negative $x$.
Using also
$\min\{(y/2)^2,1\}\ge\frac14\min\{y^2,1\}$ in (L8) yields

$$
\lambda_{\min}(J_\delta)
\ge C_0\min\{(\delta\tau)^2,1\},
\qquad
C_0=\frac{e^{-\Gamma\tau}}{64}
\min\!\left\{\frac{\gamma_-\tau}{2},
\frac{(\gamma_-\tau)^2}{8}\right\}>0.
\tag{L10}
$$

For context, this quadratic rank opening has a matching order upper
bound. The $Z$ diagonal entry in the even block is at most
$\mathbb E\sin^2(\delta S/2)\le(\delta\tau)^2/4$, and a trace-one
four-dimensional matrix has minimum eigenvalue at most $1/4$. Hence

$$
\lambda_{\min}(J_\delta)
\le\frac14\min\{(\delta\tau)^2,1\}.
\tag{L11}
$$

The constants in (L10) are intentionally loose; no sharp limit in
$\gamma\tau\to0$ is claimed.

## 3. Uniform information bound away from every lattice point

A normalized trajectory Choi vector has a phase generator of operator
norm at most $|S|/2$. Its rank-one projector derivative therefore has
trace norm at most $|S|\le\tau$. Convexity and the parameter-independent
path law give

$$
\|\dot J_\delta\|_1\le\tau,\qquad
\operatorname{Tr}(\dot J_\delta^2)\le\tau^2.
\tag{L12}
$$

For $\delta\ne0$, let $\Gamma_\delta=2J_\delta$. The inherited channel
RLD formula and positivity give

$$
\begin{aligned}
\widehat I(\mathcal E_\delta^{(\tau)})
&=\left\|\operatorname{Tr}_{\mathrm{out}}
[\dot\Gamma_\delta\Gamma_\delta^{-1}\dot\Gamma_\delta]
\right\|_\infty\\
&\le2\operatorname{Tr}(\dot J_\delta J_\delta^{-1}\dot J_\delta)\\
&\le\frac{2\tau^2}{C_0\min\{(\delta\tau)^2,1\}}.
\end{aligned}
\tag{L13}
$$

For every lattice offset and $\Delta\le W$, an entire interval between
two consecutive lattice points lies inside $[-W,W]$. For example, take
the first lattice point at or to the right of $-W$. It lies below
$-W+\Delta$, so the next point lies below or at $-W+2\Delta\le W$.
Let $m$ be the midpoint of such a gap, and restrict the parameter to

$$
\mathcal I_\Delta=[m-\Delta/4,m+\Delta/4].
$$

Every point in $\mathcal I_\Delta$ is at distance at least $\Delta/4$
from **every** underlying lattice point, and hence from every permitted
field value even if the available grid is only a subset. For
$\tau\Delta\le4$, (L13) therefore gives

$$
\sup_{\omega\in\mathcal I_\Delta}
\sup_{c\in\mathcal G_{\Delta,a}}
\widehat I(\mathcal E_{\omega-c}^{(\tau)})
\le\frac{C_R}{\Delta^2},\qquad C_R=\frac{32}{C_0}.
\tag{L14}
$$

The supremum includes arbitrarily large positive or negative grid
values. Large detuning does not offer an escape because (L10) remains
uniform there.

The [adaptive-information argument](converse_proof.md) applies to
(L14): retain the full classical history and conditional quantum memory,
use the channel RLD chain rule in every fixed history branch, and then
use data processing for the next boundary operation. The distribution
of histories can depend on $\omega$; its Fisher information is retained
in the classical–quantum state rather than omitted. The chosen number
$c(h)$ is constant when differentiating a fixed history branch. The
final readout distribution consequently satisfies

$$
I_{\mathrm{data}}(\omega)
\le\frac{NC_R}{\Delta^2},\qquad
\omega\in\mathcal I_\Delta.
\tag{L15}
$$

This covers alternating grid values from one cell to the next, adaptive
field dithering, all boundary recovery choices and ancillary systems of
any finite dimension. Hard-cap stopping is padded by discarded dummy
uses; failed postselection outcomes remain part of the data. There is
no special role for the parity decoder of the upper construction.

## 4. A biased-estimator minimax bound

On $\mathcal I_\Delta$, take the prior

$$
\pi_\Delta(\omega)=\frac4\Delta
\cos^2\!\left(\frac{2\pi(\omega-m)}\Delta\right),
\qquad |\omega-m|\le\Delta/4.
$$

It integrates to one, vanishes at its endpoints, and has Fisher
information

$$
I(\pi_\Delta)=\frac{16\pi^2}{\Delta^2}.
$$

The integration-by-parts and Cauchy–Schwarz proof in the
[general converse](converse_proof.md) gives, without an unbiasedness
condition,

$$
R(T,\Delta;\gamma)
\ge\frac{1}{\mathbb E_{\pi_\Delta}I_{\mathrm{data}}+I(\pi_\Delta)}
\ge\frac{\Delta^2}{NC_R+16\pi^2}.
\tag{L16}
$$

For $N\ge1$, the right-hand side is at least
$\Delta^2/[N(C_R+16\pi^2)]$. Since $N\le T/\tau$, this proves the
$\tau\Delta^2/T$ term.

For completeness, the usual Heisenberg lower bound applies to the
same access model independently of the noise and grid. The spectral
diameter of $Z/2$ is one, so Duhamel's formula gives

$$
\|\mathcal E_{\omega-c}^{(\tau)}-
\mathcal E_{\omega'-c}^{(\tau)}\|_\diamond
\le\tau|\omega-\omega'|.
\tag{L17}
$$

The hybrid argument for an adaptive sequence of at most $N$ cells
therefore bounds its final trace-norm difference by
$T|\omega-\omega'|$. The argument includes the memory and complete
history; at each common-history channel call it uses the same control
rule under the two hypotheses.

Choose two frequencies in the band a distance $1/T$ apart, which is
possible for $T\ge1/(2W)$. The total variation distance of any final
data distributions is at most $1/2$. Assigning an estimate to its nearer
hypothesis makes any classification error cost at least $1/(4T^2)$.
The optimal equal-prior testing error is at least $1/4$, hence

$$
R(T,\Delta;\gamma)\ge\frac{1}{16T^2}.
\tag{L18}
$$

Taking half the sum of (L18) and the consequence of (L16) proves (L3),
because the maximum of two lower bounds is at least half their sum.

## 5. Interpretation and exclusions

For a fixed positive rate and fixed cadence, (L4) makes
$\Delta=O(T^{-1/2})$ necessary and sufficient for retaining $O(T^{-2})$
global risk within the stated grid model. Thus a recovery clock may
stay fixed while the resolution of the simultaneous physical
compensation field must improve. This exponent is consistent with
quadratic residual phase noise; the converse establishes it against
every adaptive protocol allowed by the model.

Boundary dithering cannot synthesize an off-grid field inside the cell:
the unobserved jump times already create full physical Choi rank at
every nonzero detuning. A boundary counter-rotation is permitted but
does not undo that within-cell uncertainty. Faster field switching,
continuous ancillary coupling, an observed noise record, or a Hamiltonian
controlled by a coherent quantum register would change the channel
oracle and are outside the theorem.

The strict positivity of the rate is essential. At $\gamma=0$ the
physical channel is unitary, the Choi-rank bound fails, and a digital
compensation grid need not impose the $\Delta^2/T$ penalty. Likewise,
these estimates do not incorporate unknown control bias, faulty
recoveries or a noisy ancillary memory.

The [numerical verification](../verification/README.md) checks the
physical Choi eigenvalues and derivative bounds at finite parameter
values. Those checks corroborate the formulas; the positive trajectory
integrals and the information argument prove the universal statement.
