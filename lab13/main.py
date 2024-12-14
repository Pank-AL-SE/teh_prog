import math

def I(eta):
    return math.log2(eta) / 3 + 1

def K(eta, i):
    result = 1
    for j in range(1, i):
        result += eta / (8 ** j)
    return result

def eta2KFunc(eta):
    return eta * math.log2(eta)

def NkFunc(eta):
    return 2 * eta * math.log2(eta)

def NFunc(k, Nk):
    return k * Nk

def VFunc(k, Nk, eta):
    return k * Nk * math.log2(2 * eta)

def PFunc(N):
    return 3 * N / 8

def TFunc(P):
    return P / (5 * 20)

def BFunc(V):
    return V / 3000

def tauFunc(T):
    return T / 2

def tnFunc(tau, B):
    return tau / math.log(B)

def main():
    eta_values = [8, 300, 400, 512]
    
    for eta in eta_values:
        print("")
        i = I(eta)
        k = K(eta, int(i))
        eta2k = eta2KFunc(eta)
        Nk = NkFunc(eta2k)
        N = NFunc(k, Nk)
        V = VFunc(k, Nk, eta2k)
        P = PFunc(N)
        T = TFunc(P)
        B = BFunc(V)
        tau = tauFunc(T)
        tn = tnFunc(tau, B)
        
        print(f"eta = {eta}")
        print(f"i = {i}")
        print(f"k = {k}")
        print(f"Nk = {Nk}")
        print(f"N = {N}")
        print(f"V = {V}")
        print(f"P = {P}")
        print(f"T = {T}")
        print(f"B = {B}")
        print(f"tau = {tau}")
        print(f"tn = {tn}")

if __name__ == "__main__":
    main()
