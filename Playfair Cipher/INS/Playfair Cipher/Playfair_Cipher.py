def encrypt(plaintext, matrix):    
    plaintext = plaintext.replace("j", "i").upper().replace(" ",  "")
    if len(plaintext) % 2 != 0:
        plaintext += "Z"
   
    # Create pairs of characters from the plaintext
    pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
   
    ciphertext = ""
   
    for pair in pairs:
        r1, c1 = None, None
        r2, c2 = None, None
       
        # Find row and column indices for each character in the pair
        positions = []
        for char in pair:
            for r, row in enumerate(matrix):
                for c, val in enumerate(row):
                    if val == char:
                        positions.append((r, c))
                        break
                else:
                    continue
                break
       
        # Unpack positions
        (r1, c1), (r2, c2) = positions
       
        # Encrypt according to Playfair cipher rules
        if r1 == r2:
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            c1, c2 = c2, c1
       
        # Append encrypted characters to ciphertext
        ciphertext += matrix[r1][c1] + matrix[r2][c2]
   
    return ciphertext

def decrypt(plaintext, matrix):
    plaintext = plaintext.replace("j", "i").upper().replace(" ",  "")
    # Pad plaintext with 'z' if its length is odd
    if len(plaintext) % 2 != 0:
        plaintext += "Z"
   
    # Create pairs of characters from the plaintext
    pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
   
    ciphertext = ""
   
    for pair in pairs:
        r1, c1 = None, None
        r2, c2 = None, None
       
        # Find row and column indices for each character in the pair
        positions = []
        for char in pair:
            for r, row in enumerate(matrix):
                for c, val in enumerate(row):
                    if val == char:
                        positions.append((r, c))
                        break
                else:
                    continue
                break
       
        # Unpack positions
        (r1, c1), (r2, c2) = positions
       
        # Encrypt according to Playfair cipher rules
        if r1 == r2:
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
        elif c1 == c2:
            r1 = (r1 - 1) % 5
            r2 = (r2 - 1) % 5
        else:
            c1, c2 = c2, c1
       
        # Append encrypted characters to ciphertext
        ciphertext += matrix[r1][c1] + matrix[r2][c2]
   
    return ciphertext

# Example usage
plaintext = input("Enter the text: ")
matrix = [['Q','W','E','R','T'],
          ['Y','U','I','O','P'],
          ['A','S','D','F','G'],
          ['H','K','L','M','N'],
          ['B','C','V','X','Z']]

encrypted_text = encrypt(plaintext, matrix)
decrypted_text = decrypt(encrypted_text, matrix)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)