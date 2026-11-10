# WormCheck

Independent audit of Muniz et al., arXiv:2406.08250v1,
DOI 10.1016/j.dark.2024.101673. Work in progress; no human scientific review.

The initial implementation preserves the published model. Its density and
conservation equations hold symbolically, but sampled radial/angular residuals
are nonzero. This is preliminary arXiv-version evidence; journal comparison
and full independent verification remain outstanding.

Install Python >=3.11 and `pip install -e '.[test]'` in an isolated environment.
Run `python -m pytest`, `python experiments/consistency_audit.py`, and
`python experiments/derive_geometry.py`. Research dependencies are recorded in
results/manifests/environment.txt. Full scope: research/directive.md and amendments.md.

Project: https://github.com/users/mozrin/projects/8; active investigation: issue #1.
