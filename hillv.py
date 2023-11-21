import numpy as np

def text_to_matrix(text, size):
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('A'))

    while len(matrix) % size != 0:
        matrix.append(ord('X') - ord('A'))

    return np.array(matrix).reshape(-1, size)

def matrix_to_text(matrix):
    return ''.join([chr(int(char) + ord('A')) for char in matrix.flatten()])


def encrypt(plaintext, key):
    size = len(key)
    plaintext_matrix = text_to_matrix(plaintext, size)
    ciphertext_matrix = np.dot(plaintext_matrix, key) % 26
    return matrix_to_text(ciphertext_matrix)

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt(ciphertext, key):
    size = len(key)
    key_inv = np.linalg.inv(key)
    det = round(np.linalg.det(key))
    det_inv = mod_inverse(det % 26, 26)

    if det_inv is not None:
        key_adj = (key_inv * det * det_inv) % 26
        ciphertext_matrix = text_to_matrix(ciphertext, size)
        plaintext_matrix = np.dot(ciphertext_matrix, key_adj) % 26
        return matrix_to_text(plaintext_matrix)
    else:
        return "Error: The key is not invertible."

def main():
    key_str = input("Enter the key (e.g., ABCD for a 2x2 matrix): ").upper()
    size = int(len(key_str) ** 0.5)
    
    if size * size != len(key_str):
        print("Error: Invalid key length.")
        return

    key = np.array([ord(char) - ord('A') for char in key_str]).reshape(size, size)

    plaintext = input("Enter the plaintext: ").upper()
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
