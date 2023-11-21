def display(disp):
    convert = [chr(char) for char in disp]
    print("".join(convert))

def main():
    temp = 0
    ptext = input("\nEnter Plain Text: ")
    key = input("Enter Key Text: ")
    ptextLen = len(ptext)
    keyLen = len(key)
    cipher = [0] * ptextLen
    decrypt = [0] * ptextLen
    ptexti = [ord(char) for char in ptext]
    keyi = [ord(char) for char in key]
    s = list(range(256))
    k = keyi * (255 // keyLen + 1)
    j = 0

    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

    i = 0
    j = 0
    z = 0

    for l in range(ptextLen):
        i = (l + 1) % 256
        j = (j + s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        z = s[(s[i] + s[j]) % 256]
        cipher[l] = z ^ ptexti[l]
        decrypt[l] = z ^ cipher[l]

    print("ENCRYPTED: ", end="")
    display(cipher)
    print("\nDECRYPTED: ", end="")
    display(decrypt)

if __name__ == "__main__":
    main()
