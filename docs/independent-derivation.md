# Initial independent geometry derivation

Execute experiments/derive_geometry.py. Starting with the diagonal metric,
it computes the Levi-Civita connection, Ricci tensor, scalar and mixed Einstein
tensor. The Ricci convention is R_ij = partial_a Gamma^a_ij - partial_j Gamma^a_ia
+ Gamma^a_ad Gamma^d_ij - Gamma^a_jd Gamma^d_ia.
The temporal component is -b'/r^2 (the paper's positive density equation uses
-G^t_t). Radial and angular components agree with the implemented formulas.
Both angular components agree. This checks geometry independently of their
transcription; it does not independently verify the prescribed matter model.

For the published analytic redshift, Phi' is finite at r0>0 for positive
critical density, beta>=0 and omega!=-1. Thus the radial Einstein equation
at the throat requires -1/r0^2=8*pi*p_e(r0). Conservation does not by itself
impose this necessary constraint. Tests establish this relation symbolically.
No claim of a complete no-go theorem is made here.
