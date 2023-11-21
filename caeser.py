def encrypt(M, k) -> str:
    ret = ''
    for ch in M:
        ret += chr(96 + ((ord(ch) - 96 + k) % 26))
    return ret

def decrypt(C, k) -> str:
    ret = ''
    for ch in C:
        ret += chr(96 + ((ord(ch) - 96 - k) % 26))
    return ret

def main() -> None:
    M = input("Enter plaintext: ")
    k = int(input("Enter key: "))
    C = encrypt(M, k)
    print("Cipher text:", C)
    print("Plain text:", decrypt(C, k))

if __name__ == '__main__':
    exit(main() or None)
