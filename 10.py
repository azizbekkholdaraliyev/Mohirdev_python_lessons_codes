#if, elif, else --- shart operatorlari

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar: #avtolar ichida bir avtoni oladi
    if avto == 'bmw': #agar avto teng bolsa bmw ga
        print(avto.upper()) #bu sozning hamma harflarnini katta harfga ozgartiradi chunki BMW bu 3ta sozning qisqartmasidir
    else: #agar bmw ga teng bolmasa
        print(avto.title()) #uni bosh harfini katta qil

a = 10
print(a == 10) #True 
print(a == 5)  #False

#dasturlashda katta harf va kichik harf alohida talqin qilinadi
name = 'Anvar'
print(name == 'Anvar') #True 
print(name == 'anvar') #False

# == --- tengmi degani
b = 5
print(b == 5) #True
print(b == 6) #True

# != --- teng emasmi degani
c = 10
print(c != 11) #True
print(c != 10) #False

#example
ismiz = input('ismiz nima? \n>>>')
if ismiz.lower() != 'ali':
    print(f"uzur {ismiz.title()} biz Ali ni kutyapmiz")
else:
    print('salom, Ali')

#example 1
javob = float(input('10x7 nechi boladi \n>>>'))
if javob!=70:
    print('javob xato! ')

#example 2
yosh = int(input('yoshiz nechida? \n>>>'))
if yosh>=18:
    print('hush kelibsiz!')
else:
    print('sizga mumkin emas!')

#example 3
login = input('username yarating! \n>>>')
if len(login) <= 5:
    print("5 ta harfdan kop bolishi kerak")

#example 4
old = int(input('tugilgan yilizni kiriting: '))
if 2026-old <= 18:
    print(f"siz {2026-old} yoshda ekansiz")
    print("sizga kirish mumkin emas!")
else:
    print("hush kelibsiz!")

#example 5
years = int(input('yoshiz nechida '))
if years > 65: print("siz COVID 19 risk guruhida ekansiz!")

#example 6
x, y = 23, 43 #x=23 / y = 43
print("x<y") if x<y else print("x>y")
