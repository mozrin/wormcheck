# Research log

## 2026-11-11 — Acquisition checkpoint

Created owner-approved Workcheck Project 8 and verified repository association in both directions. Issue #1 tracks source reconstruction and initial audit. Downloaded arXiv v1 PDF and HTML; hashes are in references/source-manifest.json. Full reading, journal comparison, independent derivation and numerical experiments are pending. No scientific findings established. Host SymPy absent; use isolated Docker dependencies.

## Initial symbolic audit

Executed experiments/consistency_audit.py and experiments/derive_geometry.py in an isolated Python container. Density and conservation residuals simplify to zero. Radial and angular residuals are nonzero at r=1.001, 1.1 and 2 for r0=1, beta=0.01, critical density=0.005, omega=3. Independent Christoffel-to-Ricci-to-Einstein derivation agrees with implemented geometric components exactly, including both angular components. This supports investigating a consistency discrepancy in arXiv v1; journal comparison, normalized residuals, tests and independent source transcription remain pending. Evidence: results/manifests/initial-audit.json. No novelty or final error claim.

## Package and source check

Added PublishedModel symbolic package and three tests; all pass in the isolated container. Tests check density/conservation, throat normalization, necessary throat pressure constraint, and nonzero sampled residuals. ArXiv main.tex confirms the implemented shape/redshift expressions. Journal full-text access returned 403; cannot transfer the finding to the journal version yet. See docs/independent-derivation.md.
