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
juft_sonlar = []
toq_sonlar = []

for i in range(4):
    son = int(input(f"{i+1}-sonni kiriting: "))
    if son % 2 == 0:
        juft_sonlar.append(son)
    else:
        toq_sonlar.append(son)

print("Juft sonlar:", juft_sonlar)
print("Toq sonlar:", toq_sonlar)


