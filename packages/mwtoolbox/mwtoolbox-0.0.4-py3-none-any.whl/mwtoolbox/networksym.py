#-*-coding:utf-8-*-
"""
Network Parameters
"""
import numpy as np
import sympy as sp
import operator as op
from functools import reduce

def ideal_nport(N):
    """
    S-parameters of ideal N-port junction with equal reference impedances at all ports
    """
    S = sp.ones(N,N)
    a=sp.Rational(2-N,N)
    b=sp.Rational(2,N)
    S=S*b
    for i in range(N):
        S[i,i]=a
    return S

def ideal_gyrator():
    """
    S-parameters of ideal gyrator
    """
    return sp.Matrix([[0,-1],[1,0]])

def ideal_coupled_line(Ze, Zo, Te, To, Z0):
    """
    S-parameters of ideal coupled line
    Te and To in radian
    3----------4
    1----------2
    """
    De=2*Ze*Z0*sp.cos(Te)+(Ze**2+Z0**2)*sp.sin(Te)*sp.I
    Do=2*Zo*Z0*sp.cos(To)+(Zo**2+Z0**2)*sp.sin(To)*sp.I
    Ye=Ze*Z0/De
    Yo=Zo*Z0/Do
    Xe=(Ze**2-Z0**2)*sp.sin(Te)*sp.I/2/De
    Xo=(Zo**2-Z0**2)*sp.sin(To)*sp.I/2/Do
    S = sp.ones(4,4)
    S[0,0]=S[1,1]=S[2,2]=S[3,3]=Xe+Xo
    S[0,1]=S[1,0]=S[2,3]=S[3,2]=Ye+Yo
    S[0,2]=S[2,0]=S[1,3]=S[3,1]=Xe-Xo
    S[0,3]=S[3,0]=S[1,2]=S[2,1]=Ye-Yo
    return S

def ideal_amp(G):
    """
    S-parameters of an ideal amplifier/isolator
    G is voltage gain, no reflection, infinite isolation
    """
    return sp.Matrix([[0, 0], [G, 0]])

def ideal_att(G):
    """
    S-parameters of an ideal amplifier/attenuator/isolator
    G is voltage gain (<1), no reflection
    """
    return sp.Matrix([[0, G], [G, 0]])

def circulator():
    """
    S-parameters of an ideal circulator (circulation direction 1⇒2⇒3)
    """
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

def shunt_z(Z):
    """
    ABCD parameters of shunt impedance
    """
    return sp.Matrix([[1, 0], [1/Z, 1]])

def series_z(Z):
    """
    ABCD parameters of series impedance
    """
    return sp.Matrix([[1, Z], [0, 1]])

def jinv(J):
    """
    ABCD parameters of J - inverter
    """
    return sp.Matrix([[0, sp.I/J], [sp.I * J, 0]])

def jinv_lumped(X):
    """
    ABCD parameters of J - inverter produced by 3 inductors in Tee form.
    """
    return CascadeNetworks([shZ( - X), seZ(X), shZ( - X)])

def kinv(K):
    """
    ABCD parameters of k - inverter
    """
    return sp.Matrix([[0,sp.I * K], [sp.I/K, 0]])

def tline(Zo, theta):
    """
    ABCD parameters of ideal transmission line,  theta = radian
    """
    return sp.Matrix([[sp.cos(theta), sp.I * Zo * sp.sin(theta)], [sp.I/Zo * sp.sin(theta), sp.cos(theta)]])

def tline_list(Zo, theta):
    """
    ABCD parameters of ideal transmission line,  theta = radian
    """
    return tuple([sp.cos(theta), sp.I * Zo * sp.sin(theta), sp.I/Zo * sp.sin(theta), sp.cos(theta)])

def transformer(N):
    """
    ABCD parameters of ideal transformer (1:N)
    """
    return sp.Matrix([[1/N, 0], [0, N]])

def t_network(Zs1, Zp, Zs2):
    """
    ABCD parameters of Tee network
    """
    return sp.Matrix([[1 + Zs1/Zp, Zs1 + Zs2 + Zs1 * Zs2/Zp], [1/Zp, 1 + Zs2/Zp]])

def pi_network(Zp1, Zs, Zp2):
    """
    ABCD parameters of Pi network
    """
    return sp.Matrix([[1 + Zs/Zp2, Zs], [1/Zp1 + 1/Zp2 + Zs/Zp1/Zp2, 1 + Zs/Zp1]])

def abcd2y(M):
    """
    ABCD parameters to Y - Parameters conversion
    """
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[d/b, (b * c - a * d)/b], [ -1/b, a/b]])

