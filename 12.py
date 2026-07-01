#bugungi darsimizda yangi boshlagan dasturchilar eng kop qiladigan xatolarni korib chiqdik
# EOF --- End Of Function - funksiyaning yakunida xatolik boldi
# EOL --- End Of Line - qatorning yakunida xatolik bor


# SintaxError
# print "hello world"      #SyntaxError: Missing parentheses in call to 'print'.
print("Hello World!")      #Hello World!

# print("Hello World!"     #SyntaxError: '(' was never closed
print("Hello World!")      


# IndentationError
#   print("Hello World!")  #IndentationError: unexpected indent
print("Hello World!")

# print("10 gacha sanaymiz")
# for num in range(1,11):
# print(num)                 #IndentationError: expected an indented block after 'for' statement on line 19

print("10 gacha sanaymiz") #joy tashlashda TAB  dan foydalan yoki shunchaki SPACE ni 4 marta bos
for num in range(10):
    print(num+1)           #qoida sen doim bir xil joy tashlashing kerak

# Run Time Error
#TypeError
# son = input("istalgan sonni kiriting: ") #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# print(f"{son} sonining kvadrati {son**2} ga teng")

son = input("istalgan sonni kiriting: ") 
son = int(son)
print(f"{son} sonining kvadrati {son**2} ga teng")


#NameError
# prit("hello world")  #NameError: name 'prit' is not defined. Did you mean: 'print'?

# mevalar = ['olma', 'nok', 'anjir', 'qulupnay']
# for meva in mvalar: #NameError: name 'mvalar' is not defined. Did you mean: 'mevalar'?
#     print(meva)

mevalar = ['olma', 'nok', 'anjir', 'qulupnay']
for meva in mevalar: 
    print(meva)

# ValueError
# number = int(input("istalgan sonni kiriting: ")) #agar men 23.3 sonini kritisam  ValueError: invalid literal for int() with base 10: '23.3'
# if number >= 0:                                  #buning sababi int onlik sonni oz ichiga olmaydi
#     print("butun son")
# else:
#     print("manfiy son")

number = float(input("istalgan onlik sonni kiriting: ")) 
if number >= 0:                                  
    print("butun son")
else:
    print("manfiy son")


#IndexError
# fruits = ['olma', 'nok', 'anjir']
# print(fruits[3])       #IndexError: list index out of range

fruits = ['olma', 'nok', 'anjir']
print(fruits[2])         #dasturlashda sanoq sistemasi 0 dan boshlanadi shu sababli 2 chi orindagi malumot bizda 3 chi biz soragan malumotni beradi


#ZeroDivisionError
# x, y = 50, 50       #ZeroDivisionError: division by zero
# print(250/(50-50))  #dasturlashda sonni 0 ga bolib bolmaydi

x, y = 60, 50       #ZeroDivisionError: division by zero
print(250/(x-y))



#Mantiqiy xatolar --- dasturchining ozi tomonidan qilingan xatolar, dastur ishlayveradi uni xatoligini python aniqlayolmaydi, dastur togi ishlaydi ammo natija xato chiqadi dasturchi ozi qiymat kirishga xato qilgan boladi
# radius = 5
# pi = 4.14
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)

radius = 5
pi = 3.14    #biz bilamiz pi 3.14 ga teng
aylana_yuzi = pi*radius**2
print(aylana_yuzi)


#yana bir misol sonni ildizdan chiqaruvchi dastur
# num = float(input("sonni kriting: "))
# ildiz = num**1/2      #81.0 sonining ildizi 40.5 ga teng      aslida esa 9 chiqishi kerak edi
# print(f"{num} sonining ildizi {ildiz} ga teng")

num = float(input("sonni kriting: "))
ildiz = num**(1/2)   # or 0.5   #81.0 sonining ildizi 9.0 ga teng 
print(f"{num} sonining ildizi {ildiz} ga teng")


# frut = ['olma', 'nok', 'anjir', 'qulupnay']
# for fru in frut:
#     print(fru)
#     print("dastur tugadi") #olma \n dastur tugadi , nok \n dastur tugadi ........ dastur tugadi 4 marta qaytarilgan chunki uni for ga tegishli bolib qolgan

frut = ['olma', 'nok', 'anjir', 'qulupnay']
for fru in frut:
    print(fru)
print("dastur tugadi")  #for tugagandan keyin dastur songida bajariladi