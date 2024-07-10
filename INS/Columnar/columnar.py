def encrypt(msg, key):
    l = (len(msg) // len(key)) + (len(msg) % len(key))
    grid = [[" " for _ in range(len(key))] for _ in range(l)]
    index = 0
    for i in range(len(msg)):
        row = i // len(key)
        col = i % len(key)
        grid[row][col] = msg[index]
        index += 1

    sorted_columns = sorted(range(len(key)), key=key.__getitem__)
    decrypted_message = []
    for col in sorted_columns:
        for row in grid:
            decrypted_message.append(row[col])
    return ''.join(decrypted_message)

def decrypt(msg, key):
    l = (len(msg) // len(key)) + (len(msg) % len(key))
    grid = [[" " for _ in range(len(key))] for _ in range(l)]
    index = 0
    for i in range(len(msg)):
        row = i % l
        col = key[i // l] - 1
        grid[row][col] = msg[index]
        index += 1

    return ''.join(''.join(row) for row in grid)

message = input("Enter Message: ")
key = [4,2,3,1]

print("Cipher Text: ", encrypt(message, key))
print("Plain Text: ", decrypt(encrypt(message, key), key))