def y2abcd(M):
    """
    Y-Parameters to ABCD parameters conversion
    """
    y11, y12, y21, y22 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[ -y22/y21,  -1/y21], [(y12 * y21 - y11 * y22)/y21,  -y11/y21]])

def t2s(M):
    """
    Transfer scattering parameters to S-Parameters conversion
    According to definition [b1,a1]=T.[a2,b2]
    Ref: https://en.wikipedia.org/wiki/Scattering_parameters#Scattering_transfer_parameters
    """
    t11, t12, t21, t22 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    delta=t11*t22-t12*t21
    return sp.Matrix([[ t12/t22,  delta/t22], [1/t22,  -t21/t22]])

def s2t(M):
    """
    S-Parameters to Transfer scattering parameters conversion
    According to definition [b1,a1]=T.[a2,b2]
    Ref: https://en.wikipedia.org/wiki/Scattering_parameters#Scattering_transfer_parameters
    """
    s11, s12, s21, s22 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    delta=s11*s22-s12*s21
    return sp.Matrix([[ -delta/s21,  s11/s21], [-s22/s21,  1/s21]])

def abcd2z(M):
    """
    ABCD parameters to Z - Parameters conversion
    """
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a/c, ( - b * c + a * d)/c], [1/c, d/c]])

def z2abcd(M):
    """
    Z - Parameters to ABCD parameters conversion
    """
    z11, z12, z21, z22 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[z11/z21, (z11 * z22 - z21 * z12)/z21], [1/z21, z22/z21]])

def abcd2s(M, Zo=50):
    """
    ABCD parameters to S - Parameters conversion
    Valid for real Zo value
    """
    # Zo=sp.Symbol("Zo")
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    s11 = ((a + b/Zo - c * Zo - d)/(a + b/Zo + c * Zo + d))
    s12 = 2 * (a * d - b * c)/(a + b/Zo + c * Zo + d)
    s21 = (2/(a + b/Zo + c * Zo + d))
    s22 = (( - a + b/Zo - c * Zo + d)/(a + b/Zo + c * Zo + d))
    return sp.Matrix([[s11, s12], [s21, s22]])

def abcd2s_list(M, Zo=50):
    """
    ABCD parameters to S - Parameters conversion
    Valid for real Zo value
    """
    a, b, c, d = M[0], M[1], M[2], M[3]
    s11 = ((a + b/Zo - c * Zo - d)/(a + b/Zo + c * Zo + d))
    s12 = 2. * (a * d - b * c)/(a + b/Zo + c * Zo + d)
    s21 = (2./(a + b/Zo + c * Zo + d))
    s22 = (( - a + b/Zo - c * Zo + d)/(a + b/Zo + c * Zo + d))
    return [s11, s12, s21, s22]

def s2abcd(M, Z=( 50, 50 )):
    """
    S-Parameters to ABCD parameters conversion
    Valid for real Z values
    Z: reference impedance list [Z1, Z2]
    """
    Zo1, Zo2 = tuple(Z)
    s11, s12, s21, s22 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    a = ((Zo1 + s11 * Zo1) * (1 - s22) + s12 * s21 * Zo1)/(2. * s21 * sp.sqrt(Zo1 * Zo2))
    b = ((Zo1 + s11 * Zo1) * (Zo2 + s22 * Zo2) - s12 * s21 * Zo1 * Zo2)/(2. * s21 * sp.sqrt(Zo1 * Zo2))
    c = ((1 - s11) * (1 - s22) - s12 * s21)/(2. * s21 * sp.sqrt(Zo1 * Zo2))
    d = ((1 - s11) * (Zo2 + s22 * Zo2) + s12 * s21 * Zo2)/(2. * s21 * sp.sqrt(Zo1 * Zo2))
    return sp.Matrix([[a, b], [c, d]])

def abcd2t(M, Zo=50):
    """
    ABCD parameters to T - Parameters conversion

    ABCD: [V1 I1]=ABCD*[V2 -I2]
    Pseudo-Wave or Power-Wave? Don't use.
    """
    X = abcd2s(M, Zo)
    return s2t(M)

def abcd_change_ports(M):
    """
    Switching ports of ABCD parameters
    """
    M = M.I
    sp.Matrix([[M[0, 0],  - M[0, 1]], [ - M[1, 0], M[1, 1]]])

def t2abcd(M, Z=( 50,50 )):
    """
    T-parameters to ABCD parameters conversion
    """
    X = t2s(M)
    return s2abcd(X, Z)

