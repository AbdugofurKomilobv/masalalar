# import os

# products = []
# cart = []

# def clear():
#     os.system("cls" if os.name == "nt" else "clear")

# def show_menu():
#     print("=== Terminal Market ===")
#     print("1. Mahsulot qo‘shish (admin)")
#     print("2. Mahsulotlar ro‘yxati")
#     print("3. Savatga mahsulot qo‘shish")
#     print("4. Savatni ko‘rish")
#     print("5. Xarid qilish")
#     print("6. Chiqish")

# def add_product():
#     name = input("Mahsulot nomi: ")
#     try:
#         price = float(input("Narxi (so‘m): "))
#         products.append({"name": name, "price": price})
#         print(f"✅ {name} qo‘shildi.")
#     except ValueError:
#         print("❌ Narx noto‘g‘ri.")

# def show_products():
#     if not products:
#         print("❗ Mahsulotlar yo‘q.")
#         return
#     print("=== Mahsulotlar ===")
#     for i, p in enumerate(products, 1):
#         print(f"{i}. {p['name']} - {p['price']} so‘m")
# def add_to_cart():
#     show_products()
#     try:
#         index = int(input("Savatga qo‘shmoqchi bo‘lgan mahsulot raqami: ")) - 1
#         if 0 <= index < len(products):
#             cart.append(products[index])
#             print(f"🛒 {products[index]['name']} savatga qo‘shildi.")
#         else:
#             print("❌ Noto‘g‘ri raqam.")
#     except ValueError:
#         print("⚠️ Raqam kiriting.")

# def show_cart():
#     if not cart:
#         print("🛒 Savat bo‘sh.")
#         return
#     total = 0
#     print("=== Savat ===")
#     for i, item in enumerate(cart, 1):
#         print(f"{i}. {item['name']} - {item['price']} so‘m")
#         total += item['price']
#     print(f"💰 Umumiy: {total} so‘m")
# def checkout():
#     if not cart:
#         print("❗ Savat bo‘sh.")
#         return
#     show_cart()
#     confirm = input("To‘lov qilishni tasdiqlaysizmi? (ha/yo‘q): ").lower()
#     if confirm == "ha":
#         print("✅ Xaridingiz uchun rahmat!")
#         cart.clear()
#     else:
#         print("❌ To‘lov bekor qilindi.")
# while True:
#     show_menu()
#     choice = input("Tanlov (1-6): ")

#     if choice == "1":
#         add_product()
#     elif choice == "2":
#         show_products()
#     elif choice == "3":
#         add_to_cart()
#     elif choice == "4":
#         show_cart()
#     elif choice == "5":
#         checkout()
#     elif choice == "6":
#         print("Marketdan chiqildi.")
#         break
#     else:
#         print("Noto‘g‘ri tanlov.")
    
#     input("\nDavom etish uchun Enter...")
#     clear()