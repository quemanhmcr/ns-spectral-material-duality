"""Action-only exact NS shear referee for HH-TV blindness to Cartan activity."""
import numpy as np


def main():
    nu=.37; t=.29; a=1.4
    E=np.exp(-nu*t)
    pde=conv=sigS=sigO=0.0
    for y in np.linspace(-np.pi,np.pi,4001):
        U=a*E*np.sin(y); Ut=-nu*U; Uyy=-U
        pde=max(pde,abs(Ut-nu*Uyy))
        # h=(U(y),0,0): h dot grad = U partial_x, but h is x-independent.
        conv=max(conv,0.0)
        dU=a*E*np.cos(y)
        A=np.array([[0.0,dU,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
        S=.5*(A+A.T); O=.5*(A-A.T)
        sigS=max(sigS,np.linalg.norm(S)); sigO=max(sigO,np.linalg.norm(O))
    # Since B(h,h)=0 identically, every signed HH edge/work and its TV vanish.
    hh_tv=0.0
    print(f"worst exact periodic shear NSE residual: {pde:.3e}")
    print(f"worst nonlinear self-advection signal: {conv:.3e}")
    print(f"canonical HH total-variation signal: {hh_tv:.3e}")
    print(f"maximum unresolved strain signal: {sigS:.3e}")
    print(f"maximum unresolved connection signal: {sigO:.3e}")
    assert pde<2e-14
    assert conv==0.0 and hh_tv==0.0
    assert sigS>0.5 and sigO>0.5
    print("PASS: exact NSE can have zero HH transfer/TV with active unresolved strain and connection")


if __name__=='__main__': main()
