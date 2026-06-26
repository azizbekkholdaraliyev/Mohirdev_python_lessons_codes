#sonlar bilan ishlash (integer va float)
a = 20
b = 5.5
temp = 36.6
print(type(temp))
print(type(a))
print(type(b))

print("uzun sonlarni osnroq yozish uchun orasini _ bilan ajratish mumkin bu xato emas")
aholi_soni = 7_364_434_233
print(aholi_soni)

x, y, z = 2, 3, 4
print(x, y, z)


c = a*b
print(type(c))

d = 100/2
print(d)

dd = 100//2
print(dd)

print("ozgarmas qiymatlar katta harflar bilan yozsam bu ozgarmas qiymatga ega uni ozgartirma")
radius = 20
PI = 3.14159
diametr = 2*radius
print("aylana uzunligi=", PI*diametr)



ism = "javohir"
yosh = 26

# habar = ism + yosh
# print(habar)
#string va integer, floatni + bolmaydi
print(type(ism))
print(type(yosh))

print(ism + str(yosh))
#bunda yosh barbir int ligicha qoladi 
print(type(yosh))


#kichik dasturcha

tavallud = input("nechanchi yilda tugilgansiz?")
yoshi = 2026 - int(tavallud)
print("siz", yoshi, "dasiz")

#input foydalanuvchidan qabul qilingan malumotni doim string deb qabul qiladi shuning uchun arifmetik amal bajarmoqchi bolsang uni int(ozgaruvchi) qilib yozishing kerek
#yoki temp = int(input("yoshingiz nechida"))

t = int(9)
n = float(10)
s = str(36.6)
print(type(t))
print(type(n))
print(type(s))
