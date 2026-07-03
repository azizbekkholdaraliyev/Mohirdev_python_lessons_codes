#input() va while

#input()
# ism = input('ismingiz nima ')
# savol = f"salom {ism.title()}. yoshingiz nechida? "
# yosh = input(savol) #input doim foydalanuvchi kiritgan malumotini string deb qabul qiladi
# yosh = int(yosh)
# height = input('boyingiz nechi metr? ')
# height = float(height)

#while()
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son = son + 1
# print('dastur tugadi')

# # while and input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')


# # ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur to\'xtadi!')

# break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi!')
# # break for

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# CONTINUE
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# # # Continue while
# son = 0
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)

# infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son += 1

# son = 1
# while son>0:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)