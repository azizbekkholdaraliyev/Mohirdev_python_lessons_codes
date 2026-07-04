#while va lugat bilan ishlash


# print("yaqin dostlaringizning royhatini tuzamiz! ")
# ismlar = []
# n=1
# while True:
#     savol = f"{n}-dostingizni ismini kriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("yana ism qoshasizmi? (ha/yoq)")
#     n+=1
#     if takrorlash != 'ha':
#         break

# print('ismlar royhati: ')
# for ism in ismlar:
#     print(ism.title())


# #dostlarni yoshini saqlovchi dastur

# print('doslaringizni yoshini saqlaymiz!')
# doslar = {}
# ishora = True
# while ishora:
#     ism = input('dostingizni ismini kriting: ')
#     yosh = input(f"{ism}ning yoshini kiriting: ")
#     doslar[ism] = int(yosh)

#     javob = input('yana malumot qoshasizmi? (ha/yoq)')
#     if javob != 'ha':
#         ishora = False

# for ism, yosh in doslar.items():
#     print(f"{ism.title()} {yosh}da")

# cars = ['nexia', 'gentra', 'matiz', 'kobalt', 'nexia', 'spark', 'nexia', 'malibu', 'nexia']
# cars.remove('nexia') #bu faqat birinchi uchragan nexia ni olib tashlaydi.
# print(cars)

# cars = ['nexia', 'gentra', 'matiz', 'kobalt', 'nexia', 'spark', 'nexia', 'malibu', 'nexia']
# while 'nexia' in cars: #bu esa royhatdagi hamma nexia ni olib tashlaydi 
#     cars.remove('nexia') #bu sikl bu royhatda umuman nexia qolmaguncha davom etadi
# print(cars) 

# cars = ['nexia', 'gentra', 'matiz', 'kobalt', 'nexia', 'spark', 'nexia', 'malibu', 'nexia']
# car = 'nexia'
# while car in cars: #bu esa royhatdagi hamma nexia ni olib tashlaydi 
#     cars.remove(car) #bu sikl bu royhatda umuman nexia qolmaguncha davom etadi
# print(cars) 


# talabalar = ['anvar', 'olim', 'sanjar', 'vali']
# baholangan_talabalar = {}
# while talabalar: #bu degani talabalar royhatida umuman talaba qolmaguncha davom etadi, talaba qolmasa dastur toxtaydi
#     talaba = talabalar.pop() #royhatdan bitta talabani sugirib oladi
#     baho = input(f"{talaba.title()}ning bahosini kiring: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho) #bu yerda talaba kalit, baho esa qiymat

# #talabalar royhatini ekranga chiqarsang endi u bosh, chunki biz har bir talabani boshqa lugatga otqazdik va baholadik
# print(talabalar)

# #baholangan_talabalar lugati esa endi tola
# print(baholangan_talabalar)