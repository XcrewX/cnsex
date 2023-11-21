FILL_CHAR = 'y'
key = [[None for _ in range(5)] for _ in range(5)]
handleIJ = lambda x: x if len(x) == 1 else x[0]

def nextFillChar(ch):
    global FILL_CHAR
    num = ord(FILL_CHAR) - ord('a')
    while True:
        FILL_CHAR = chr(((num + 1) % 26) + ord('a'))
        if FILL_CHAR != ch:
            return FILL_CHAR

def constructKey(K):
    global key
    if 'i' in K or 'j' in K:
        raise ValueError("Invalid Key") # not handling i/j containing key
    done = set()
    i, j = 0, 0
    K += ''.join(map(lambda x: chr(97 + x), range(26)))
    while K:
        if K[0] not in done:
            if K[0] in 'ij':
                done.add('i')
                done.add('j')
                key[i][j] = 'ij'
                j += 1
                if j % 5 == 0:
                    j = 0
                    i += 1
                continue
            key[i][j] = K[0]
            done.add(K[0])
            j += 1
            if j % 5 == 0:
                j = 0
                i += 1
        K = K[1:]

def indexOf(x):
    global key
    for i in range(5):
        for j in range(5):
            if x in key[i][j]:
                return (i, j)

def diagrams(M):
    ret, n = [], len(M)
    i = 0
    while i < n:
        buf = M[i]
        if i + 1 == n:
            buf += nextFillChar(M[i])
            i += 2
        elif M[i] == M[i + 1]:
            buf += nextFillChar(M[i])
            i += 1
        else:
            buf += M[i+1]
            i += 2
        ret.append(buf)
    return ret

def encrypt(M):
    global key
    C = ''
    for pair in diagrams(M):
        a, b = indexOf(pair[0]), indexOf(pair[1])
        if a[0] == b[0]: # same row
            for x, y in [a, b]:
                C += handleIJ(key[x][(y + 1) % 5])
        elif a[1] == b[1]: # same col
            for x, y in [a, b]:
                C += handleIJ(key[(x + 1) % 5][y])
        elif a[0] != b[0] and a[1] != b[1]:
            x1, y1 = a
            x2, y2 = b
            C += handleIJ(key[x1][y2])
            C += handleIJ(key[x2][y1])
    return C

def decrypt(M):
    global key
    C = ''
    for pair in diagrams(M):
        a, b = indexOf(pair[0]), indexOf(pair[1])
        if a[0] == b[0]: # same row
            for x, y in [a, b]:
                C += handleIJ(key[x][(y - 1) % 5])
        elif a[1] == b[1]: # same col
            for x, y in [a, b]:
                C += handleIJ(key[(x - 1) % 5][y])
        elif a[0] != b[0] and a[1] != b[1]:
            x1, y1 = a
            x2, y2 = b
            C += handleIJ(key[x1][y2])
            C += handleIJ(key[x2][y1])
    return C

def main() -> None:
    M = "hello"
    K = "ganesh"
    constructKey(K)
    C = encrypt(M)
    Md = decrypt(C)
    print("Cipher text:", C)
    print("Decrypt text:", Md)

if __name__ == "__main__":
    exit(main() or 0)
