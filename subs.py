Sub = {chr(97 + x): chr(97 + 26 - x - 1) for x in range(26)}
InvSub = {chr(97 + 26 - x - 1): chr(97 + x) for x in range(26)}

def encrypt(M):
    return ''.join(map(lambda x: Sub[x], M))

def decrypt(C):
    return ''.join(map(lambda x: InvSub[x], C))

def main() -> None:
    M = input("Enter Plaintext: ")
    C = encrypt(M)
    Md = decrypt(C)
    print("Cipher text:", C)
    print("Decrypt text:", Md)

if __name__ == "__main__":
    exit(main() or 0)
