"""Execute independent mpmath transcription and numerical differentiation.

No SymPy expressions or derivatives are imported. A second transcription of
the source expressions checks implementation; shared source assumptions remain.
"""
import json
import mpmath as m

rows=[]
for digits in [30,60,100]:
 m.mp.dps=digits
 k=m.pi**2/720
 beta=m.mpf('0.01'); critical=m.mpf('0.005'); throat=m.mpf(1); omega=m.mpf(3)
 rho=lambda x:-k*x**-4*(1+5*beta/(3*x*x))
 density=lambda x:rho(x)*(1-rho(x)/critical)
 pressure=lambda x:omega*rho(x)-(2*omega+1)*rho(x)**2/critical
 primitive=lambda x:8*m.pi*k/x*(1+5*beta/(9*x*x)+k/(5*critical*x**4)+10*k*beta/(21*critical*x**6)+25*k*beta**2/(81*critical*x**8))
 shape=lambda x:throat+primitive(x)-primitive(throat)
 # Differentiate log of the original lapse product, not a symbolic Phi expression.
 lapse=lambda x:(x/throat)**(12*(1+2*omega)/(1+omega))*((5*beta+3*throat**2)/(5*beta+3*x*x))**(2*omega/(1+omega))*((10*beta*k+6*k*throat**2+3*critical*throat**6)/(10*beta*k+6*k*x*x+3*critical*x**6))**2
 phi=lambda x:m.log(lapse(x))/2
 for text in ['1.000001','1.001','1.1','2']:
  r=m.mpf(text); b=shape(r); bp=m.diff(shape,r); pp=m.diff(phi,r); ppp=m.diff(phi,r,2)
  lhs={'density':bp/r**2,'radial':-b/r**3+2*(r-b)*pp/r**2,
       'angular':(1-b/r)*(ppp+pp**2+pp/r)+(b-r*bp)*pp/(2*r*r)+(b-r*bp)/(2*r**3)}
  rhs={'density':8*m.pi*density(r),'radial':8*m.pi*pressure(r),'angular':8*m.pi*pressure(r)}
  conservation=m.diff(pressure,r)+pp*(density(r)+pressure(r))
  row={'digits':digits,'r':text,'conservation':str(conservation),'components':{}}
  for name in lhs:
   difference=lhs[name]-rhs[name]
   scale=max(abs(lhs[name]),abs(rhs[name]),1/r**2)
   row['components'][name]={'lhs':str(lhs[name]),'rhs':str(rhs[name]),'residual':str(difference),'absolute_residual':str(abs(difference)),'normalized_residual':str(abs(difference)/scale)}
  assert abs(lhs['density']-rhs['density']) < m.mpf(10)**(-digits+5)
  assert abs(conservation) < m.mpf(10)**(-digits+5)
  assert abs(lhs['radial']-rhs['radial'])>1
  rows.append(row)
print(json.dumps({'source':'arXiv:2406.08250v1','parameters':{'beta':'0.01','critical':'0.005','r0':'1','omega':'3'},'method':'independent mpmath transcription; numerical derivatives','normalization':'max(abs(lhs),abs(rhs),1/r^2); dimensionless in source Planck-unit convention','rows':rows},indent=2))
