class Matrix:
    def __init__(self, obj):
        self.m = []
        if isinstance(obj, list):
            self.m.append(obj)
        if isinstance(obj, str):
            for i in range(0, len(obj), 2):
                self.m.append([ord(obj[i]) - 97, 0 if i + 1 == len(obj) else ord(obj[i+1]) - 97])
        if isinstance(obj, Matrix):
            for row in obj.m:
                self.m.append(row.copy())

    def str(self):
        ret = ""
        for row in self.m:
            ret += ''.join(map(lambda x: chr(x + 97), row))
        return ret

    def mod(self, m):
        this = Matrix(self)
        for i in range(len(this.m)):
            for j in range(len(this.m[i])):
                this.m[i][j] = this.m[i][j] % m if this.m[i][j] >= 0 else (this.m[i][j] + m * 7) % m
        return this

    def dot(self, col):
        ret = []
        for i in range(len(self.m)):
            tmp = 0
            for j in range(len(col)):
                tmp += self.m[i][j] * col[j]
            ret.append(tmp)
        return Matrix(ret)

    def inv2x2(self, m):
        this = Matrix(self)
        a, b = this.m[0][0], this.m[0][1]
        c, d = this.m[1][0], this.m[1][1]
        this.m[0][0], this.m[0][1] = d, -b
        this.m[1][0], this.m[1][1] = -c, a
        this = this.mod(m)
        kInv = -1
        k = 1
        while True:
            if ((a * d - c * b) * k) % m == 1:
                kInv = k
                break
            k += 1
        for i in range(len(this.m)):
            for j in range(len(this.m[i])):
                this.m[i][j] *= kInv
        this = this.mod(m)
        return this

def encrypt(M, K):
    ret = ""
    for col in M.m:
        ret += K.dot(col).mod(26).str()
    return ret

def decrypt(C, K):
    ret = ""
    for col in C.m:
        ret += K.inv2x2(26).dot(col).mod(26).str()
    return ret

def main() -> None:
    M = Matrix(input("Enter Plaintext: "))
    K = Matrix(input("Enter Key: "))
    C = encrypt(M, K)
    Md = decrypt(Matrix(C), K)
    print("Cipher text:", C)
    print("Decrypt text:", Md)

if __name__ == "__main__":
    exit(main() or 0)
