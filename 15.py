# lugat elementlari bilan ishlash
talaba_0 = {
    'ism':'ali',
    'familiya':'valiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
}

#items() --- lugatni ekranga chiqaradi
print(talaba_0.items())

for key, value in talaba_0.items():
    print(f"key: {key}")
    print(f"value: {value} \n")

#keys() --- kalitlarni ekranga chiqaradi
talaba_1 = {
    'ism':'vali',
    'familiya':'aliyev',
    'yosh':26,
    'fakultet':'informatika',
    'kurs':3
}
print(talaba_1.keys())


mahsulotlar = {
    'anor':10000,
    'olma':15000,
    'banan':20000,
    'anjir':25000,
    'gilos':30000
}
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

#agar biz keys() dan foydalanmasak ham huddi shu natijani olamiz
for mahsulot in mahsulotlar:
    print(mahsulot.title())

#example 1
bozorlik = ['anor', 'uzum', 'gilos', 'baliq', 'anjir']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} som")

#buni aksini ham qilish mumkin
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"iltimos, {buyum}ni dokoningizga olib keling")

#lugat malumotlarini alifbo tartibida tartiblash
print('dokonimizdagi mahsulotlar')
for mahs in sorted(mahsulotlar):
    print(mahs.title())

telefonlar = {
    'ali':'iphone x',
    'vali':'s9',
    'olim':'mi 10',
    'orif':'nokia',
    'hamida':'s9',
    'maryam':'huawei',
    'toxir':'iphone x',
    'umar':'iphone x'
}
print('foydalanuvchilar quyidagi telefonlarni ishlatishadi')
for tel in telefonlar.values():
    print(tel)

#foydalanuvchilar bir xil telefon ishlatganlari ham bor ekan agar 3 ta bir xil model kelsa ularni faqat 1 tasi ekranga chiqarmoqchi bolsak
#set() --- lugatda bir xil bir nechta malumot kelsa ularni faqat bittasi ekranga chiqariladi
print('foydalanuvchilar quyidagi telefonlarni ishlatishadi')
for tel in set(telefonlar.values()):
    print(tel)

#set ham bir malumot turi
toys = {'ball', 'cars', 'bear', 'teddy', 'ball', 'cars'} #tepada gaplashganimizdek set malumot turi bir biriga oxshash bolmagan malumotlarni oz ichiga oladi
print(toys) #ular ichida bir xillari bolsa ham ulardan faqat bittasi ekranga chiqariladi
print(type(toys))