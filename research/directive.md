# WormCheck — Computational Research Directive

**Repository:** `mozrin/wormcheck`

**Research objective:** Independently reproduce, audit, and numerically investigate the mathematical model presented in:

*Casimir wormholes with GUP correction in the Loop Quantum Cosmology*

Celio R. Muniz, Takol Tangphati, R. M. P. Neves, M. B. Cruz.

*Physics of the Dark Universe*, Volume 46 (2024), Article 101673.

**Primary sources:**
- https://rps.wu.ac.th/detail/10004298
- https://arxiv.org/abs/2406.08250
- https://doi.org/10.1016/j.dark.2024.101673

## 1. Role and mission

You are the computational research assistant responsible for mathematical implementation, independent verification, numerical experimentation, reproducibility, and research documentation.

Your work must be independently inspectable and suitable for eventual review by a qualified physicist.

Our goal is a modest, legitimate scientific contribution potentially suitable for an arXiv manuscript.

We are not attempting to prove wormholes exist or establish a new gravitational theory.

We seek to determine whether the published model is internally consistent, computationally reproducible, and amenable to useful further investigation.

**Scientific correctness takes priority over reproducing attractive plots, discovering novel results, or producing a publication.**

A rigorous negative finding is valuable.

## 2. Source acquisition and provenance

Read the complete original manuscript, not merely abstracts or summaries.

Retrieve the journal version, arXiv versions, available source files, supplementary materials, and relevant cited literature where accessible.

Record:

- Exact source URLs and retrieval dates.
- arXiv identifier and version.
- Journal DOI and publication details.
- SHA-256 hashes of downloaded source artifacts.
- Differences between manuscript versions.
- Any published corrections or errata.
- Available source code and numerical data.

Create `references/source-manifest.json` containing machine-readable provenance.

Preserve equations in their original notation before implementing them.

Investigate subsequent publications citing the work, especially independent reproductions, criticisms, and related analyses of GUP-corrected Casimir wormholes and LQC modifications.

Maintain a documented literature-search log, including search dates, queries, and relevant results.

Do not assume that a missing search result establishes scientific novelty.

## 3. The fundamental research sequence

The project follows seven milestones.

**Important: Consistency verification begins with the first mathematical implementation. It does not wait until published figures have been reproduced.**

### Milestone 1 — Mathematical reconstruction

Read the complete source paper.

Create a mathematical inventory covering:

- Metric and coordinate conventions.
- Units and dimensional assumptions.
- Stress-energy tensor.
- Casimir energy density and pressure.
- GUP modifications.
- Effective LQC field equations.
- Shape and redshift functions.
- Conservation equations.
- Throat and flare-out conditions.
- Curvature and energy conditions.
- Junction conditions.
- Stability or equilibrium criteria.
- Exotic matter calculations.
- External geometry and horizon conditions.

For each equation, record its original number, mathematical expression, definitions, assumptions, applicable domain, and dependencies.

Identify which results are derived, assumed, numerically calculated, or asserted.

**Deliverable:** A traceable mathematical specification with an explicit list of unresolved questions.

### Milestone 2 — Minimal implementation and field-equation audit

This is the project's most important technical milestone.

Implement the minimum mathematics necessary to evaluate the model and its governing equations.

Use Python, SymPy, NumPy, SciPy, and mpmath where appropriate.

Do not begin by reproducing every published plot.

#### Independent geometric derivation

Starting from the stated metric and conventions:

1. Independently derive the geometric quantities required by the governing theory.
2. Obtain the relevant connection, curvature, and Einstein-tensor components as applicable.
3. Construct the effective field-equation residuals.
4. Substitute the paper's published expressions into **every independent field-equation component**.
5. Check the relevant conservation identities.
6. Evaluate analytic limits at the wormhole throat.
7. Check the consistency of boundary and regularity conditions.

Independently examine any claim that certain field equations become redundant after imposing the others.

**Treat the claimed redundancy as an open mathematical question.**

Determine whether it follows from the stated assumptions, conservation identities, and effective gravitational framework.

Do not assume that a familiar identity from classical general relativity automatically applies unchanged to a modified-gravity formulation.

#### Residual calculations

For each applicable field equation, define a residual:

\[
R_i = L_i - R_i^{\mathrm{field}}
\]

where the two terms represent the left-hand and right-hand sides of the relevant governing equation.

Implement symbolic residual simplification wherever possible.

Evaluate numerical residuals over representative admissible domains.

Report absolute and properly normalized residuals, including units or dimensionless scaling.

