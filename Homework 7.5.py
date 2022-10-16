encrypt = input("Введите сообщение для шифровки: ")
key = int(input("Введите число (сдвиг): "))
encrypted = ""

for letter in encrypt:
    if 'A' <= letter <= 'Z':
        encrypted += chr(ord('A') + (ord(letter)-ord('A') + key) % 26)
    elif 'a' <= letter <= 'z':
        encrypted += chr(ord('a') + (ord(letter)-ord('a') + key) % 26)
    else:
        encrypted += letter
print("Ваш шифр:", encrypted)
