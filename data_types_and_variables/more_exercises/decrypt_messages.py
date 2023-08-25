key = int(input())
num_of_lines = int(input())

decrypted_message = []
decrypted = []
encrypted = []

for line in range(num_of_lines):
    new_line = input()

    decrypted_message.append(ord(new_line))
for item in decrypted_message:
    item += key
    decrypted.append(item)

for item in decrypted:
    encrypted.append((chr(item)))

print(''.join(encrypted))
