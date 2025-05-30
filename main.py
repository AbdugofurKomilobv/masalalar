# Masalan: n = 123 → javob: 131

# def next_palindrome(n):
#     def is_palindrome(x):
#         return str(x) == str(x)[::-1]
    
#     n += 1
#     while not is_palindrome(n):
#         n += 1
#     return n

# print(next_palindrome(123))  # 131



age = int(input('yosh: '))

if age > 0 and 18 > age:
    print('siz xali voyaga yetmagansiz')
elif age >= 18 and age <= 150:
    print('siz voyaga yetgansiz')
else:
    print('R.I.P')