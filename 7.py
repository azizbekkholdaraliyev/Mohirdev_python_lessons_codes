#list  

mevalar = ['olma', 'anor', 'anjir', 'shaftoli']

narxlar = [1998, 1200, 2000, 9090]

sonlar = ['bir', 'ikki', 3, 4, 5]

ismlar = []

#elementlarni ozini tarib raqami bilan chaqirib olish mumkin dasturlash olamida sanoq tartibi 0,1,2,3.... deb boshlanadi
print(mevalar[0])
print(narxlar[2])
print(sonlar[4])
print(ismlar)
print(mevalar[-1])
print(narxlar[-2])
print(mevalar[3].upper())
print(narxlar[1] + narxlar[2])
print(narxlar[1] - 100)
mevalar[0] = 'orik'
print(mevalar[0])

cars = []

#append() --- listga malumot qoshish uchun va malumot qoshilganda list oxiriga qoshiladi
mevalar.append('qovun')
print(mevalar)

#insert()  --- listni index boyicha listning hohlagan joyiga malumotni qoshish mumkin
mevalar.insert(3, 'ananas')
print(mevalar)

#del ---  listdagi malumotlarni ochirib tashlash uchun ishlatiladi
cars.append('lacetti')
cars.append('malibu')
cars.append('damas')
cars.append('nexia')
cars.append('kobalt')

print(cars)

del cars[0]
print(cars)

del cars[2]
print(cars)

cars.insert(0, 'nexia_3')
print(cars)

#remove() --- listdagi malumotni olib tashlaydi uning nomi orqali ammo bu funksiya eng birinchi uchragan qiymatni ozini olib tashlaydi 
#misol uchun listda 2ta mushuk bor bir uni ochirib tashlasak faqatgina birinchi mushuk listdan olib tashlanadi qolgan mushuk nomli mushuklar esa qoladi
hayvonlar = ['mushuk', 'kuchuk', 'qoy', 'lochin', 'mushuk']
print(hayvonlar)

hayvonlar.remove('mushuk')
print(hayvonlar)

#pop --- list ichidagi malumotni sugurib olib boshqa maqsadlarda ishlatish uchun imkoniyat yaratadi
#agar bir pop() dan foydalanib olishi kerak bolgan malumotni indexini kiritmasak u listdagi oxirgi malumotni ajratib oladi
bozorlik = ['piyor', 'non', 'gosht', 'shakar', 'tuz']
print(bozorlik)
mahsulot = bozorlik.pop(1)
print(mahsulot)
print(bozorlik)