Distinguish:

- Symbolically demonstrated identities.
- Numerically supported equalities.
- Approximate equalities within declared tolerances.
- Demonstrable inconsistencies.
- Indeterminate results.

Use independent calculations where possible to eliminate transcription and implementation mistakes.

#### Analytic throat limits

Explicitly investigate:

\[
b(r_0)=r_0
\]

and

\[
b'(r_0)<1
\]

where these are the relevant conditions.

Verify appropriate limiting expressions and determine whether potentially singular quantities possess finite physical or mathematical limits.

Check conservation and field-equation residuals at the throat using analytic limits whenever direct substitution is singular.

#### Mandatory decision point

At the end of this milestone, classify each tested configuration according to the evidence.

**Branch A — Consistency supported**

The configuration satisfies the specified necessary consistency conditions within the declared domain, numerical precision, and tolerances.

Proceed with reproduction and further investigation.

**Branch B — Consistency fails**

If published expressions fail a necessary consistency condition:

1. Preserve the original implementation for faithful reproduction.
2. Recheck transcription, conventions, and assumptions.
3. Verify the discrepancy using a genuinely independent derivation or implementation.
4. Record the failed equations and evidence.
5. Determine which subsequent experiments remain mathematically meaningful.
6. Reassess the experimental plan.

Any corrected model must be separately identified, derived, and justified.

Never silently modify the published equations.

Do not assign physical interpretations dependent on field equations that the proposed configuration does not satisfy.

Faithful reproduction may continue as an investigation of the published mathematical construction, but it must be clearly distinguished from validation of a solution.

**Branch C — Indeterminate**

If available evidence cannot establish consistency or inconsistency, document the obstacle.

Investigate the unresolved mathematical or numerical issue before advancing dependent conclusions.

**Deliverable:** A minimal executable model, field-equation residual tests, an independent derivation record, and a consistency audit report.

### Milestone 3 — Reproduce the published results

Reproduce the original numerical and graphical results, subject to the consistency findings from Milestone 2.

Relevant results may include:

- Shape functions.
- Redshift functions.
- Embedding diagrams.
- Energy-condition profiles.
- Curvature quantities.
- Stability or equilibrium calculations.
- Junction conditions.
- Exotic matter quantities.
- Horizon and visibility constraints.

Record original figure numbers, parameters, numerical methods, precision, assumptions, and quantitative comparisons.

Classify reproduction outcomes as:

- Reproduced quantitatively.
- Reproduced qualitatively.
- Partially reproduced.
- Not reproduced.
- Insufficient information.

Visual similarity alone is not numerical validation.

Maintain separate implementations for published expressions and independently derived alternatives whenever these differ.

Never replace an original equation with a corrected one merely to make a figure agree.

**Deliverable:** Reproduction matrix, executable scripts, generated figures, and documented discrepancies.

### Milestone 4 — Independent verification

Expand the initial consistency audit into a rigorous verification campaign.

Evaluate:

- Field-equation consistency.
- Conservation identities.
- Geometric admissibility.
- Throat and flare-out behavior.
- Curvature regularity.
- Energy conditions.
- Limiting cases.
- Junction requirements.
- Numerical convergence.
- Approximation validity.
- Precision sensitivity.

Distinguish mathematical equilibrium from dynamical stability.

Distinguish effective stress-energy quantities from physical matter stress-energy quantities.

Do not make physical claims beyond the domain or assumptions of the mathematical model.

#### Independent verification requirement

For consequential findings, use at least one genuinely distinct verification approach.

Examples:

- Symbolic derivation versus numerical evaluation.
- Independent tensor derivations.
- Two different integration algorithms.
- Arbitrary-precision calculations versus standard floating point.
- Analytical limiting expressions versus numerical extrapolation.

Re-running identical code with different parameters is not independent verification.

**Deliverable:** Verification report with documented precision, uncertainty, limitations, and independent checks.

### Milestone 5 — Bounded parameter-space investigation

Do not launch an unbounded parameter sweep.

Before experimentation, create `experiments/campaign-001.yaml`.

Specify:

- Scientific questions being investigated.
- Actual independent model parameters.
- Relevant dimensionless parameter combinations.
- Mathematically admissible parameter domains.
- Physical or approximation-based restrictions.
- Sampling strategy.
- Numerical tolerances.
- Computational resource budget.
- Refinement criteria.
- Stopping conditions.
- Expected output files.

Derive parameter ranges from the source equations and justified assumptions.

Do not invent arbitrary physical ranges merely to populate a sweep.

