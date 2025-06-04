import os

products = []
cart = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    print("=== Terminal Market ===")
    print("1. Mahsulot qo‘shish (admin)")
    print("2. Mahsulotlar ro‘yxati")
    print("3. Savatga mahsulot qo‘shish")
    print("4. Savatni ko‘rish")
    print("5. Xarid qilish")
    print("6. Chiqish")
