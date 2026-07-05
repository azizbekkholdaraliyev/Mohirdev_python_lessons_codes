# --- funksiyalar bilan ishlash

# --- return

# def toliq_ism_yasa(ism, familiya):
#     """toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# talaba_1 = toliq_ism_yasa('otkir', 'hoshimov')
# talaba_2 = toliq_ism_yasa('sanjar', 'otabekov')
# print(f"darsga kelmagan talabalar: {talaba_1} va {talaba_2}")
# print(f"{talaba_1} darsga kechikib keldi")

# --- otasining ismini kritsa ham kiritmasa ham bu dastur ishlayveradi
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba_1 = toliq_ism_yasa('otkir', 'hoshimov')
# talaba_2 = toliq_ism_yasa('otkir', 'hoshimov', 'oktamovich')
# print(f"darsga kelmagan talabalar: {talaba_1} va {talaba_2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto


# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
# avtolar = [avto1, avto2]
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



#range() --- funksiyasini ozimiz yaratamiz
# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# raqamlar = oraliq(0,10)
# print(raqamlar)



#qadam ni ham qoshaylik masalan 2 qadam tashlab sana deyishi mumkinku
# def oraliq(min, max, oraliq=None):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         if oraliq:
#             min += oraliq
#         elif oraliq==None:
#             min += 1
#     return sonlar

# raqamlar = oraliq(0,10,2)
# print(raqamlar)


#avto salonga mashinalar qoshish va ularni malumotlarini lugatga va har bir moshina yaratilgandan keyin 
# ularni royhat shaklida saqlovchi dastur

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end="")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == "no":
#         break

# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(
#         f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}"
#     )