#list bilan ishlash 
cars = ['bmw', 'mers', 'audi', 'hundai', 'opel', 'chevrolet', 'tesla']
print(cars)

#sort() --- royhat ichidagi malumotlarni alifbe tartibida sartarofka qiladi
#katta harflar doim alifbe tartibidan ham oldinda keladi
cars.sort()
print(cars)

#sort(reverse=true) --- alifbo tartibida teskarisiga tartiblaydi
cars.sort(reverse=True)
print(cars)

#sorted() --- royhatga tegmagan holatda alifbe tartibida sartarofka qiladi, asl holiga tegmaydi
print(sorted(cars))
print(sorted(cars, reverse=True))

#bularni sonlarga ham qolash mumkin
sonlar = [12, 14, 13, 17, 16, 15, 19, 18]

sonlar.sort()
print(sonlar)

print(sorted(sonlar))
print(sorted(sonlar, reverse=True))

#len() --- royhatni uzunligini aniqlaydi
print(len(sonlar))
print(len(cars))

#range() --- malum bir sondan malum bir songacha bolgan sonlarni royhatini tuzadi
raqamlar = list(range(0, 10))
print(raqamlar)

#qadamni ham bera olasan misol uchun faqat toq yoki juft sonlarni chiqaraolasan
numbers = list(range(0, 22, 2))
print(numbers)

#max --- listdagi eng katta qiymatni korsatadi
print(max(numbers))

#min --- listdagi eng kichik qiymatni korsatadi
print(min(numbers))

#sum --- listdagi hamma sonlarni qiymatini hisoblab beradi
print(sum(numbers))

#royhatni malum bir qismini ajratib olish uchun 
print(cars[0:3])
print(cars[3:5])

print(cars[:3])
print(cars[2:])

#royhatni nushalash va ozgartirish

my_cars = cars
print('my cars' ,my_cars)

my_cars.remove('hundai')
print(my_cars)

my_cars[0] = 'gentra'
print(my_cars)

#but ammo bu ozgarishlar cars ga ham tasir qiladi chunki biz my_cars = cars deb yozganmiz bu esa bitta royhatga 2 ta nom berishdir
#royhatni qanday nushalab olish mumkin
cars_me = cars[:]

cars_me.remove('bmw')
print(cars_me)
print(cars)

cars_me[0] = 'bugatti'
print('cars = ', cars)
print('cars me = ', cars_me)

#tuple --- malumot turi
#bu malumot turi ozgarmas hisoblanadi uni hech qanday ozgartirib bolmaydi
toys = ('car', 'teddy', 'gun', 'bus', 'ball')
# toys.remove('cars') AttributeError: 'tuple' object has no attribute 'remove'
# toys.append('knife') AttributeError: 'tuple' object has no attribute 'append'

#ammo biz ozgartirishga majbur bolib qolsak tupledagi royhatni listga ozgartiramiz va ozgartirib bolib yana tuplega ozgartirishimiz mumkin
print(type(toys)) #tuple
toys = list(toys)
print(type(toys)) #list

print(toys)

toys.append('bear')
print(toys)

toys.remove('teddy')
print(toys)

#ozgartirib bolgan royhatni yana tuple ga qaytarib qoyishimiz mumkin
print(type(toys))
toys = tuple(toys)
print(type(toys))