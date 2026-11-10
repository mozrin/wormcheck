"""Symbolic implementation of arXiv v1 equations 1, 4, 5, 11 and 13."""
import sympy as s


class PublishedModel:
    """Construct published expressions and component residuals.

    Conventions: signature (-,+,+,+), G=c=hbar=1. The redshift expression
    requires omega != -1. Positive r, r0, critical and beta are assumed.
    Geometric temporal density uses -G^t_t; radial/angular use G^i_i.
    """

    def __init__(self):
        """Build exact symbolic expressions without numerical substitution."""
        r, r0, beta, critical = s.symbols('r r0 beta critical', positive=True)
        omega = s.symbols('omega', real=True)
        k = s.pi**2 / 720
        rho = -k / r**4 * (1 + 5 * beta / (3 * r**2))
        rhoe = rho * (1 - rho / critical)
        pe = omega * rho - (2 * omega + 1) * rho**2 / critical
        primitive = 8*s.pi*k/r * (1 + 5*beta/(9*r**2) + k/(5*critical*r**4) + 10*k*beta/(21*critical*r**6) + 25*k*beta**2/(81*critical*r**8))
        b = r0 + primitive - primitive.subs(r, r0)
        phi = (6*(1+2*omega)/(1+omega)*s.log(r/r0)
               + omega/(1+omega)*s.log((5*beta+3*r0**2)/(5*beta+3*r**2))
               + s.log((10*beta*k+6*k*r0**2+3*critical*r0**6)/(10*beta*k+6*k*r**2+3*critical*r**6)))
        dphi = s.diff(phi,r)
        radial = -b/r**3 + 2*(r-b)*dphi/r**2 - 8*s.pi*pe
        angular_geometry = ((1-b/r)*(s.diff(phi,r,2)+dphi**2+dphi/r)
                            +(b-r*s.diff(b,r))*dphi/(2*r**2)
                            +(b-r*s.diff(b,r))/(2*r**3))
        residuals = {
         'density': s.factor(s.diff(b,r)/r**2-8*s.pi*rhoe),
         'conservation': s.factor(s.diff(pe,r)+dphi*(rhoe+pe)),
         'radial': radial,
         'angular': angular_geometry-8*s.pi*pe,
        }
        self.symbols = (r, r0, beta, critical, omega)
        self.b, self.phi, self.rhoe, self.pe = b, phi, rhoe, pe
        self.residuals = residuals