def snp2smp(SM,ports):
    """
    This method changes the port numbering of the network
    port j of new network corresponds to ports[j] in old network
    if the length of "ports" argument is lower than number of ports, remaining ports are terminated with current reference impedances and number of ports are reduced.
    """
    ports = [x-1 for x in ports]
    ixgrid = ports, ports
    return SM.extract(*ixgrid)

def cascade_networks(networks):
    """
    Cascading 2-port Networks,  input and output is ABCD matrices of networks
    """
    return reduce(op.mul, networks)

def parallel_networks(networks):
    """
    Paralleling 2-port Networks,  input and output  is ABCD matrices of networks
    """
    ymatrices = [abcd2y(M) for M in networks]
    return y2abcd(reduce(op.add, ymatrices))

def series_networks(networks):
    """
    Series Connection of Networks (reference pins of 1. network is connected to alive pins of 2. network),  input and output  is ABCD matrices of networks
    """
    zmatrices = [abcd2z(M) for M in networks]
    return z2abcd(reduce(op.add, zmatrices))

def s_normalize_pseudo(S, Zold, Znew):
    """
    Zold,  Znew port_sayisi uzunlugunda dizilerdir
    Pseudo-Wave icin
    """
    ps = len(Zold)
    A = sp.zeros(ps, ps)
    gamma = sp.zeros(ps, ps)
    imp_yeni = []
    for i in range(ps):
        imp_yeni.append(Znew[i])
        z = Zold[i]
        ri = ((imp_yeni[i] - z)/(imp_yeni[i] + z))
        gamma[i, i] = ri
        A[i, i] = csqrt(z.real/imp_yeni[i].real) * abs(imp_yeni[i]/z) * 2 * z/(imp_yeni[i] + z)
    return A.I * (S - gamma) * (sp.eye(ps) - gamma * S).I * A

def s_normalize_power(S, Zold, Znew):
    """
    Zold,  Znew port_sayisi uzunlugunda dizilerdir
    Power-Wave icin
    Reference: Article, “Multiport conversions between S, Z, Y, h, ABCD, and T parameters”
    """
    ps = len(Zold)
    A = sp.zeros(ps, ps)
    gamma = sp.zeros(ps, ps)
    imp_yeni = []
    for i in range(ps):
        imp_yeni.append(Znew[i])
        z = Zold[i]
        gamma[i, i] = ((imp_yeni[i] - z)/(imp_yeni[i] + z.C))
        A[i, i] = 2*csqrt(z.real)*csqrt(imp_yeni[i].real) /(imp_yeni[i].C + z)
    return A.I * (S - gamma.C) * (sp.eye(ps) - gamma * S).I * A.C

def s_phase_deembed(S, phase):
    """
    S-parameter deembedding
    S is sympy.Matrix NxN
    phase, deembedding phase for each port in radian. Positive phase is deembedding into the circuit
    """
    PhaseMatrix=sp.exp(1j*sp.diag(*phase))
    return PhaseMatrix*S*PhaseMatrix

def connect_2_ports(Smatrix,k,m):
    """ Port-m is connected to port-k and both ports are removed
    Reference: QUCS technical.pdf, S-parameters in CAE programs, p.29
    """
    k,m=min(k,m),max(k,m)
    k, m = k-1, m-1
    ps=Smatrix.shape[0]
    Sm=sp.zeros(ps-2,ps-2) # output matrix
    S = Smatrix
    for i in range(ps-2):
        ii=i+(i>=k)+(i>=(m-1))
        for j in range(ps-2):
            jj=j+(j>=k)+(j>=(m-1))
            # index = (ps-2)*(i-1)+(j-1)
            temp = S[k,jj]*S[ii,m]*(1-S[m,k])+S[m,jj]*S[ii,k]*(1-S[k,m])+S[k,jj]*S[m,m]*S[ii,k]+S[m,jj]*S[k,k]*S[ii,m]
            Sm[i,j] = S[ii,jj] + temp/((1-S[m,k])*(1-S[k,m])-S[k,k]*S[m,m])
    return Sm

