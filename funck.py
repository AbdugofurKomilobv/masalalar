import os

tasks = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=== TO-DO LIST ===")
    print("1. Vazifa qo‘shish")
    print("2. Vazifalarni ko‘rish")
    print("3. Vazifani o‘chirish")
    print("4. Chiqish")

def add_task():
    task = input("Yangi vazifani kiriting: ")
    tasks.append(task)
    print("✅ Vazifa qo‘shildi!")

def show_tasks():
    if not tasks:
        print("❗ Vazifalar yo‘q.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    show_tasks()
    try:
        index = int(input("O‘chirmoqchi bo‘lgan vazifa raqamini kiriting: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"🗑️ '{deleted}' o‘chirildi.")
        else:
            print("❌ Noto‘g‘ri raqam.")
    except ValueError:
        print("⚠️ Raqam kiriting!")

while True:
    show_menu()
    choice = input("Tanlang (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Dasturdan chiqildi.")
        break
    else:
        print("Noto‘g‘ri tanlov.")
    
    input("\nDavom etish uchun Enter bosing...")
    clear()
