"""Execute analytical residual asymptotics and the residual Bianchi identity."""
import json
import sympy as s
from wormcheck import PublishedModel

model = PublishedModel()
r,r0,beta,critical,omega=model.symbols
radial=model.residuals['radial']
angular=model.residuals['angular']
dphi=s.diff(model.phi,r)
identity=s.factor(s.diff(radial,r)+dphi*radial+2*(radial-angular)/r)
assert identity==0
# Factor to rational form before limits; no numerical parameter substitution.
limits={name:str(s.simplify(s.limit(s.factor(r**2*expression),r,s.oo)))
        for name,expression in [('radial',radial),('angular',angular)]}
print(json.dumps({'source':'arXiv:2406.08250v1','assumptions':'r0>0, critical>0 finite, beta>=0, omega != -1; asymptotic mathematical limit',
 'residual_bianchi_identity':str(identity), 'scaled_limits':limits,
 'consequence':'For omega=3, scaled radial and angular residuals tend to 6 and 9. These rational residuals cannot vanish identically on any open radial interval. No physical large-radius validity is assumed.'},indent=2))
