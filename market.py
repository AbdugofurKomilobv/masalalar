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

def add_product():
    name = input("Mahsulot nomi: ")
    try:
        price = float(input("Narxi (so‘m): "))
        products.append({"name": name, "price": price})
        print(f"✅ {name} qo‘shildi.")
    except ValueError:
        print("❌ Narx noto‘g‘ri.")

def show_products():
    if not products:
        print("❗ Mahsulotlar yo‘q.")
        return
    print("=== Mahsulotlar ===")
    for i, p in enumerate(products, 1):
        print(f"{i}. {p['name']} - {p['price']} so‘m")
