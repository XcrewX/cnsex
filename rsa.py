import random
import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

# Example usage
p = 61
q = 53
public, private = generate_keypair(p, q)
message = '88'
encrypted_msg = encrypt(public, message)
decrypted_msg = decrypt(private, encrypted_msg)

print("Public Key: ", public)
print("Private Key: ", private)
print("Original Message: ", message)
print("Encrypted Message: ", encrypted_msg)
print("Decrypted Message: ", decrypted_msg)

