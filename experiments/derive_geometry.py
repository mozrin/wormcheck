"""Execute to derive mixed Einstein components directly from the metric."""
import sympy as s

t,r,theta,varphi=s.symbols('t r theta varphi',real=True)
x=[t,r,theta,varphi]
b=s.Function('b')(r)
phi=s.Function('Phi')(r)
g=s.diag(-s.exp(2*phi),1/(1-b/r),r**2,r**2*s.sin(theta)**2)
gi=g.inv()
connection={}
for a in range(4):
 for i in range(4):
  for j in range(4):
   connection[a,i,j]=s.simplify(sum(gi[a,d]*(s.diff(g[d,j],x[i])+s.diff(g[d,i],x[j])-s.diff(g[i,j],x[d]))/2 for d in range(4)))
ricci=s.zeros(4)
for i in range(4):
 for j in range(4):
  ricci[i,j]=s.simplify(sum(s.diff(connection[a,i,j],x[a])-s.diff(connection[a,i,a],x[j])+sum(connection[a,a,d]*connection[d,i,j]-connection[a,j,d]*connection[d,i,a] for d in range(4)) for a in range(4)))
scalar=s.simplify(s.trace(gi*ricci))
einstein=s.simplify(gi*ricci-s.eye(4)*scalar/2)
expected=[-s.diff(b,r)/r**2,
 -b/r**3+2*(r-b)*s.diff(phi,r)/r**2,
 (1-b/r)*(s.diff(phi,r,2)+s.diff(phi,r)**2+s.diff(phi,r)/r)+(b-r*s.diff(b,r))*s.diff(phi,r)/(2*r**2)+(b-r*s.diff(b,r))/(2*r**3)]
for i,name in enumerate(['temporal','radial','angular']):
 difference=s.simplify(einstein[i,i]-expected[i])
 print(name, 'derived:',einstein[i,i], 'difference:',difference)
 assert difference==0
assert s.simplify(einstein[3,3]-einstein[2,2])==0
print('All metric-derived diagonal components agree with the implemented geometric formulas.')
