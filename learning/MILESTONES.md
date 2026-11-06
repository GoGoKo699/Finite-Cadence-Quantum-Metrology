# Thirty milestones for finite-cadence quantum metrology

[Repository overview](../README.md) · [Nielsen–Chuang bridge](NIELSEN_CHUANG_BRIDGE.md) · [Model and exact results](../science/model.md)

This map follows one scientific question: **which resources let a noisy sensor retain inverse-square estimation error when its recovery clock has a positive, fixed interval?** The milestones connect the exact physical experiment, its constructive protocols, and the bounds that apply to every permitted protocol.

The educational anchor is Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, 10th Anniversary Edition (2010). “N&C” below always means that edition. Its relevant sections supply the language of states, operations, distinguishability and error correction. The [bridge](NIELSEN_CHUANG_BRIDGE.md) translates that language to this project. Exact finite-cell support, adaptive information bounds and global minimax accounting are supplied by the linked scientific pages and their research references; they are not attributed to the textbook.

## Structure and use

The map has **11 background/preliminary milestones and 19 narrative/innovation milestones**. The background must assemble an unusually important experimental contract: a quantum channel, an error algebra, an admissible controller, a statistical objective and a hard resource budget. Its last milestone integrates those objects into one well-defined question. The narrative then develops the positive construction and all-strategy converse before using the four-level and grid examples to separate three control resources. Its last milestones integrate scope, evidence and physical meaning.

This allocation follows the scientific dependencies rather than the order of textbook chapters. Each milestone is a common understanding target, independent of any reader's previous attempts. Together they cover the project's argument and consequences; specialist calculations and every technical lemma remain in the proof pages.

| Phase | Stable IDs | Progression |
|---|---|---|
| Background/preliminaries | M01–M11 | Individual states and cells → correction and distinguishability → the complete experimental and statistical contract |
| Narrative/innovation | M12–M30 | Correctable algebra and exact tangent → globally paid protocol and converse → fast/fixed separation and grid law → a unified resource account |

Dependency links name earlier milestones whose ideas are needed. They describe the scientific order, not a requirement to read every cited textbook page before using the explanations.

## Phase I — Background/preliminaries

### M01 — A frequency becomes a measurement distribution

**Central question:** How does a signal frequency become something that an experiment can estimate?

**Understanding target:** Explain how a known Hermitian generator changes relative phases, how preparation and measurement turn those phases into outcome probabilities, and why a single measurement outcome is not itself the unknown frequency. Distinguish a physical state from an estimator constructed from repeated outcomes.

**Dependencies and story role:** No earlier milestone. This introduces the sensor, the unknown parameter and the observable evidence before noise or feedback is added.

**Conceptual connection:** Unitary evolution and the Born rule become the starting point for an estimation problem. The logical X/Y readouts later used in the construction are concrete instances of this connection.

