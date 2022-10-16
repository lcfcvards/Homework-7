import random
random_value = random.randint(1, 10)
attempt = 0

for i in range(1, 4):
    choice = int(input(f"Попытка №{i}: "))
    if choice > random_value:
        print("Бери меньше")
    elif choice < random_value:
        print("Бери больше")
    else:
        print("Ты угадал!")
        break
    attempt += 1
if attempt >= 3:
    print("Ты не угадал!")
