tasks = []

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n1. Vazifa qo‘shish\n2. Vazifalarni ko‘rish\n3. Chiqish")
    choice = input("Tanlang: ")
    
    if choice == "1":
        task = input("Yangi vazifa: ")
        tasks.append(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break
    else:
        print("Noto‘g‘ri tanlov!")