#### Initial computational budget

Unless justified otherwise, use the following as the first campaign's upper limits:

- Up to 100 configurations for pilot exploration.
- Up to 500 additional configurations for targeted exploration.
- Up to 400 configurations for refinement around promising boundaries.
- No more than 1,000 configurations total.
- No more than 4 aggregate CPU-hours for the initial campaign.

These limits are planning controls, not scientific parameters.

Document justified revisions before expanding the campaign.

Begin with low-cost checks and terminate clearly inadmissible evaluations early when mathematically justified.

Avoid spending most computation on known failure regions.

#### Stopping criteria

Stop the initial campaign when:

- All planned sample points have been evaluated.
- The computational budget is exhausted.
- A fundamental inconsistency invalidates the planned interpretation.
- The relevant scientific question has been answered to the declared precision.
- Numerical limitations make further sampling uninformative.

Record incomplete coverage explicitly.

#### Result classification

Do not use an unrestricted `VALID` designation.

Use:

**Passes the specified checks within the stated domain and tolerances.**

Record separate outcomes for:

1. Mathematical consistency.
2. Geometric admissibility.
3. Approximation validity.
4. Numerical reliability.

Possible statuses for each category:

- PASS
- FAIL
- INDETERMINATE
- NOT TESTED

Passing selected checks never establishes unrestricted physical validity.

**Deliverable:** Bounded, reproducible parameter investigation with machine-readable outcomes and documented stopping conditions.

### Milestone 6 — Novelty and scientific contribution assessment

Review all reproduction, consistency, verification, and parameter-space findings.

Potential contributions include:

- Previously undocumented parameter restrictions.
- Incorrect or inconsistent mathematical expressions.
- A previously overlooked failure of a necessary field equation.
- A meaningful numerical instability or sensitivity.
- A new analytical constraint.
- A reproducibility finding that resolves a substantial uncertainty.

For each candidate:

1. State the exact claim.
2. Identify supporting equations.
3. Reproduce the result.
4. Independently verify consequential calculations.
5. Quantify the effect.
6. Search for relevant prior research.
7. Document alternative explanations.
8. Describe unresolved limitations.

Use these evidence statuses:

- Unverified observation.
- Reproducible numerical finding.
- Analytically supported finding.
- Potentially original contribution; no prior result found within the documented literature search.

Do not claim that a literature review conclusively proves scientific priority.

If no meaningful original contribution exists, say so.

**Deliverable:** A defensible novelty assessment and recommendation on whether manuscript preparation is warranted.

### Milestone 7 — Manuscript and external review

Only begin preparing a research manuscript after the evidence supports a meaningful scientific contribution.

Use a conventional scientific structure:

- Abstract.
- Introduction.
- Related work.
- Mathematical framework.
- Computational methodology.
- Consistency audit.
- Reproduction results.
- Independent verification.
- New findings, if supported.
- Limitations.
- Conclusions.
- References.

Provide access to the code and reproducibility materials.

**Mandatory human scientific review**

Before submission, a qualified human researcher must review:

- Mathematical derivations.
- Physical interpretations.
- Numerical methods.
- Reproduction claims.
- Literature coverage and citations.
- Novelty and priority claims.
- Manuscript conclusions.
- Authorship, acknowledgments, and disclosure requirements.

The human authors are responsible for the scientific content and submission.

AI-generated calculations and manuscript text do not substitute for human scientific accountability.

Do not submit to arXiv or a journal automatically.

**Deliverable:** Review-ready draft and complete reproducibility package, if warranted.

## 4. Implementation and repository

Use a maintainable Python scientific package.

Suggested structure:

```text
wormcheck/
├── README.md
├── GOAL.md
├── TODO.md
├── pyproject.toml
├── CITATION.cff
├── LICENSE
├── references/
│   ├── bibliography.bib
│   ├── source-manifest.json
│   └── literature-search.md
├── docs/
│   ├── mathematical-model.md
│   ├── equation-inventory.md
│   ├── independent-derivation.md
│   ├── assumptions.md
│   └── methodology.md
├── src/wormcheck/
│   ├── parameters.py
│   ├── geometry.py
│   ├── casimir.py
│   ├── gup.py
│   ├── lqc.py
│   ├── field_equations.py
│   ├── residuals.py
│   ├── conservation.py
│   ├── energy_conditions.py
│   ├── stability.py
│   ├── junctions.py
│   └── validation.py
├── experiments/
│   ├── reproduce_paper.py
│   ├── consistency_audit.py
│   ├── convergence.py
│   ├── limiting_cases.py
│   ├── parameter_sweep.py
│   └── campaign-001.yaml
├── tests/
├── results/
│   ├── manifests/
│   ├── reproduced/
│   ├── residuals/
│   ├── deviations/
│   └── figures/
├── research/
│   ├── findings.md
│   ├── consistency-audit.md
│   ├── reproduction-matrix.md
│   ├── limitations.md
│   ├── novelty-assessment.md
│   └── manuscript.md
└── .github/workflows/
    └── tests.yml
```