**Source pointers:** N&C §§2.1–2.2 and 2.4; [exact sensing cells](../science/model.md#exact-sensing-cells); [fixed-quadrature means, Eqs. (U17)–(U19)](../science/grid_upper.md#5-one-refinement-stage-using-two-fixed-measurements).

### M02 — One physical cell is an exact noisy channel

**Central question:** What operation does the sensor undergo between two correction boundaries?

**Understanding target:** Read the cell as the exponential of the simultaneous Hamiltonian and dissipative generators. Explain the roles of the Hermitian jump operators, the cell duration and the density operator. Distinguish this exact channel from a leading short-time approximation or an assumed product of a noise channel and a signal unitary.

**Dependencies and story role:** [M01](#m01--a-frequency-becomes-a-measurement-distribution). The individual sensing step becomes the physical object that every protocol must use.

**Conceptual connection:** A master equation specifies a complete operation over a positive duration. Its full duration, rather than only its first derivative at zero time, determines the finite-cadence problem.

**Source pointers:** N&C §§8.2.2–8.2.4 and 8.4.1; [exact sensing cells](../science/model.md#exact-sensing-cells); [construction, Eq. (C1)](../science/constructive_proof.md#1-statement-and-quantifiers).

### M03 — Memory, instruments and the accessible experiment

**Central question:** What can a controller retain and change without gaining access to the noise environment?

**Understanding target:** Distinguish the active sensor, a noiseless ancilla, a classical record and an inaccessible environment. Explain how a quantum instrument produces both an outcome and a conditional quantum state, and how boundary preparation, recovery and measurement can be represented as parameter-independent operations.

**Dependencies and story role:** [M01](#m01--a-frequency-becomes-a-measurement-distribution), [M02](#m02--one-physical-cell-is-an-exact-noisy-channel). This extends one cell into the ingredients of an adaptive experiment.

**Conceptual connection:** An ancilla can preserve coherence without becoming another active sensor. A mathematical trajectory representation can explain a channel without making its jump times observable to the controller.

**Source pointers:** N&C §§2.2, 2.4–2.5 and 8.2.2–8.2.4; [allowed operations and resources](../science/model.md#allowed-operations-and-resources); [unobserved trajectory representation](../science/grid_upper.md#2-exact-corrected-cell).

### M04 — An error span and an error algebra ask different questions

**Central question:** Why can correcting the leading noise operators differ from correcting the errors of a whole positive-time cell?

**Understanding target:** Distinguish a linear span of selected operators from the unital star algebra generated by every finite product of the jumps. Keep the real Hermitian Lindblad span separate from the full complex algebra. Explain why higher jump words can enlarge the relevant operator space.

**Dependencies and story role:** [M02](#m02--one-physical-cell-is-an-exact-noisy-channel). This isolates the algebraic distinction that later separates fast correction from a fixed clock.

**Conceptual connection:** Closure under composition turns individual error operators into a collective error space. The importance of those products comes from the exact physical cell, not from a change in notation.

**Source pointers:** N&C §2.1 and §10.3.1 for linear-error-space foundations; [the full noise algebra](../science/model.md#the-full-noise-algebra); [fast correction and one fixed clock](../references/RELATED_WORK.md#fast-correction-and-one-fixed-clock).

### M05 — Correct noise without erasing the useful signal

**Central question:** What must be indistinguishable to an error-correcting code, and what must remain distinguishable for sensing?

**Understanding target:** Explain the Knill–Laflamme condition as equality of error-overlap data across logical states, together with the vanishing of inappropriate logical cross terms. Distinguish correcting an error space from preserving every Hamiltonian. A useful sensing code must remove the relevant noise while retaining a nontrivial logical signal.

**Dependencies and story role:** [M03](#m03--memory-instruments-and-the-accessible-experiment), [M04](#m04--an-error-span-and-an-error-algebra-ask-different-questions). This converts the operator-space distinction into a task for encoding and recovery.

**Conceptual connection:** Quantum error correction protects distinguishability within the logical system. Metrology adds the requirement that the unknown parameter still change that protected system.

**Source pointers:** N&C §10.3; [algebra-wide code condition, Eqs. (C6)–(C11)](../science/constructive_proof.md#2-an-explicit-code-and-a-rate-independent-decoder); [four-level code moments, Eq. (F3)](../science/fast_fixed_separation.md#1-the-signal-passes-hnls-but-belongs-to-the-full-algebra).

### M06 — A physical counterfield changes the cell

**Central question:** Why is subtracting a frequency estimate during noisy evolution a physical resource?

**Understanding target:** Explain the residual detuning $`\delta=\omega-c`$, where the known field value $`c`$ is chosen from earlier data and held throughout a cell. Distinguish this physical cancellation from subtracting a number from an estimate or applying a known rotation only after the cell. Identify commutation as the special circumstance in which a boundary rotation can represent the same compensation.

**Dependencies and story role:** [M02](#m02--one-physical-cell-is-an-exact-noisy-channel), [M03](#m03--memory-instruments-and-the-accessible-experiment). This identifies the control family whose powers and limitations are being compared.

**Conceptual connection:** Feedback can change the noise-affected experiment itself. The resulting channel still depends on the unknown residual; no accurate frequency has been provided for free.

**Source pointers:** N&C §8.4.1 for generator language; [exact sensing cells](../science/model.md#exact-sensing-cells); [physical compensation](../science/interpretation.md#physical-compensation-keeps-the-experiment-near-an-exactly-correctable-point); [commuting exception, Eq. (F22)](../science/fast_fixed_separation.md#4-every-fixed-positive-clock-has-finite-information-per-cell).

### M07 — Compare channels and identify their support

**Central question:** Which mathematical descriptions let one compare all possible uses of a noisy cell?

**Understanding target:** Distinguish trace distance between output states, a channel's diamond-norm difference when ancillary inputs are allowed, and the support of its Choi operator. Explain that Choi support corresponds to a vectorized Kraus-operator space, and that positivity on a fixed proper support is different from full rank on the ambient space.

**Dependencies and story role:** [M02](#m02--one-physical-cell-is-an-exact-noisy-channel), [M03](#m03--memory-instruments-and-the-accessible-experiment), [M04](#m04--an-error-span-and-an-error-algebra-ask-different-questions). These descriptions prepare both the constructive approximation bounds and the converse.

**Conceptual connection:** Operational distinguishability and operator support answer complementary questions: how much two experiments can differ, and which directions a physical channel actually occupies.

**Source pointers:** N&C §9.2.1 and §§8.2.2–8.2.4 as foundations; [Choi convention and exact support](../science/converse_proof.md#2-exact-finite-time-kraus-support); [channel comparison, Eqs. (C42)–(C44)](../science/constructive_proof.md#10-matching-total-time-lower-bound). The project's bridge supplies the channel-norm and support extensions.

### M08 — Local sensitivity and global risk are different claims

**Central question:** What must be proved to estimate an initially unknown frequency over a fixed band?

**Understanding target:** Read mean-square error as an average over outcomes and minimax risk as the worst frequency followed by optimization over allowed protocols. Distinguish local Fisher information near a working point from a uniform risk guarantee on a nonshrinking band. Recognize that a biased estimator, an alias or a rare large mistake cannot be dismissed by quoting local sensitivity.

**Dependencies and story role:** [M01](#m01--a-frequency-becomes-a-measurement-distribution), [M07](#m07--compare-channels-and-identify-their-support). This supplies the statistical objective before an adaptive protocol is judged.

**Conceptual connection:** A physical response must be turned into a complete inference rule. Inverse-square and inverse-time risk refer to this rule's total error, not just to the slope of an observable.

**Source pointers:** N&C §9.2.1 for distinguishability background; [risk and resource definitions](../science/model.md#allowed-operations-and-resources); [global risk discussion](../science/interpretation.md#physical-compensation-keeps-the-experiment-near-an-exactly-correctable-point); [biased-estimator bound](../science/converse_proof.md#5-global-risk-without-an-unbiasedness-assumption).

### M09 — Charge every history to one budget

**Central question:** How is an adaptive experiment compared fairly when its outcomes determine later actions?

**Understanding target:** Explain why every prepared batch, failed decision and postselection failure consumes its actual cells. Distinguish a deterministic cap of $`N=\lfloor T/\tau\rfloor`$ cells on every history from an average cost or a cost conditioned on success. Separate sensing time from the assumed ideal, instantaneous boundary operations.

**Dependencies and story role:** [M03](#m03--memory-instruments-and-the-accessible-experiment), [M06](#m06--a-physical-counterfield-changes-the-cell), [M08](#m08--local-sensitivity-and-global-risk-are-different-claims). The statistical objective now has a complete operational resource constraint.

**Conceptual connection:** Feedback alters the path through an experiment but does not erase the cost or probability of an unfavorable path. Both constructive risk estimates and universal lower bounds must retain those paths.

**Source pointers:** N&C §8.2 for quantum-operation foundations; [allowed operations and resources](../science/model.md#allowed-operations-and-resources); [exact budget choice](../science/constructive_proof.md#9-exact-budget-choice-and-resource-accounting); [full-history converse](../science/converse_proof.md#4-adaptive-histories-and-coherent-memory-are-included).

### M10 — Identification can fail even with a useful tangent

**Central question:** Can a sensor be locally sensitive while two distinct frequencies remain globally indistinguishable?

**Understanding target:** Explain an alias as equality of the accessible cell channels at different frequencies, and why repeated or adaptive use cannot distinguish an exact alias pair. Distinguish choosing a small cadence for a fixed band from accepting an arbitrary supplied cadence and band.

**Dependencies and story role:** [M01](#m01--a-frequency-becomes-a-measurement-distribution), [M02](#m02--one-physical-cell-is-an-exact-noisy-channel), [M06](#m06--a-physical-counterfield-changes-the-cell), [M08](#m08--local-sensitivity-and-global-risk-are-different-claims). This completes the distinction between local response and the globally meaningful experiment.

**Conceptual connection:** Periodic phase information can carry strong local derivatives and still lose the label of the correct period. Identifiability is therefore an additional question beside the rate at which information accumulates.

**Source pointers:** N&C §§2.2 and 9.2.1 as foundations; [identification is a separate requirement](../science/interpretation.md#identification-is-a-separate-requirement); [exact aliases and an alias-free upper bound](../science/fast_fixed_separation.md#5-exact-aliases-and-an-alias-free-sql-upper-bound).

### M11 — Assemble the fixed-cadence question

**Central question:** What complete experiment is classified by the project's main theorem?

**Understanding target:** State together the finite-dimensional sensor, Hermitian parameter-independent noise, exact simultaneous cell, one active sensing system, ideal boundary operations, inaccessible environment, classical counterfield, fixed band, hard total time and minimax loss. Explain the order of choices: the physical model and band are fixed, one suitable positive cadence may be chosen, and only then does the horizon grow.

**Dependencies and story role:** [M04](#m04--an-error-span-and-an-error-algebra-ask-different-questions)–[M10](#m10--identification-can-fail-even-with-a-useful-tangent), drawing on [M01](#m01--a-frequency-becomes-a-measurement-distribution)–[M03](#m03--memory-instruments-and-the-accessible-experiment). This is the background phase's synthesis.

**Conceptual connection:** Algebra, controller access, statistical loss and resource accounting form one problem. Changing any of them can change the answer even when the phrase “quantum sensing with error correction” stays the same.

**Source pointers:** [Model and exact results](../science/model.md); [resource interpretation](../science/interpretation.md); [Nielsen–Chuang bridge](NIELSEN_CHUANG_BRIDGE.md), integrating the selected textbook foundations.

## Phase II — Narrative/innovation

### M12 — Turn the signal outside the algebra into a code

**Central question:** How does an operator component outside the noise algebra specify two protected logical states?

**Understanding target:** Explain the residual $`Q=G-\Pi_{\mathcal A_F}G`$, why it is a nonzero traceless Hermitian operator, and how its positive and negative parts yield two density operators. Connect their purifications on disjoint ancilla supports to equal algebra expectations, zero logical cross terms and a surviving signal difference.

**Dependencies and story role:** [M04](#m04--an-error-span-and-an-error-algebra-ask-different-questions), [M05](#m05--correct-noise-without-erasing-the-useful-signal), [M11](#m11--assemble-the-fixed-cadence-question). The narrative begins with the concrete object that makes the positive direction possible.

**Conceptual connection:** Hilbert–Schmidt orthogonality becomes an experimentally meaningful separation: the noise algebra cannot distinguish the two logical populations in the prohibited way, while the signal can act differently on them.

**Source pointers:** N&C §§2.1, 2.4–2.5 and 10.3; [explicit code, Eqs. (C4)–(C6)](../science/constructive_proof.md#2-an-explicit-code-and-a-rate-independent-decoder).

### M13 — One decoder corrects an entire algebra

**Central question:** Why can the same recovery work without knowing the actual jump rates?

**Understanding target:** Explain how the scalar Knill–Laflamme Gram matrix separates orthogonal error isometries and supplies a trace-preserving decoder, including the unused orthogonal complement. Distinguish the geometry of a correctable algebra from the Kraus weights of a particular channel. Understand why correcting every Kraus operator in the known envelope algebra makes the decoder independent of rates, field setting and sensing horizon.

**Dependencies and story role:** [M05](#m05--correct-noise-without-erasing-the-useful-signal), [M12](#m12--turn-the-signal-outside-the-algebra-into-a-code). This turns the code's algebraic property into a physical boundary operation.

**Conceptual connection:** Error correction can be robust to uncertain probabilities when its operator space is already corrected. The persistent encoding ancilla has dimension at most the sensor dimension; implementing recovery can additionally use a fixed reset apparatus.

**Source pointers:** N&C §10.3; [decoder and universal correction, Eqs. (C7)–(C11)](../science/constructive_proof.md#2-an-explicit-code-and-a-rate-independent-decoder); [unknown rates along known directions](../science/model.md#unknown-rates-along-known-directions).

### M14 — Find the exact finite-cell signal tangent

**Central question:** What signal survives after a whole noisy cell is corrected at zero residual detuning?

**Understanding target:** Explain why the compensated null channel is corrected exactly, while the first derivative away from it is a logical Hamiltonian. Interpret $`B_\tau=\int_0^\tau e^{t\mathcal D^\dagger}(G)\,dt`$ as the noise-evolved signal integrated across the physical cell. Distinguish this tangent from an assumed noiseless value $`\tau G`$. Explain why Hermitian noise gives a strictly positive overlap with the residual code direction.

**Dependencies and story role:** [M02](#m02--one-physical-cell-is-an-exact-noisy-channel), [M06](#m06--a-physical-counterfield-changes-the-cell), [M12](#m12--turn-the-signal-outside-the-algebra-into-a-code), [M13](#m13--one-decoder-corrects-an-entire-algebra). This connects the fixed decoder to exact finite-time dynamics.

**Conceptual connection:** Exact null correction and a nonzero nearby tangent can coexist. Positivity of that tangent is a local statement; global estimation still needs controlled nonlinear errors and identification.

**Source pointers:** N&C §8.4.1 and §10.3 as foundations; [exact null correction](../science/constructive_proof.md#3-exact-correction-at-the-compensated-point); [tangent, Eqs. (C16)–(C20)](../science/constructive_proof.md#4-the-exact-finite-cell-signal-tangent); [positivity](../science/constructive_proof.md#5-positivity-of-the-tangent-and-uniform-rate-bounds).

### M15 — Balance linear signal against quadratic mismatch

**Central question:** Why can increasingly long coherent blocks remain useful at one fixed correction interval?

**Understanding target:** Contrast the first-order logical phase with the second-order detuning remainder. Explain how the cell bound telescopes across a block, giving a total channel error bounded by $`4n\delta^2\tau^2\|G\|^2`$. Connect shrinking residual uncertainty with increasing block length, and explain why known rate bounds suffice for a uniformly positive slope without measuring the rates.

**Dependencies and story role:** [M07](#m07--compare-channels-and-identify-their-support), [M14](#m14--find-the-exact-finite-cell-signal-tangent). This supplies the controlled approximation needed to use the local tangent repeatedly.

**Conceptual connection:** The controller gains time to accumulate phase by reducing the mismatch that produces decoherence. A once-chosen sufficiently small cadence makes this balance valid even at the initial, widest interval.

**Source pointers:** [Uniform rate bounds, Eqs. (C24)–(C25)](../science/constructive_proof.md#5-positivity-of-the-tangent-and-uniform-rate-bounds); [quadratic remainder, Eqs. (C26)–(C28)](../science/constructive_proof.md#6-a-uniform-quadratic-cell-remainder); [cadence conditions, Eq. (C30)](../science/constructive_proof.md#7-a-sign-test-with-one-fixed-cadence). These are project derivations beyond the anchor's channel foundations.

### M16 — Refine an interval without knowing the exact slope

**Central question:** How can one fixed readout tell the controller which part of its current frequency interval to retain?

**Understanding target:** Explain the outer-quarter sign margin, the central overlap shared by the two candidate intervals, and the role of repeated bounded measurement outcomes. Distinguish the conditional reliability claim made while the truth is inside the current interval from the protocol's definition on every history. Recognize why a known positive slope bound is sufficient even when its actual value is unknown.

**Dependencies and story role:** [M08](#m08--local-sensitivity-and-global-risk-are-different-claims), [M09](#m09--charge-every-history-to-one-budget), [M15](#m15--balance-linear-signal-against-quadratic-mismatch). This turns a controlled physical response into one adaptive estimation step.

**Conceptual connection:** Overlap prevents a near-zero signal from forcing an unreliable left/right decision. Nested intervals also retain geometric control of the eventual error after a later decision goes wrong.

**Source pointers:** [Sign test and overlap, Eqs. (C29)–(C35)](../science/constructive_proof.md#7-a-sign-test-with-one-fixed-cadence); [physical-compensation interpretation](../science/interpretation.md#physical-compensation-keeps-the-experiment-near-an-exactly-correctable-point).

### M17 — Complete the globally paid Heisenberg construction

**Central question:** How do reliable refinements become a uniform inverse-square risk guarantee under a hard time cap?

**Understanding target:** Explain the first-exclusion decomposition: an early mistake is more costly, so earlier stages receive stronger reliability. Connect the bound $`R\le13w_K^2`$ to a deterministic cost of at most a constant divided by $`w_K`$, and hence to a final width of order $`T^{-1}`$. Explain how the two-frequency distinguishability argument supplies the matching inverse-square lower bound.

**Dependencies and story role:** [M08](#m08--local-sensitivity-and-global-risk-are-different-claims), [M09](#m09--charge-every-history-to-one-budget), [M16](#m16--refine-an-interval-without-knowing-the-exact-slope). This integrates the positive branch from code to complete estimation theorem.

**Conceptual connection:** The protocol earns its accurate working point using the same budget as its fine sensing. Fixed code, recovery, ancilla and readout coexist with improving classical field precision, logarithmically many settings and a linear-in-time number of fixed-duration correction cells.

**Source pointers:** [Global risk](../science/constructive_proof.md#8-global-risk-without-an-uncharged-accurate-prior); [exact budget and resources](../science/constructive_proof.md#9-exact-budget-choice-and-resource-accounting); [matching lower bound](../science/constructive_proof.md#10-matching-total-time-lower-bound).

### M18 — Determine the full physical Kraus support

**Central question:** When the signal belongs to the noise algebra, why does every positive-time cell have exactly that operator support?

**Understanding target:** Follow both inclusions: every trajectory stays in the algebra, while trajectories with arbitrarily many jumps recover all finite words in its span. Explain the use of positivity, continuity and closed support when jump times approach a boundary. Distinguish a support argument from assigning positive probability to simultaneous jumps or granting access to their record.

**Dependencies and story role:** [M04](#m04--an-error-span-and-an-error-algebra-ask-different-questions), [M07](#m07--compare-channels-and-identify-their-support), [M11](#m11--assemble-the-fixed-cadence-question). This starts the converse from the physical channel before any recovery.

**Conceptual connection:** Rare trajectories can determine exact support even when they are negligible in a leading short-time approximation. The actual Hermitian jumps, including which rates are nonzero, determine the algebra used here.

**Source pointers:** N&C §§8.2.2–8.2.4 for channel representations; [exact support, Eqs. (C3)–(C6)](../science/converse_proof.md#2-exact-finite-time-kraus-support).

### M19 — Bound information in the whole adaptive record

**Central question:** Why can arbitrary codes, memory and feedback add at most a fixed amount of information per cell in the converse regime?

**Understanding target:** Explain why a detuning-independent Choi support, positivity on that support and a compact accessible detuning range give finite channel RLD information. Describe how the full classical-history-plus-quantum-memory state retains both outcome-probability information and conditional quantum information. At a fixed history, the chosen field is held fixed when differentiating; the history's parameter dependence remains included.

**Dependencies and story role:** [M03](#m03--memory-instruments-and-the-accessible-experiment), [M06](#m06--a-physical-counterfield-changes-the-cell), [M09](#m09--charge-every-history-to-one-budget), [M18](#m18--determine-the-full-physical-kraus-support). This lifts the one-cell bound to every allowed adaptive protocol.

**Conceptual connection:** The inherited RLD chain rule and data processing control the entire experiment, not only one decoder or one measurement. A fixed bounded field range is material to the general uniform bound.

**Source pointers:** [Uniform channel information](../science/converse_proof.md#3-a-uniformly-finite-channel-information-bound); [adaptive histories and memory](../science/converse_proof.md#4-adaptive-histories-and-coherent-memory-are-included); [RLD21, Propositions 29 and 38](../references/SOURCES.md#rld21). RLD is a research-level ingredient beyond the selected anchor.

### M20 — Convert the information bound into the classification

**Central question:** What global estimation obstruction follows from information that grows only linearly with cell count?

**Understanding target:** Explain the smooth-prior, integration-by-parts argument that bounds risk without assuming an unbiased estimator. Read the resulting lower bound $`1/(NM+\pi^2/W^2)`$ with its fixed-model constants. Combine it with the constructive branch to classify the existence of a sufficiently small, horizon-independent cadence supporting Heisenberg order.

**Dependencies and story role:** [M08](#m08--local-sensitivity-and-global-risk-are-different-claims), [M10](#m10--identification-can-fail-even-with-a-useful-tangent), [M17](#m17--complete-the-globally-paid-heisenberg-construction), [M19](#m19--bound-information-in-the-whole-adaptive-record). This integrates the two sides of the general theorem.

**Conceptual connection:** A Bayesian lower bound on one supported prior constrains worst-case risk. An inverse-time lower bound excludes inverse-square performance; it does not guarantee inverse-time attainment when a scalar signal or aliases prevent identification.

**Source pointers:** [Global risk without unbiasedness](../science/converse_proof.md#5-global-risk-without-an-unbiasedness-assumption); [consequence and boundaries](../science/converse_proof.md#6-consequence-and-boundaries); [fixed-cadence criterion](../science/model.md#result-1-the-fixed-cadence-criterion).

### M21 — Build the four-level algebraic separation

**Central question:** How can a signal pass the fast-control criterion and fail the fixed-cadence criterion in the same sensor?

**Understanding target:** Explain why the cubic signal $`G=L^3`$ for $`L=\mathrm{diag}(-3,-1,1,3)`$ lies outside the quadratic real span but inside the full diagonal algebra. Connect the displayed code's equal first two noise moments and unequal cubic signal moments to its first-order recovered Hamiltonian. Distinguish this correction of leading errors from exact correction at positive duration.

**Dependencies and story role:** [M04](#m04--an-error-span-and-an-error-algebra-ask-different-questions), [M05](#m05--correct-noise-without-erasing-the-useful-signal), [M18](#m18--determine-the-full-physical-kraus-support), [M20](#m20--convert-the-information-bound-into-the-classification). This turns the abstract distinction into one explicit physical witness.

**Conceptual connection:** Polynomial degree separates two error spaces without changing the sensor or signal. There is no contradiction between the two criteria because they describe different correction-rate resources.

**Source pointers:** N&C §10.3 for error-correction foundations; [algebra and code, Eqs. (F1)–(F3)](../science/fast_fixed_separation.md#1-the-signal-passes-hnls-but-belongs-to-the-full-algebra); [finite-step approximation](../science/fast_fixed_separation.md#2-an-explicit-recovery-and-a-finite-step-approximation); [HNLS18](../references/SOURCES.md#hnls18).

### M22 — Compare the fast and fixed clocks globally

**Central question:** What resource changes when the four-level sensor moves from inverse-time to inverse-square error?

**Understanding target:** Explain why the explicit fast construction chooses its interval as $`h(T)=\Theta(T^{-1})`$ and uses $`\Theta(T^2)`$ recoveries while still charging at most total sensing time $`T`$. Contrast that construction with the all-strategy fixed-clock information bound. Explain why the exact alias period limits the fixed-clock SQL upper bound to an identifiable interval.

**Dependencies and story role:** [M09](#m09--charge-every-history-to-one-budget), [M10](#m10--identification-can-fail-even-with-a-useful-tangent), [M17](#m17--complete-the-globally-paid-heisenberg-construction), [M20](#m20--convert-the-information-bound-into-the-classification), [M21](#m21--build-the-four-level-algebraic-separation). This completes the first resource comparison at the same global-risk level.

**Conceptual connection:** A cadence fixed during one run can still shrink with the planned horizon. The correction count is a demonstrated resource of this construction, not a universal minimum; unlimited classical field precision cannot remove the commuting witness's fixed-clock obstruction.

**Source pointers:** [Global fast protocol and resources](../science/fast_fixed_separation.md#3-a-global-fast-clock-protocol-with-every-outcome-charged); [fixed-clock bound](../science/fast_fixed_separation.md#4-every-fixed-positive-clock-has-finite-information-per-cell); [aliases and SQL upper bound](../science/fast_fixed_separation.md#5-exact-aliases-and-an-alias-free-sql-upper-bound).

### M23 — Read the exact transverse-qubit response

**Central question:** What happens to the signal phase when bit-flip noise is corrected only at cell boundaries?

**Understanding target:** Explain the parity code, the unobserved telegraph sign of the accumulated phase and the exact corrected coherence function $`f(z)`$. Distinguish phase response from visibility. Connect its nonzero phase slope and quadratic attenuation near zero detuning to the mechanism behind compensation, without replacing the exact response by an unmodified noiseless phase.

**Dependencies and story role:** [M01](#m01--a-frequency-becomes-a-measurement-distribution), [M02](#m02--one-physical-cell-is-an-exact-noisy-channel), [M05](#m05--correct-noise-without-erasing-the-useful-signal), [M14](#m14--find-the-exact-finite-cell-signal-tangent). This begins the second resource comparison with a completely specified qubit channel.

**Conceptual connection:** A fixed parity recovery removes the final bit flip but does not reveal when flips changed the sign of phase accumulation. The residual phase spread is physical even though the trajectory model is used only for calculation.

**Source pointers:** [Exact corrected cell, Eqs. (U3)–(U7)](../science/grid_upper.md#2-exact-corrected-cell); [phase and visibility bounds](../science/grid_upper.md#3-uniform-phase-and-visibility-bounds); [FIXED21](../references/SOURCES.md#fixed21) and [NOISERATE](../references/SOURCES.md#noiserate) for credited antecedents.

### M24 — Estimate more finely than the physical grid

**Central question:** Why does a discrete set of field values not force the final estimate to lie on that same grid?

**Understanding target:** Separate the interval center, the nearest available physical field and the estimated frequency. Explain how two fixed X/Y quantum measurements are combined using a classically calculated reference phase from the exact response. Identify where knowledge of the positive noise rate enters and why this processing requires no increasingly precise quantum measurement axis.

**Dependencies and story role:** [M06](#m06--a-physical-counterfield-changes-the-cell), [M16](#m16--refine-an-interval-without-knowing-the-exact-slope), [M23](#m23--read-the-exact-transverse-qubit-response). This constructs one grid-compatible refinement step.

**Conceptual connection:** Coarse physical compensation leaves a residual detuning; calibrated inference can still resolve frequencies within a grid gap. Control resolution and the numerical precision of an estimate are different resources.

**Source pointers:** [Grid covering and small-band conditions](../science/grid_upper.md#4-fixed-band-and-grid-range); [fixed measurements and classical projection, Eqs. (U15)–(U21)](../science/grid_upper.md#5-one-refinement-stage-using-two-fixed-measurements); [classical precision and known-rate requirement](../science/grid_upper.md#10-what-precision-and-resources-are-used).

### M25 — Pay for both quadratures and all grid refinements

**Central question:** How does limited compensation resolution change the best useful coherent block and the total sensing bill?

**Understanding target:** Explain why the block length balances interval width against squared grid spacing in dimensionless variables. Connect the reduced sign margin to additional repetitions, count both independent quadrature batches, and follow the deterministic cost bound that produces inverse-square plus grid-dependent inverse-time risk. Distinguish this batch count from the logarithm-squared count of the continuous-field protocol.

**Dependencies and story role:** [M09](#m09--charge-every-history-to-one-budget), [M16](#m16--refine-an-interval-without-knowing-the-exact-slope), [M17](#m17--complete-the-globally-paid-heisenberg-construction), [M24](#m24--estimate-more-finely-than-the-physical-grid). This closes the grid construction at the global, hard-budget level.

**Conceptual connection:** Once the grid limits useful coherent accumulation, more independent data carry the refinement cost. The first-error geometry still works, but its concentration margin and payment schedule must be recomputed.

**Source pointers:** [Concentration and interval update](../science/grid_upper.md#6-concentration-and-interval-update); [global risk](../science/grid_upper.md#7-global-risk-with-all-failures-included); [two-quadrature cell count](../science/grid_upper.md#8-deterministic-cell-count-including-both-quadratures); [integer-budget rule](../science/grid_upper.md#9-a-budget-rule-valid-for-every-integer-budget).

### M26 — Find the obstruction before choosing a decoder

**Central question:** What feature of the unrecovered qubit cell prevents a different boundary code from eliminating the grid penalty?

**Understanding target:** Explain why the physical Choi matrix has rank two at zero detuning and full rank at every nonzero detuning for positive noise. Connect positive contributions from one- and two-jump trajectories to the quadratic opening of its smallest eigenvalue near the compensated point. Distinguish this unrecovered-channel statement from the performance of the displayed parity recovery.

**Dependencies and story role:** [M07](#m07--compare-channels-and-identify-their-support), [M18](#m18--determine-the-full-physical-kraus-support), [M23](#m23--read-the-exact-transverse-qubit-response). This finds the physical obstruction required for an all-strategy grid converse.

**Conceptual connection:** Unobserved jump timing creates channel directions that a final parity correction alone does not remove. Positivity of the rate is essential: at zero noise the unitary channel has different support and this obstruction disappears.

**Source pointers:** [Physical Choi rank and eigenvalue bounds, Eqs. (L5)–(L11)](../science/grid_lower.md#2-the-full-physical-choi-matrix-loses-rank-only-at-zero-detuning); [verification scope](../verification/README.md#what-the-checks-do-not-settle).

### M27 — Use one grid gap to constrain every adaptive policy

**Central question:** How can a lower bound remain valid when a controller switches or dithers among grid fields after every cell?

**Understanding target:** Explain why the middle half of an interior lattice gap stays a definite distance from every allowed field value. Use that fact to understand the uniform per-cell information bound, the full-history chain rule and the smooth-prior risk bound. Identify why the common condition $`\Delta\le W`$ guarantees a suitable gap for every offset.

**Dependencies and story role:** [M19](#m19--bound-information-in-the-whole-adaptive-record), [M20](#m20--convert-the-information-bound-into-the-classification), [M26](#m26--find-the-obstruction-before-choosing-a-decoder). This turns the physical support calculation into the grid obstruction for arbitrary allowed controllers.

**Conceptual connection:** The same hard set of frequencies stays away from all instantaneous grid choices, so changing the choice from one boundary to the next does not invalidate the bound. Subcell switching or a coherent field register would define a different experiment.

**Source pointers:** [Information away from every lattice point, Eqs. (L12)–(L15)](../science/grid_lower.md#3-uniform-information-bound-away-from-every-lattice-point); [biased-estimator minimax bound](../science/grid_lower.md#4-a-biased-estimator-minimax-bound); [why a physical-channel bound is needed](../references/RELATED_WORK.md#why-the-calibrated-grid-requires-a-physical-channel-bound).

### M28 — Interpret the matched resolution law with its quantifiers

**Central question:** What must improve with the sensing horizon when the recovery clock itself stays fixed?

**Understanding target:** Combine the grid upper and lower bounds to read $`R_T^*=\Theta(T^{-2}+\tau\Delta^2/T)`$ uniformly over the stated spacings and offsets. Explain the crossover and why $`\Delta=O((\tau T)^{-1/2})`$ retains Heisenberg order at fixed model parameters. Distinguish the known-positive-rate grid theorem from the unknown-bounded-rate continuous-field sufficiency theorem, and distinguish the actual jump algebra from its known envelope when rates may vanish.

**Dependencies and story role:** [M13](#m13--one-decoder-corrects-an-entire-algebra), [M20](#m20--convert-the-information-bound-into-the-classification), [M25](#m25--pay-for-both-quadratures-and-all-grid-refinements), [M27](#m27--use-one-grid-gap-to-constrain-every-adaptive-policy). This integrates the grid branch with the general classification.

**Conceptual connection:** A fixed recovery interval does not mean every control precision remains fixed. A fixed grid eventually yields an inverse-time term, not a constant error floor; the noise-free limit and unknown calibration are separate cases.

**Source pointers:** [Compensation-resolution law](../science/model.md#result-3-a-compensation-resolution-law); [unknown-rate quantifiers](../science/model.md#unknown-rates-along-known-directions); [grid interpretation and exclusions](../science/grid_lower.md#5-interpretation-and-exclusions).

### M29 — Follow the evidence from ingredient to conclusion

**Central question:** Which parts of the scientific account are inherited, analytically established here or checked only in finite examples?

**Understanding target:** Trace the roles of algebraic error correction, local channel criteria, exact transverse response, global phase-estimation ideas and the RLD chain rule to their cited sources. Explain what the deterministic matrix checks can detect and why sampled signs, eigenvalues or derivatives do not prove universal support or infinite-horizon minimax rates. Distinguish the operational contribution from a claim of exhaustive priority.

**Dependencies and story role:** [M17](#m17--complete-the-globally-paid-heisenberg-construction), [M20](#m20--convert-the-information-bound-into-the-classification), [M22](#m22--compare-the-fast-and-fixed-clocks-globally), [M28](#m28--interpret-the-matched-resolution-law-with-its-quantifiers). This integrates the proof routes with their evidential and attribution boundaries.

**Conceptual connection:** A trustworthy conclusion has a chain of explicit assumptions, imported tools, project-specific derivations and appropriate checks. Neither a textbook reference nor successful numerical reproduction replaces a missing link in that chain.

**Source pointers:** [Related work](../references/RELATED_WORK.md); [primary source index](../references/SOURCES.md); [verification and its limits](../verification/README.md); [boundaries and proof dependencies](../science/model.md#boundaries-and-proof-dependencies).

### M30 — Explain the whole control-resource picture

**Central question:** How do the fixed-cadence criterion, fast-clock witness and grid law fit into one physical account?

**Understanding target:** Explain why the full noise algebra governs the possibility of exact finite-cell protection, why adaptive physical compensation can turn its surviving tangent into global precision, and why compensation resolution remains a separate resource. Use the four-level and transverse-qubit examples to distinguish a fixed clock, a horizon-dependent clock and a finite field grid. State the load-bearing assumptions and what changes when identification, rate knowledge or physical access changes.

**Dependencies and story role:** [M11](#m11--assemble-the-fixed-cadence-question), [M17](#m17--complete-the-globally-paid-heisenberg-construction), [M20](#m20--convert-the-information-bound-into-the-classification), [M22](#m22--compare-the-fast-and-fixed-clocks-globally), [M28](#m28--interpret-the-matched-resolution-law-with-its-quantifiers), [M29](#m29--follow-the-evidence-from-ingredient-to-conclusion). This is the narrative phase's final synthesis.

**Conceptual connection:** The answer depends jointly on what evolves inside a cell, what can be controlled at its boundaries and what must be inferred from a fixed initial band. The results give a bounded operational classification with ideal controls, rather than a fault-tolerance claim or a universal statement for other noise models.

**Source pointers:** [Model and exact results](../science/model.md); [physical interpretation](../science/interpretation.md); [scope of the contribution](../references/RELATED_WORK.md); [Nielsen–Chuang bridge](NIELSEN_CHUANG_BRIDGE.md).

