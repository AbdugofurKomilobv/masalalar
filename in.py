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


# birthdays = {}

# while True:
#     print("\n1. Tug‘ilgan kun qo‘shish\n2. Ko‘rish\n3. Chiqish")
#     choice = input("Tanlang: ")
    
#     if choice == "1":
#         name = input("Ism: ")
#         date = input("Tug‘ilgan sana (dd-mm): ")
#         birthdays[name] = date
#     elif choice == "2":
#         for name, date in birthdays.items():
#             print(f"{name} - {date}")
#     elif choice == "3":
#         break
#     else:
#         print("Noto‘g‘ri tanlov!")

# while True:
#     message = input("Sen: ").lower()
    
#     if "salom" in message:
#         print("Bot: Salom! Yaxshimisan?")
#     elif "yaxshi" in message:
#         print("Bot: Zo'r-ku! 😊")
#     elif "isming nima" in message:
#         print("Bot: Meni 'MegaBot' deb chaqir.")
#     elif "hayr" in message or "xayr" in message:
#         print("Bot: Xayr! Ko‘rishguncha!")
#         break
#     else:
#         print("Bot: Buni tushunmadim, boshqacharoq yoz-chi? 🤔")

# import time

# sekund = int(input("Necha sekund kutamiz? "))
# print("Taymer boshlandi!")

# for i in range(sekund, 0, -1):
#     print(i)
#     time.sleep(1)

# print("⏰ Taymer tugadi!")


# import random

# score = 0

# for i in range(5):
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     answer = int(input(f"{a} + {b} = "))
#     if answer == a + b:
#         print("✅ To‘g‘ri!")
#         score += 1
#     else:
#         print(f"❌ Noto‘g‘ri! Javob: {a + b}")

# print(f"\nUmumiy natija: {score}/5")



import random

symbols = ["🍒", "🍋", "🍊", "⭐", "7️⃣"]

while True:
    input("🎰 PLAY uchun Enter bosing...")
    slots = [random.choice(symbols) for _ in range(3)]
    print(" | ".join(slots))
    
    if slots.count(slots[0]) == 3:
        print("🎉 Jackpot! Hammayoq bir xil!")
    elif len(set(slots)) == 2:
        print("😄 Yaxshi urinish!")
    else:
        print("😢 Bu safar omad bo‘lmadi...")
    
    if input("Yana o‘ynaysanmi? (ha/yo‘q): ") != "ha":
        break