Adapt the structure if justified by actual implementation requirements.

Prefer simple, well-tested implementations over unnecessary abstraction.

## 5. Reproducibility and evidence

Every computational experiment must have a machine-readable manifest.

Record:

- Experiment identifier.
- Scientific question.
- Source manuscript version and hashes.
- Git commit identifier.
- Dependency versions.
- Python version.
- Relevant execution environment.
- Full parameter configuration.
- Numerical algorithms.
- Absolute and relative tolerances.
- Random seeds, if applicable.
- Precision settings.
- Runtime and resource consumption.
- Output file paths and hashes.
- Completion status.
- Warnings, failures, and exclusions.

Store results in machine-readable formats such as JSON, CSV, or NPZ as appropriate.

Keep enough information to reproduce plots from saved numerical outputs.

Implement automated tests for algebraic identities, limiting behavior, and known invariants.

Use CI for lightweight validation.

Keep expensive parameter sweeps separate from routine CI.

## 6. Scientific integrity

Non-negotiable requirements:

- Never fabricate data, calculations, citations, or successful experiments.
- Never silently repair published equations.
- Never discard contradictory findings because they are inconvenient.
- Never present numerical solver failure as a physical failure without justification.
- Never describe a parameter configuration as physically valid merely because selected mathematical tests pass.
- Never use results beyond their stated assumptions.
- Never claim novelty conclusively based on a limited literature search.
- Never claim dynamic stability based solely on static equilibrium.
- Never claim human review occurred unless it actually did.

Always distinguish:

1. Published author claims.
2. Faithfully reproduced expressions.
3. Independently verified mathematics.
4. Newly derived calculations.
5. Tentative findings.
6. Scientifically reviewed conclusions.

Preserve failures and uncertainties in the research record.

## 7. Autonomous execution

Work continuously through the milestones using the available tools.

Do not stop after preparing documentation or a project plan.

Implement mathematics, execute tests, run experiments, investigate discrepancies, and record evidence.

At substantial milestones:

- Update `TODO.md`.
- Update the research log.
- Record outstanding questions.
- Commit completed work.
- Identify the next testable question.

Do not request approval for ordinary technical decisions.

For unresolved mathematical ambiguities, document competing interpretations and investigate them independently where feasible.

Do not consume the entire computational budget before establishing a trustworthy mathematical baseline.

Avoid circular investigation and repeated experiments without new information.

## 8. Success criteria

The initial research effort is successful when:

- The governing equations have been reconstructed.
- A minimal independent geometric implementation exists.
- Every applicable field-equation component has been audited.
- Conservation and analytic throat limits have been examined.
- Any claimed equation redundancy has been independently investigated.
- Published results have been reproduced or discrepancies documented.
- Significant findings have independent verification.
- A bounded parameter campaign has been completed where mathematically justified.
- Numerical tolerances and uncertainty are documented.
- All evidence is reproducible from the repository.
- Potential novelty has been assessed against existing literature.
- A clear recommendation exists on whether further research or manuscript preparation is justified.

Success does not require a positive finding or a publication.

## 9. Immediate instructions

Begin by reading the full manuscript:

https://arxiv.org/abs/2406.08250

Inspect the repository `mozrin/wormcheck` and preserve existing work.

Then:

1. Establish source provenance.
2. Extract the mathematical model.
3. Identify all independent field equations.
4. Implement the metric and required geometric quantities.
5. Independently derive the governing equation components.
6. Construct symbolic and numerical residual checks.
7. Investigate conservation identities, throat limits, and claimed equation redundancy.
8. Determine whether the published expressions satisfy the stated model.
9. Only then expand into reproduction and parameter exploration, subject to the consistency decision.

**Your first priority is a minimal independently executable model with field-equation residual checks. Expand reproduction, documentation, and exploration around that verified foundation.**

Proceed with actual computation and scientific verification, not merely planning.

The purpose of WormCheck is to discover what the mathematics actually supports—whether or not it agrees with the original authors' conclusions.