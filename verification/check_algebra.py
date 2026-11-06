"""Finite independent checks of the algebra decoder and exact finite-cell tangent.

Matrix exponentials and Frechet derivatives test the analytic construction;
these finite examples do not prove its universal claims.
"""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm, expm_frechet

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)


def vec(a):
    return a.reshape(-1, order="F")


def commutator(g):
    eye = np.eye(len(g))
    return -1j * (np.kron(eye, g) - np.kron(g.T, eye))


def dissipator(jumps):
    d = len(jumps[0])
    eye = np.eye(d)
    out = np.zeros((d*d, d*d), complex)
    for l in jumps:
        l2 = l @ l
        out += np.kron(l.conj(), l) - (np.kron(eye, l2) + np.kron(l2.T, eye))/2
    return out


def code_decoder(g, basis):
    d = len(g)
    # Orthogonal projection uses a least-squares basis, without assuming that
    # the supplied algebra basis is normalized.
    matrix = np.column_stack([vec(a) for a in basis])
    q = g - (matrix @ np.linalg.lstsq(matrix, vec(g), rcond=None)[0]).reshape((d,d), order="F")
    q = (q + q.conj().T)/2
    vals, vectors = np.linalg.eigh(q)
    positive = np.flatnonzero(vals > 1e-10)
    negative = np.flatnonzero(vals < -1e-10)
    s = vals[positive].sum()
    assert s > 0 and abs(s + vals[negative].sum()) < 1e-10
    anc = len(positive) + len(negative)
    v = np.zeros((d*anc, 2), complex)
    for a, (j, bit) in enumerate([(j,0) for j in positive] + [(j,1) for j in negative]):
        v[:,bit] += np.sqrt(abs(vals[j])/s)*np.kron(vectors[:,j], np.eye(anc)[:,a])
    errors = [np.kron(a, np.eye(anc)) @ v for a in basis]
    gram = np.empty((len(basis),len(basis)), complex)
    kl = 0.0
    for j, ej in enumerate(errors):
        for k, ek in enumerate(errors):
            block = ej.conj().T @ ek
            gram[j,k] = np.trace(block)/2
            kl = max(kl, np.linalg.norm(block-gram[j,k]*I))
    lam, u = np.linalg.eigh((gram+gram.conj().T)/2)
    w = [sum(errors[j]*u[j,k] for j in range(len(errors)))/np.sqrt(lam[k])
         for k in range(len(lam)) if lam[k] > 1e-10]
    perr = sum(wa @ wa.conj().T for wa in w)
    complement = np.eye(d*anc)-perr
    assert np.linalg.norm(v.conj().T@v-I) < 1e-10
    assert np.linalg.eigvalsh(complement)[0] > -1e-10
    for j, wa in enumerate(w):
        for k, wb in enumerate(w):
            assert np.linalg.norm(wa.conj().T@wb-(I if j==k else 0)) < 1e-10

    def decode(rho):
        result = sum(wa.conj().T@rho@wa for wa in w)
        result[0,0] += np.trace(complement@rho)
        return result

    def corrected(superop):
        out = np.zeros((4,4), complex)
        for col in range(4):
            unit = np.eye(4)[:,col].reshape((2,2), order="F")
            state = (v@unit@v.conj().T).reshape((d,anc,d,anc))
            result = np.zeros_like(state)
            for a in range(anc):
                for b in range(anc):
                    result[:,a,:,b] = (superop@vec(state[:,a,:,b])).reshape((d,d), order="F")
            out[:,col] = vec(decode(result.reshape((d*anc,d*anc))))
        return out
    return q, s, v, corrected, kl, anc


cases = [
    ("noncommuting_M2_tensor_I", np.kron(I,Z)+.35*np.kron(Y,X)+.1*np.kron(X,I),
     [np.kron(a,I) for a in [I,X,Y,Z]], [np.kron(X,I),np.kron(Z,I)],
     [(0.,0.),(.2,.9),(1.3,.5)]),
    ("diagonal_qutrit_algebra", np.array([[.2,1,.3j],[1,-.1,.7],[-.3j,.7,-.1]],complex),
     [np.diag(np.eye(3)[j]).astype(complex) for j in range(3)],
     [np.diag([-1.,0.,1.])], [(0.,),(.4,),(1.3,)])
]
rows=[]
for name,g,basis,directions,ratesets in cases:
    q,s,v,corrected,kl,anc=code_decoder(g,basis)
    d=len(g); qgap=float(np.trace(q@q).real/s)
    for rates in ratesets:
        jumps=[np.sqrt(rate)*f for rate,f in zip(rates,directions)]
        D=dissipator(jumps)
        M=2*sum(float(np.linalg.norm(l,2)**2) for l in jumps)
        for tau in [.07,.4,1.3]:
            E,dE=expm_frechet(tau*D,tau*commutator(g))
            aug=np.zeros((d*d+1,d*d+1),complex)
            aug[:d*d,:d*d]=D
            aug[:d*d,-1]=vec(g)
            B=expm(tau*aug)[:d*d,-1].reshape((d,d),order="F")
            HL=v.conj().T@np.kron(B,np.eye(anc))@v
            null_error=float(np.linalg.norm(corrected(E)-np.eye(4)))
            tangent_error=float(np.linalg.norm(corrected(dE)-commutator(HL)))
            gap=float((HL[0,0]-HL[1,1]).real)
            lower=qgap*(tau if M==0 else -np.expm1(-M*tau)/M)
            assert null_error < 1e-10 and tangent_error < 1e-10
            assert lower-1e-10 <= gap <= qgap*tau+1e-10
            rows.append(dict(model=name,rates=list(rates),tau=tau,ancilla_dimension=anc,
                             kl_error=float(kl),null_error=null_error,tangent_error=tangent_error,
                             logical_gap=gap,proved_gap_lower=float(lower)))

l=np.array([-3.,-1.,1.,3.]); g=l**3
span=np.column_stack([np.ones(4),l,l*l])
residual=float(np.linalg.norm(g-span@np.linalg.lstsq(span,g,rcond=None)[0]))
assert residual>1
gaussian=[]
for tau in [.01,.2,1.,4.]:
    R=np.exp(-tau*(l[:,None]-l[None,:])**2/2)
    smallest=float(np.linalg.eigvalsh(R)[0]);assert smallest>0
    gaussian.append(dict(tau=tau,minimum_eigenvalue=smallest))
result=dict(kind="Finite numerical checks, not a universal proof",cases=len(rows),
            maximum_kl_error=max(r['kl_error'] for r in rows),
            maximum_null_error=max(r['null_error'] for r in rows),
            maximum_tangent_error=max(r['tangent_error'] for r in rows),
            minimum_logical_gap=min(r['logical_gap'] for r in rows),
            four_level_hnls_residual=residual,gaussian_checks=gaussian,rows=rows)
out=Path(__file__).parent/'results'/'algebra_checks.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','gaussian_checks']},indent=2))
