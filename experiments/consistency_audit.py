"""Initial symbolic audit of arXiv:2406.08250v1, equations 1–13.

Execute in the isolated research container. Geometric components here are
transcribed from equations 7–9; an independent tensor derivation is pending.
"""
import json
import sympy as s

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
parameters = {r0:1,beta:s.Rational(1,100),critical:s.Rational(5,1000),omega:3}
report = {'source':'arXiv:2406.08250v1',
          'verification_scope':'Published components only; independent tensor derivation pending',
          'parameters':{'r0':1,'beta':'0.01','critical':'0.005','omega':3},
          'symbolic_density':str(residuals['density']),
          'symbolic_conservation':str(residuals['conservation']),
          'throat_radial':str(s.factor(radial.subs(r,r0))),
          'samples':[]}
for radius in [s.Rational(1001,1000),s.Rational(11,10),s.Integer(2)]:
 report['samples'].append({'r':str(radius),'residuals':{
  name:str(expression.subs(parameters).subs(r,radius).evalf(50))
  for name,expression in residuals.items()}})
print(json.dumps(report,indent=2))
