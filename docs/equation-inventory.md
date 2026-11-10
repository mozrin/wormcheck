# Equation inventory — arXiv v1

Source: https://arxiv.org/src/2406.08250v1. Mathematical expressions extracted from main.tex; source hashes in references/source-manifest.json. This preserves notation, including suspected sign/normalization issues. The blocks are source-order blocks, **not equation numbers**: align/eqnarray blocks contain several numbered equations. The independently checked numbering map below is authoritative where given.

## Numbering and verification map

Equations 1–6: matter prescription, effective field equation, isotropic tensor, effective density/pressure, metric. Assumptions: G=c=hbar=1; signature (-,+,+,+), static spherical geometry. These are prescribed model inputs, not derived quantum-gravity results.

Equations 7–9: density, radial and angular equations. Metric-derived geometric components verified. Density identity holds; pressure equations fail for the tested construction. Equation 7 tensor label has the temporal sign issue discussed in the audit.

Equation 10: isotropic effective conservation, verified symbolically. Equation 11: shape, verified by differentiation and throat value. Equation 12: embedding integral, not verified; lower limit 0 lies outside r>=r0. Equation 13: lapse, verified against conservation, normalized at throat.

Equations 14–18: isotropic energy-condition inequalities; no dynamical content. Equation 19: effective dp/density diagnostic, not a perturbative stability theorem. Equations 20–29: shell geometry, stresses and matching, not independently verified. Equations 30–31: VIQ definition and evaluation, pending independent differentiation/integration checks.

## Shared symbol and domain ledger

r is areal radius; r0>0 throat; R>r0 matching radius; M exterior Schwarzschild parameter; beta>=0 GUP coefficient; critical density rho_c>0; omega constant with strict Casimir omega=3. rho,p are prescribed original matter; rho_e,p_e effective matter. b has length units, Phi is dimensionless; beta/r^2 and rho/rho_c must be dimensionless. The simultaneous Planck-unit normalization masks gravitational conversion factors: a restored-unit audit remains outstanding. Phi expression excludes omega=-1. Domains of shell square roots require separate checking; do not infer them from source plots.

## Original mathematical blocks

### Source block 1

```latex
\begin{equation}\label{casimirdenspress}
    \rho(r) = -\frac{k}{r^4}\left(1+\frac{5\beta}{3r^2}\right) \quad \text{and} \quad p(r) = \omega \rho(r),
\end{equation}
```

### Source block 2

```latex
\begin{eqnarray}
    G^{\mu}_{\ \nu} \equiv R^{\mu}_{\ \nu} - \frac{1}{2} g^{\mu}_{\ \nu} R = 8 \pi T^{\mu}_{\ \nu} ,
\end{eqnarray}
```

### Source block 3

```latex
\begin{eqnarray}
    T^{\mu}_{\ \nu} = \text{diag}\left(-\rho_{e}, p_{e}, p_{e}, p_{e} \right),
    \label{en_mo_tensor}
\label{energy_tensor}
\end{eqnarray}
```

### Source block 4

```latex
\begin{eqnarray}
\rho_e(r) &=& \rho\left(1-\frac{\rho}{\rho_c}\right),\label{rhoeff}\\
p_e(r)&=& p-\rho\left(\frac{2p+\rho}{\rho_c}\right),\label{peff}
\label{edensity}
\end{eqnarray}
```

### Source block 5

```latex
\begin{equation}\label{metric1}
    ds^2=-e^{2\Phi(r)}dt^2+\frac{dr^2}{1-\frac{b(r)}{r}}+r^2d\Omega_2,
\end{equation}
```

### Source block 6

```latex
\begin{align}
G_{\ t}^{t} = & \frac{b'}{r^{2}}= 8 \pi \rho_e(r),\label{eq:g00}\\
G_{\ r}^{r} = & -\frac{b}{r^{3}}+ 2\frac{\left(r-b\right)\Phi'}{r^{2}}=  8 \pi p_e(r),\label{eq:grr}\\
G_{\theta}^{\theta} = & G_{\phi}^{\phi} = \left(1-\frac{b}{r}\right)\left[\Phi''+(\Phi')^{2}+\frac{\left(b-rb'\right)}{2r(r-b)}\Phi'+\frac{\left(b-rb'\right)}{2r^2(r-b)}+\frac{\Phi'}{r}\right]=  8 \pi  p_{e}(r),\label{eq:gthetatheta}
\end{align}
```

### Source block 7

```latex
\begin{equation}\label{TOV}
    -\frac{dp_e}{dr}-\Phi'(\rho_e+p_e)=0,
\end{equation}
```

### Source block 8

```latex
\begin{eqnarray}
    b(r)=r_0&-&\frac{8 \pi  k}{ r_0}\left(1+\frac{5\beta }{9 r_0^2}+\frac{ k}{5 \rho_c r_0^4}+\frac{10 k \beta }{21\rho_c r_0^6}+\frac{ 25 k\beta^2 }{81 \rho_c r_0^8}\right)\nonumber\\
    &+&\frac{8 \pi  k}{r}\left(1+\frac{5\beta }{9 r^2}+\frac{ k}{5 \rho_c r^4}+\frac{10 k \beta }{21\rho_c r^6}+\frac{ 25 k\beta^2 }{81 \rho_c r^8}\right).
    \label{b(r)}
\end{eqnarray}
```

### Source block 9

