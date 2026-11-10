"""Execute equation 30/31 derivative, symbolic integral and quadrature checks."""
import json
import sympy as s
import mpmath as m
from wormcheck import PublishedModel

model=PublishedModel()
r,r0,beta,critical,omega=model.symbols
k=s.pi**2/720
integrand=4*s.pi*r**2*(model.rhoe+model.pe).subs(omega,3)
published_primitive=(16*k*s.pi/r+56*k*s.pi*beta/(9*r**3)
 +32*k*k*s.pi/(5*r**5*critical)+272*k*k*s.pi*beta/(21*r**7*critical)
 +560*k*k*s.pi*beta**2/(81*r**9*critical))
derived=s.integrate(s.expand(integrand),r)
defect=s.factor(s.diff(published_primitive,r)-integrand)
assert s.simplify(s.diff(derived,r)-integrand)==0
assert defect!=0
parameters={r0:1,beta:s.Rational(1,100),critical:s.Rational(5,1000)}
R=s.Rational(11,10)
published=(published_primitive.subs(r,R)-published_primitive.subs(r,r0)).subs(parameters)
independent=(derived.subs(r,R)-derived.subs(r,r0)).subs(parameters)
m.mp.dps=60
# Independent numeric integrand starts with original matter definitions.
knum=m.pi**2/720
rho=lambda x:-knum/x**4*(1+m.mpf(5)*m.mpf('0.01')/(3*x*x))
f=lambda x:4*m.pi*x*x*(4*rho(x)-8*rho(x)**2/m.mpf('0.005'))
quad=m.quad(f,[1,m.mpf('1.1')])
assert abs(quad-m.mpf(str(independent.evalf(60))))<m.mpf('1e-55')
print(json.dumps({'source':'arXiv:2406.08250v1 equations 30–31',
 'published_primitive':str(published_primitive),'independently_integrated_primitive':str(derived),
 'derivative_defect':str(defect),'parameters':{'r0':1,'R':'1.1','beta':'0.01','critical':'0.005','omega':3},
 'published_integral':str(published.evalf(60)),'symbolic_integral':str(independent.evalf(60)),
 'quadrature':str(quad),'quadrature_absolute_error':str(abs(quad-m.mpf(str(independent.evalf(60))))),
 'interpretation':'Arithmetic check of prescribed integrand; not a physical exotic-matter validation of the inconsistent geometry.'},indent=2))
