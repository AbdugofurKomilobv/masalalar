# tasks = []

# def show_tasks():
#     for i, task in enumerate(tasks, 1):
#         print(f"{i}. {task}")

# while True:
#     print("\n1. Vazifa qo‘shish\n2. Vazifalarni ko‘rish\n3. Chiqish")
#     choice = input("Tanlang: ")
    
#     if choice == "1":
#         task = input("Yangi vazifa: ")
#         tasks.append(task)
#     elif choice == "2":
#         show_tasks()
#     elif choice == "3":
#         break
#     else:
#         print("Noto‘g‘ri tanlov!")

# import random

# secret = random.randint(1, 100)
# tries = 0

# while True:
#     guess = int(input("1 dan 100 gacha son kiriting: "))
#     tries += 1
#     if guess < secret:
#         print("Ko‘proq son kiriting!")
#     elif guess > secret:
#         print("Kamroq son kiriting!")
#     else:
#         print(f"Topdingiz! Urinishlar soni: {tries}")
#         break


birthdays = {}

while True:
    print("\n1. Tug‘ilgan kun qo‘shish\n2. Ko‘rish\n3. Chiqish")
    choice = input("Tanlang: ")
    
    if choice == "1":
        name = input("Ism: ")
        date = input("Tug‘ilgan sana (dd-mm): ")
        birthdays[name] = date
    elif choice == "2":
        for name, date in birthdays.items():
            print(f"{name} - {date}")
    elif choice == "3":
        break
    else:
        print("Noto‘g‘ri tanlov!")
