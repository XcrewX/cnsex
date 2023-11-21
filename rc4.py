S = [0] * 255
T = [0] * 255

def initST(M, K):
    global S, T
    for i in range(255):
        S[i] = i
        T[i] = K[i % len(K)]

def initPremut(M, K):
    global S, T
    j = 0
    for i in range(255):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

def init(M, K):
    initST(M, K)
    initPremut(M, K)

def KStream():
    global S
    i, j, k = 0, 0, 0
    while True:
        k += 1
        i = (k + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def main() -> None:
    M = list(map(ord, input("Enter Plaintext: ")))
    K = list(map(ord, input("Enter Key: ")))
    init(M, K)
    C, Md = [], []
    for i in range(len(M)):
        ks = next(KStream())
        C.append(M[i] ^ ks)
        Md.append(C[-1] ^ ks)
    Md = ''.join(map(chr, Md))
    print("Cipher Text:", C)
    print("Decrypt Text:", Md)


if __name__ == "__main__":
    exit(main() or 0)
