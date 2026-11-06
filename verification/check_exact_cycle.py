"""Independent density-matrix check of the recovered logical channel and sign margin."""
import json
import numpy as np
from scipy.linalg import expm
from pathlib import Path
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Z=np.diag([1,-1]).astype(complex)
XS=np.kron(X,I); ZS=np.kron(Z,I)
P0=np.diag([1,0,0,1]).astype(complex); P1=np.eye(4)-P0
R0=P0; R1=XS@P1
ket=np.array([1,0,0,1],complex)/np.sqrt(2)
rho=np.outer(ket,ket.conj())
def fclosed(delta,gamma,tau):
 if gamma==0: return np.exp(-1j*delta*tau)
 k=np.sqrt(complex(gamma*gamma-delta*delta))
 sinh_over_k=tau if abs(k)<1e-13 else np.sinh(k*tau)/k
 return np.exp(-gamma*tau)*(np.cosh(k*tau)+(gamma-1j*delta)*sinh_over_k)
def physical(delta,gamma,tau):
 H=delta*ZS/2
 L=-1j*(np.kron(np.eye(4),H)-np.kron(H.T,np.eye(4)))+gamma*(np.kron(XS.conj(),XS)-np.eye(16))
 evolved=(expm(tau*L)@rho.reshape(16,order="F")).reshape((4,4),order="F")
 rec=R0@evolved@R0.conj().T+R1@evolved@R1.conj().T
 return 2*rec[0,3]
checks=[]
for gamma in [0,.1,1,3]:
 for tau in [.1,.7,1.4]:
  for delta in [-2,-.3,0,.3,1,2]:
   target=fclosed(delta,gamma,tau); actual=physical(delta,gamma,tau)
   checks.append(abs(target-actual))
Gamma=1.; W=.05; tau=1.; beta=.25
amin=(1-np.exp(-2*Gamma*tau))/(2*Gamma)
smin=np.sin(beta*amin/(4*tau))
assert tau*W<=beta/2
assert beta*tau*W/2<=smin/2
margin=[]
for gamma in np.linspace(0,Gamma,31):
 for stage in range(20):
  w=W*(3/4)**stage; n=int(np.floor(beta/(tau*w)))
  for fraction in np.linspace(.5,1,21):
   delta=w*fraction
   mean=-np.imag(fclosed(delta,gamma,tau)**n)
   margin.append(mean)
assert max(checks)<1e-12
assert min(margin)>=smin/2-1e-12
result={"density_matrix_cases":len(checks),"maximum_complex_channel_discrepancy":float(max(checks)),"sign_margin_cases":len(margin),"minimum_computed_positive_mean":float(min(margin)),"proved_uniform_lower_margin":float(smin/2),"Gamma":Gamma,"tau":tau,"W":W,"scope":"Finite numerical cross-check; proof establishes universal statement independently."}
(Path(__file__).parent / "results" / "exact_cycle_results.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
