#Nesting --- qisqa qilib aytganda bir narsani ichida boshqa narsa saqlash yani tarmoqlanib ketaveradi
car0 = {
    'model':'nexia',
    'rang':'qizil',
    'yil':2019,
    'narh':15000,
    'km':20000,
    'karobka':'mexanika'
}
car1 = {
    'model':'nexia 3',
    'rang':'sariq',
    'yil':2012,
    'narh':17000,
    'km':40000,
    'karobka':'mexanika'
}
car2 = {
    'model':'gentra',
    'rang':'qora',
    'yil':2017,
    'narh':19000,
    'km':21000,
    'karobka':'mexanika'
}
# #tasavvur qiling bir barcha mashinalarni foydalanuvchiga korsatmoqchimiz
# car = car0 # shu yol orqali biz har bir mashinani ekranga osongina chiqarishimiz mumkin ammo kop qator codelar yozish talab etiladi
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

#osonroq yoli
cars = [car0, car1, car2] #har bir lugatni bir listga yigib oldik va qisqa kod orqali bu malumotlarni ekranga chiqardik
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
    
# #endi tepadagi lugatlardan yaratilgan listni malum bir kerakli malumotni ozini qanday ekranga chiqaramiz
# print(cars[0])
# print(cars[1])
# print(cars[2])

# #ichidagi elemetlarni chiqarish uchun
# print(cars[0]['model'])
# print(cars[2]['rang'])
# print(cars[1]['narh'])

# #
# print(f"{cars[0]['rang'].title()} "
#       f"{cars[2]['model']}")

# #example
# malibus=[]
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2026,
#         'narh':None,
#         'km':0,
#         'karobka':'avto'
#     }
#     malibus.append(new_car)
# #malibus royhatini ichiga qarasak 10 ta malibu haqidagi malumotni korishimiz mumkin
# for malibu in malibus:
#     print(malibu)

# #endi mashinalarga ozgartirish kiritishimiz mumkin misol bizda
# #umuman rang berilmagan 10 ta malibu bor ularga har biriga alohida rang berishimiz mumkin
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[3:6]: #3dan 5gacha chunki range da ogirgi raqam kirmaydi
#     malibu['rang']='qora'

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['karobka']='mexanika'

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000

# # for malibu in malibus:
# #     print(malibu)

# # LUG'AT ICHIDA RO'YXAT
# dasturchilar = {
#     "ali": ["python", "c++"],
#     "vali": ["html", "css", "js"],
#     "hasan": ["php", "sql"],
#     "husan": ["python", "php"],
#     "maryam": ["c++", "c#"],
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end="")
#     for til in tillar:
#         print(f"{til.upper()} ", end="")




hamkasblar = {
    "ali": {
        "familiya": "valiyev",
        "tyil": 1995,
        "malumot": "oliy",
        "tillar": ["python", "c++"],
    },
    "vali": {
        "familiya": "aliyev",
        "tyil": 2001,
        "malumot": "o'rta-maxsus",
        "tillar": ["html", "css", "js"],
    },
    "hasan": {
        "familiya": "husanov",
        "tyil": 1999,
        "malumot": "maxsus",
        "tillar": ["python", "php"],
    },
}

for ism, info in hamkasblar.items():
    print(
        f"\n{ism.title()} {info['familiya'].title()}, "
        f"{info['tyil']}-yilda tug'ilgan. "
        f"Ma'lumoti: {info['malumot']}. \n"
        "Quyidagi dasturlash tillarini biladi:"
    )
    for til in info["tillar"]:
        print(til.upper(), end=" ")