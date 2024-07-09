a=input("enter the text: ")

b=input("enter the key: ")

print("Encrypted text ")

encrypted = ''
for i in range(len(a)):
    encrypted += chr(ord(a[i]) ^ ord(b[i % len(b)]))

print(encrypted)

print("decrypted text ")

decrypted =''
for i in range(len(a)):
    
    decrypted += chr(ord(encrypted[i]) ^ ord(b[i% len(b)]))

print(decrypted)