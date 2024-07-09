# Given parameters
p = 3
q = 11
n = p * q
phi_n = (p - 1) * (q - 1)
e = 7
d = 3

# Encryption function
def encrypt(m, e, n):
    return pow(m, e, n)

# Decryption function
def decrypt(c, d, n):
    return pow(c, d, n)

# Encrypt and decrypt given values
values = [3, 4, 1]
for value in values:
    encrypted = encrypt(value, e, n)
    decrypted = decrypt(encrypted, d, n)
    print(f"Original: {value}, Encrypted: {encrypted}, Decrypted: {decrypted}")