```latex
\begin{equation}
   dr^2+r^2d\phi^2+dz^2=\frac{dr^2}{1-\frac{b(r)}{r}}+r^2d\phi^2\Rightarrow z(r)=\int_0^{r}\left[\frac{b(u)/u}{1-b(u)/u}\right]^{1/2}du.
\end{equation}
```

### Source block 10

```latex
\begin{equation}
   -g_{tt}(r)= e^{2\Phi(r)}=\left(\frac{r}{r_0}\right)^{\frac{12(1+2\omega)}{1+\omega}}\left(\frac{5\beta+3r_0^2}{5\beta+3r^2}\right)^{\frac{2\omega}{1+\omega}}\left(\frac{10\beta k+6k r_0^2+3\rho_cr_0^6}{10\beta k+6k r^2+3\rho_cr^6}\right)^2,\label{redshifteq}
\end{equation}
```

### Source block 11

```latex
\begin{eqnarray}
        \rho_e + p_e \geq 0.
    \end{eqnarray}
```

### Source block 12

```latex
\begin{eqnarray}
        \rho_e &\geq& 0, \\
        \rho_e + p_e &\geq& 0
    \end{eqnarray}
```

### Source block 13

```latex
\begin{eqnarray}
        \rho_e + 3 p_e &\geq& 0, \\
        \rho_e + p_e &\geq& 0
    \end{eqnarray}
```

### Source block 14

```latex
\begin{equation}
  \label{vsound}
    (v_s)^2=\frac{d p_e}{d\rho_e}=\frac{d p_e/dr}{d\rho_e/dr}.
\end{equation}
```

### Source block 15

```latex
\begin{equation}
    {S^i}_j=-{\kappa^i}_j+{\delta^i}_j\kappa^k_k,
\end{equation}
```

### Source block 16

```latex
\begin{equation}
    \kappa_{ij}=\kappa_{ij}^+-\kappa_{ij}^-.
\end{equation}
```

### Source block 17

```latex
\begin{equation}
    \kappa_{ij}^\pm=- n_\nu^\pm\left.\left[\frac{\partial^2 X_\nu}{\partial\xi^i\partial\xi^j}+\Gamma^\nu_{\alpha\beta}\frac{\partial X^\alpha}{\partial\xi^i}\frac{\partial X^\beta}{\partial\xi^j}\right]\right|_S,
\end{equation}
```

### Source block 18

```latex
\begin{equation}
    n_\nu^\pm=\pm \left|g^{\alpha\beta }\frac{\partial f}{\partial X^\alpha}\frac{\partial f}{\partial X^\beta}\right|^{-1/2}\frac{\partial f}{\partial X^\nu},
\end{equation}
```

### Source block 19

```latex
\begin{equation}
    {S^i}_j = \text{diag}\left(-\Sigma,  \mathcal{P},  \mathcal{P}, \mathcal{P} \right),\label{Intrisic_SET}
\end{equation}
```

### Source block 20

```latex
\begin{eqnarray}
    &&\Sigma = -\frac{2}{R}\left(\sqrt{1-\frac{2M}{R}}-\sqrt{1-\frac{b(R)}{R}} \right),\label{surface_energy}\\
    &&\mathcal{P}= \frac{1}{R}\left[ \frac{1-\frac{M}{R}}{\sqrt{1-\frac{2M}{R}}}-\left(1+R\Phi'(R)\right)\sqrt{1-\frac{b(R)}{R}}\right],\label{surface_tension}
\end{eqnarray}
```

### Source block 21

```latex
\begin{equation}\label{derivativePhi}
    \Phi^{'}(R)=\frac{6 \left(5 \beta+2 R^2\right) \left[2 k (2 \omega+1) \left(5 \beta+3 R^2\right)+3 \rho_c R^6 \omega\right]}{R (\omega+1) \left(5 \beta+3 R^2\right) \left(10 k \beta+6 k R^2+3\rho_c R^6\right)}.
\end{equation}
```

### Source block 22

```latex
\begin{eqnarray}
    && \sqrt{1-\frac{2M}{R}}=\sqrt{1-\frac{b(R)}{R}},\label{cond_1}\\
    && \frac{1-\frac{M}{R}}{\sqrt{1-\frac{2M}{R}}}=\left(1+R\Phi'(R)\right)\sqrt{1-\frac{b(R)}{R}}.\label{cond_2}
\end{eqnarray}
```

### Source block 23

```latex
\begin{equation}\label{viq}
\mathcal{I}_v=\int_{r_0}^R 4\pi r^2 (\rho_e+p_e)dr,
\end{equation}
```

### Source block 24

```latex
\begin{align}
&\mathcal{I}_v=\frac{16 k \pi}{R} - \frac{16 k \pi}{r_0} + \frac{56 k \pi \beta}{9 R^3} - \frac{56 k \pi \beta}{9 r_0^3} + \frac{32 k^2 \pi}{5 R^5 \rho_c} - \frac{32 k^2 \pi}{5 r_0^5 \rho_c} \nonumber\\
&+ \frac{272 k^2 \pi \beta}{21 R^7 \rho_c} - \frac{272 k^2 \pi \beta}{21 r_0^7 \rho_c} + \frac{560 k^2 \pi \beta^2}{81 R^9 \rho_c} - \frac{560 k^2 \pi \beta^2}{81 r_0^9 \rho_c},
\end{align}
```
