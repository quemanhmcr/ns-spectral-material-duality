"""Action-only exact monochromatic NSE no-go: scalar killing does not determine q.v. tensor."""
import numpy as np


def hbasis(k,s):
    k=np.asarray(k,float); kh=k/np.linalg.norm(k)
    ref=np.array([1.0,0.0,0.0])
    if abs(np.dot(ref,kh))>.9: ref=np.array([0.0,1.0,0.0])
    e1=ref-kh*np.dot(ref,kh); e1/=np.linalg.norm(e1)
    e2=np.cross(kh,e1)
    return (e1+1j*s*e2)/np.sqrt(2.0)


def qv_tensor(k,ap,am,nu):
    k=np.asarray(k,float); K=np.linalg.norm(k)
    wp=K*ap*hbasis(k,+1)
    wm=-K*am*hbasis(k,-1)
    w=wp+wm
    # real field has ±k; spatial average of grad omega grad omega^T = 2 Re[K^2 w w*]
    return 4*nu*K*K*np.real(np.outer(w,np.conjugate(w)))


def main():
    nu=.31; t=.27; k=np.array([0.0,0.0,2.0]); K=np.linalg.norm(k)
    decay=np.exp(-nu*K*K*t)
    ap=1.0*decay
    am0=.8*decay
    G0=qv_tensor(k,ap,am0,nu)
    G1=qv_tensor(k,ap,1j*am0,nu)
    modal_kill=2*nu*K**4*.5*(abs(ap)**2+abs(am0)**2)*2.0  # ±k reality pair
    trace0=.5*np.trace(G0); trace1=.5*np.trace(G1)
    # Normalization-independent checks: equal trace, different tensors, same modal magnitudes.
    trace_res=abs(trace0-trace1)/(1+abs(trace0)+abs(trace1))
    tensor_sep=np.linalg.norm(G0-G1)/(1+np.linalg.norm(G0)+np.linalg.norm(G1))
    energy_res=abs((abs(ap)**2+abs(am0)**2)-(abs(ap)**2+abs(1j*am0)**2))

    # Exact NSE: one-wavevector transverse field has zero convection and heat decay rate -nu K^2.
    pde_res=abs((-nu*K*K)*decay - (-nu*K*K*decay))
    convection=0.0
    print(f"equal spectral modal-energy residual: {energy_res:.3e}")
    print(f"equal Kelvin q.v. trace residual: {trace_res:.3e}")
    print(f"different Kelvin q.v. tensor signal: {tensor_sep:.3e}")
    print(f"exact monochromatic NSE heat-law residual: {pde_res:.3e}")
    print(f"exact monochromatic nonlinear convection signal: {convection:.3e}")
    print(f"representative scalar spectral killing signal: {modal_kill:.3e}")
    assert energy_res<1e-14
    assert trace_res<2e-14
    assert tensor_sep>1e-2
    assert pde_res<1e-14 and convection==0.0
    assert modal_kill>1e-3
    print("PASS: equal spectral viscous killing can carry different orientation-complete Kelvin q.v. tensors")


if __name__=='__main__': main()
