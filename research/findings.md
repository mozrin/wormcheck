# Research log

## 2026-11-11 — Acquisition checkpoint

Created owner-approved Workcheck Project 8 and verified repository association in both directions. Issue #1 tracks source reconstruction and initial audit. Downloaded arXiv v1 PDF and HTML; hashes are in references/source-manifest.json. Full reading, journal comparison, independent derivation and numerical experiments are pending. No scientific findings established. Host SymPy absent; use isolated Docker dependencies.

## Initial symbolic audit

Executed experiments/consistency_audit.py and experiments/derive_geometry.py in an isolated Python container. Density and conservation residuals simplify to zero. Radial and angular residuals are nonzero at r=1.001, 1.1 and 2 for r0=1, beta=0.01, critical density=0.005, omega=3. Independent Christoffel-to-Ricci-to-Einstein derivation agrees with implemented geometric components exactly, including both angular components. This supports investigating a consistency discrepancy in arXiv v1; journal comparison, normalized residuals, tests and independent source transcription remain pending. Evidence: results/manifests/initial-audit.json. No novelty or final error claim.

## Package and source check

Added PublishedModel symbolic package and three tests; all pass in the isolated container. Tests check density/conservation, throat normalization, necessary throat pressure constraint, and nonzero sampled residuals. ArXiv main.tex confirms the implemented shape/redshift expressions. Journal full-text access returned 403; cannot transfer the finding to the journal version yet. See docs/independent-derivation.md.

## Analytical pressure obstruction

Exact asymptotic coefficients are 8*omega/(1+omega) and 16*omega^2/(1+omega)^2. They preclude vanishing rational residuals on an open interval for omega!=0,-1 at fixed positive finite critical density. Residual Bianchi identity holds but does not force pressure residuals to zero. Branch B recorded for arXiv v1 strict Casimir case; see research/consistency-audit.md. Five tests pass. Journal correspondence and novelty remain unresolved.

## Independent numerical confirmation and inventory

Separate mpmath transcription and numerical differentiation agree with symbolic pressure residuals at four radii, at 30/60/100 digits. Normalized radial residual at r=1.1 is approximately 1.32068 using max(|lhs|,|rhs|,1/r^2). Density/conservation are within precision-scaled tolerance. Added mathematical source blocks and preliminary literature log; inventory is not yet complete at individual-symbol and equation-dependency level.

## VIQ arithmetic audit

Equation 31 does not differentiate to equation 30 integrand for beta>0. Three beta-dependent antiderivative coefficients differ from direct integration (80/9, 320/21, 800/81 in k/pi factors). Independent quadrature agrees with direct integration to <1e-55 for the documented sample. Original expression preserved in experiments/integral_audit.py. Added assumptions ledger. Journal correspondence remains unresolved.