def connect_network_1_conn(Smatrix,EX,k,m):
    """ Port-m of EX circuit is connected to port-k of this circuit
    Remaining ports of EX are added to the port list of this circuit in order.
    Reference: QUCS technical.pdf, S-parameters in CAE programs, p.29
    """
    S = Smatrix
    k, m = k-1, m-1
    ps1=S.shape[0]
    ps2=EX.shape[0]
    ps=ps1+ps2-2
    Sm=sp.ones(ps,ps)
    for i in range(ps1-1):
        ii=i+(i>(k-1))
        for j in range(ps1-1):
            jj=j+(j>(k-1))
            # index = (i-1)*ps+(j-1)
            Sm[i,j] = S[ii,jj]+S[k,jj]*EX[m,m]*S[ii,k]/(1-S[k,k]*EX[m,m])
    for i in range(ps2-1):
        ii=i+(i>(m-1))
        for j in range(ps1-1):
            jj=j+(j>(k-1))
            # index = (i+ps1-1-1)*ps+(j-1)
            Sm[i+ps1-1,j] = S[k,jj] * EX[ii,m] / (1 - S[k,k] * EX[m,m])
    for i in range(ps1-1):
        ii=i+(i>(k-1))
        for j in range(ps2-1):
            jj=j+(j>(m-1))
            # index = (i-1)*ps+(j+ps1-1-1)
            Sm[i,j+ps1-1] = EX[m,jj] * S[ii,k] / (1 - EX[m,m] * S[k,k])
    for i in range(ps2-1):
        ii=i+(i>(m-1))
        for j in range(ps2-1):
            jj=j+ (j>(m-1))
            # index = (i+ps1-1-1)*ps+(j+ps1-1-1)
            Sm[i+ps1-1,j+ps1-1] = EX[ii,jj]+EX[m,jj]*S[k,k]*EX[ii,m]/(1-EX[m,m]*S[k,k])
    return Sm

def connect_network_1_conn_retain(Smatrix,EX,k,m):
    ideal3port = ideal_nport(3)
    EX = connect_network_1_conn(EX,ideal3port,m,1)
    psex = EX.shape[0]
    sonuc = connect_network_1_conn(Smatrix,EX,k,psex)
    return sonuc

def connect_2_ports_list(Smatrix,conns):
    """ Short circuit ports together one-to-one. Short circuited ports are removed.
    Ports that will be connected are given as tuples in list conn
    i.e. conn=[(p1,p2),(p3,p4),..]
    The order of remaining ports is kept.
    Reference: QUCS technical.pdf, S-parameters in CAE programs, p.29
    """
    for i in range(len(conns)):
        k,m = conns[i]
        Smatrix = connect_2_ports(Smatrix, k,m)
        for j in range(i+1,len(conns)):
            conns[j][0]=conns[j][0]-(conns[j][0]>k)-(conns[j][0]>m)
            conns[j][1]=conns[j][1]-(conns[j][1]>k)-(conns[j][1]>m)
    return Smatrix

def connect_2_ports_retain(Smatrix,k,m):
    """ Port-m and Port-k are joined to a single port.
    New port becomes the last port of the circuit.
    Reference: QUCS technical.pdf, S-parameters in CAE programs, p.29
    """
    ideal3port = idealNport(3)
    ps = Smatrix.shape[0]
    k,m=min(k,m),max(k,m)
    Sm = connect_network_1_conn(Smatrix,ideal3port,m,1)
    Sm = connect_2_ports(Sm,k,ps)
    return Sm

if __name__=="__main__":
    R1, R2 = sp.symbols("R1 R2")
    # s1 = abcd2s(shunt_z(R1)*series_z(R2)*shunt_z(R1) )
    # sonuc = s1.subs([(R1,100),(R2,50)]).evalf()
    # sp.pprint(s1)
    # sp.pprint(sonuc)
    s1=abcd2s(shunt_z(R1))
    s2=abcd2s(series_z(R2))
    # ss = connect_network_1_conn(s1,s2,2,1)
    # ss = connect_network_1_conn(connect_network_1_conn(s1,s2,2,1),s1,2,1)
    # sonuc = ss.subs([(R1,100),(R2,50)]).evalf()
    # sp.pprint(sp.simplify(s2))
    # sp.pprint(sp.simplify(s2abcd(ss)))
    # sp.pprint(sonuc)
    # sp.pprint(sp.ones(3,4))
    # sp.pprint(sp.diag(*np.array([1,2,3])))
    tri = idealNport(3)
    sp.pprint(sp.simplify(s2))
    # s3 = connect_network_1_conn(tri,s2,2,1)
    # sp.pprint(sp.simplify(s3))
    # s4 = connect_network_1_conn(s3,tri,3,1)
    # s5 = connect_network_1_conn(s4,s2,2,1)
    # s6 = connect_2_ports(s5,2,4)
    # sp.pprint(sp.simplify(s6))

    s4 = connect_network_1_conn_retain(s2,s2,2,2)
    sp.pprint(sp.simplify(s4))
    s5 = connect_2_ports_retain(s4,2,1)
    sp.pprint(sp.simplify(s5))
