# Consistency audit — arXiv v1

Status: analytically supported discrepancy, pending journal comparison and
external scientific review. No novelty claim.

## Tested construction

The metric, effective isotropic matter, b and Phi are the published equations
1–13, with the sign convention (-,+,+,+). Use -G^t_t for positive density-side
normalization; equation 7's label G^t_t has a sign mismatch with that convention.
Our discrepancy does not depend on that label: the density equation itself holds.

## Residual relation

Let E_r=G^r_r-8*pi*p_e and E_t=G^theta_theta-8*pi*p_e.
Since the density residual and effective matter conservation vanish, the
contracted Bianchi identity reduces to

    E_r' + Phi' E_r + 2(E_r-E_t)/r = 0.

This identity is verified symbolically. It relates the two pressure residuals;
it does not force either to vanish. The independent metric derivation confirms
the components used, and the arXiv TeX confirms the prescribed b and Phi.

## Analytical obstruction

For fixed positive finite critical density, beta>=0, r0>0, omega!=-1,
Phi' ~ a/r with a=4*omega/(1+omega); b tends to a finite constant and
p_e=O(r^-4). Therefore

    lim r^2 E_r = 2a = 8*omega/(1+omega)
    lim r^2 E_t = a^2 = 16*omega^2/(1+omega)^2.

SymPy independently evaluates these limits from the full expressions.
For omega=3 the limits are 6 and 9. For any nonzero omega in this domain,
the published expressions cannot be a solution on any open radial interval:
the residuals are rational analytic functions for r>0, and vanishing on an
open interval would make them identically zero. The nonzero asymptotic
coefficient contradicts that. This is an algebraic argument, not a claim
that the effective physics is trustworthy at infinity. Matching at finite R
does not repair the interior residual. omega=0 and omega=-1 require separate
analysis; no conclusion for them is established by these limits.

## Scope decision

Branch B for the strict Casimir construction in arXiv v1. Further reproduction
can characterize published expressions but cannot validate their interpretation
as the stated isotropic field-equation solution. Do not silently alter them.
Journal-version correspondence, independent matter transcription, numerical
normalization, full equation inventory and literature priority remain unresolved.

## VIQ expression check

For omega=3, the definition uses rho_e+p_e=4*rho-8*rho^2/rho_c.
Writing the antiderivative in powers of radius, direct integration gives

    F(r)=16*pi*k/r + 80*pi*k*beta/(9*r^3)
       +32*pi*k^2/(5*rho_c*r^5)
       +320*pi*k^2*beta/(21*rho_c*r^7)
       +800*pi*k^2*beta^2/(81*rho_c*r^9).

The definite integral is F(R)-F(r0). The published equation 31 instead uses
56, 272 and 560 for the three beta-dependent coefficients. Its derivative
defect is positive for beta>0, rho_c>0, r>0; it vanishes when beta=0.
Both formulas vanish at R=r0, so that boundary check alone cannot detect it.
For r0=1, R=1.1, beta=0.01, rho_c=0.005, the published expression is
-0.3572305217303575 while direct integration gives -0.3588500378477355.
Independent 60-digit quadrature agrees with direct symbolic integration.
See experiments/integral_audit.py and its machine-readable evidence.
