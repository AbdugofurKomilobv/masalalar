# Masalan: n = 123 → javob: 131

# def next_palindrome(n):
#     def is_palindrome(x):
#         return str(x) == str(x)[::-1]
    
#     n += 1
#     while not is_palindrome(n):
#         n += 1
#     return n

# print(next_palindrome(123))  # 131



# age = int(input('yosh: '))

# if age > 0 and 18 > age:
#     print('siz xali voyaga yetmagansiz')
# elif age >= 18 and age <= 150:
#     print('siz voyaga yetgansiz')
# else:
#     print('R.I.P')

# try:
#     age = int(input("Yoshingizni kiriting: "))

#     if age <= 0:
#         print("Yosh noto‘g‘ri kiritilgan. Siz hali tug‘ilmagansiz shekilli :)")
#     elif age < 7:
#         print("Siz go‘dak bolalarsiz – bog‘chaga qatnayapsizmi?")
#     elif 7 <= age < 12:
#         print("Siz boshlang‘ich sinf o‘quvchisisiz.")
#     elif 12 <= age < 18:
#         print("Siz o‘smir yoshidasiz – maktab yoki kollej o‘quvchisi bo‘lishingiz mumkin.")
#     elif 18 <= age < 30:
#         print("Siz voyaga yetgansiz va yoshlik davridasiz – o‘qish, ishlash yoki oilaviy hayot boshlanishi.")
#     elif 30 <= age < 60:
#         print("Siz to‘liq voyaga yetgan, hayot tajribasi bor insonsiz.")
#     elif 60 <= age <= 150:
#         print("Siz keksalar safidasiz – tajriba va donolik sizda.")
#     else:
#         print("R.I.P – bu yoshda yashaganlar juda kam. Balki noto‘g‘ri kiritgandirsiz?")
# except ValueError:
#     print("Iltimos, butun son kiriting.")





# 1-QISM: Juft va toq sonlarni ajratish
# juft_sonlar = []
# toq_sonlar = []

# for i in range(4):
#     son = int(input(f"{i+1}-sonni kiriting: "))
#     if son % 2 == 0:
#         juft_sonlar.append(son)
#     else:
#         toq_sonlar.append(son)

# print("Juft sonlar:", juft_sonlar)
# print("Toq sonlar:", toq_sonlar)


# 2-QISM: Fruits ro'yxati bilan ishlash
# fruits = ["apple", "banana", "cherry", "elderberry"]
# print("\nBoshlang'ich fruits ro'yxati:", fruits)

# # 'cherry' ni pop bilan o'chirish (index orqali)
# fruits.pop(2)  # cherry indeksda 2-da

# # 'elderberry' ni remove bilan o'chirish (qiymat orqali)
# fruits.remove("elderberry")

# print("O'zgartirilgan fruits ro'yxati:", fruits)

# # 3-QISM: Ikkita ro'yxatni birlashtirish
# birinchi_royxat = [1, 2, 3, 4, 5]
# ikkinchi_royxat = [6, 7, 8, 9, 10]

# # Birinchi ro'yxatdagi 2 ta boshlang'ich elementni ikkinchisiga qo‘shish
# ikkinchi_royxat.extend(birinchi_royxat[:2])

# print("\nYangilangan ikkinchi ro'yxat:", ikkinchi_royxat)



import random
from colorama import Fore, init

# # colorama kutubxonasini ishga tushiramiz
# init(autoreset=True)

# juft_sonlar = []
# toq_sonlar = []

# i = 0

# while i < 10:
#     son = random.randint(1,100)
#     if son % 2 == 0:
#         juft_sonlar.append(son)
#     else:
#         toq_sonlar.append(son)
#     i+=1


# print(Fore.GREEN + "juft sonlar", juft_sonlar)
# print(Fore.RED + "toq sonlar", toq_sonlar)


# init(autoreset=True)

# juft_kvadrat = []
# toq_kub = []

# i = 0
# while i < 10:
#     son = random.randint(1, 50)
#     if son % 2 == 0:
#         juft_kvadrat.append(son ** 2)
#     else:
#         toq_kub.append(son ** 3)
#     i += 1

# print(Fore.GREEN + "Juft sonlar kvadrati:", juft_kvadrat)
# print(Fore.RED + "Toq sonlar kubi:", toq_kub)




# init(autoreset=True)

# juft_sonlar = []
# toq_sonlar = []

# n = int(input("Nechta son hosil qilinsin? "))

# i = 0
# while i < n:
#     son = random.randint(1, 100)
#     if son % 2 == 0:
#         juft_sonlar.append(son)
#     else:
#         toq_sonlar.append(son)
#     i += 1

# print(Fore.GREEN + f"Juft sonlar ({len(juft_sonlar)} ta):", juft_sonlar)
# print(Fore.RED + f"Toq sonlar ({len(toq_sonlar)} ta):", toq_sonlar)


# juft = []
# toq = []

# while len(juft) < 5 or len(toq) < 5:
#     s = random.randint(1, 100)
#     if s % 2 == 0 and len(juft) < 5:
#         juft.append(s)
#     elif s % 2 == 1 and len(toq) < 5:
#         toq.append(s)

# print(Fore.GREEN + "5 ta juft son:", juft)
# print(Fore.RED + "5 ta toq son:", toq)


# init(autoreset=True)

# juft_katta = []
# toq_katta = []

# i = 0
# while i < 15:
#     son = random.randint(1, 100)
#     if son > 50:
#         if son % 2 == 0:
#             juft_katta.append(son)
#         else:
#             toq_katta.append(son)
#         i += 1

# print(Fore.GREEN + "50 dan katta juft sonlar:", juft_katta)
# print(Fore.RED + "50 dan katta toq sonlar:", toq_katta)


# juft = []
# toq = []

# i = 0
# while i < 10:
#     n = random.randint(1, 20)
#     if n % 2 == 0:
#         juft.append(n)
#     else:
#         toq.append(n)
#     i += 1

# juft_yigindi = sum(juft)
# toq_kopaytma = 1
# for t in toq:
#     toq_kopaytma *= t

# print(Fore.GREEN + f"Juft sonlar: {juft} | Yig‘indisi: {juft_yigindi}")
# print(Fore.RED + f"Toq sonlar: {toq} | Ko‘paytmasi: {toq_kopaytma}")


# init(autoreset=True)

# hamma_sonlar = []

# i = 0
# while i < 20:
#     son = random.randint(1, 100)
#     hamma_sonlar.append(son)
#     i += 1

# juftlar = [x for x in hamma_sonlar if x % 2 == 0]
# toq = [x for x in hamma_sonlar if x % 2 != 0]

# print(Fore.YELLOW + "Barcha sonlar:", hamma_sonlar)
# print(Fore.GREEN + "Juft sonlar:", juftlar)
# print(Fore.RED + "Toq sonlar:", toq)


init(autoreset=True)

i = 0
while i < 10:
    son = random.randint(1, 100)
    kvadrat = son ** 2
    if son % 2 == 0:
        print(Fore.GREEN + f"{son} – juft, kvadrati: {kvadrat}")
    else:
        print(Fore.RED + f"{son} – toq, kvadrati: {kvadrat}")
    i += 1
