#Dictionary --- (lug'at) - kalit va qiymatni oz ichiga oladi qisqa qilib izohli lug'at deyish mumkin
car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

en_uz = {'apple':'olma','banana':'banan','cherry':'gilos'}
print(en_uz)
print(en_uz['apple'])

mevalar = {'olma':10000,'tarvuz':8000,'qovun':12000}
print(f"olmaning narxi {mevalar['olma']}")

#lugatda istalgan malumot turlarini saqlash mumkin
talaba_0 = {'ism':'fariz','yosh':26,'t_yil':2000}
print(f"{talaba_0['ism'].title()}, \
      {talaba_0['t_yil']} chi yili tug'ilgan, \
        {talaba_0['yosh']} yoshda")


print('talaba 1')
talaba_1 = {}
talaba_1['ism'] = 'shokir'
talaba_1['yosh'] = 25
talaba_1['kurs'] = 3
print(talaba_1)
print(f"{talaba_1['ism'].title()}, {talaba_1['yosh']} yosh , {talaba_1['kurs']} kurs")

#qiymatni ozgartirish
talaba_1['kurs'] = 4
print(talaba_1)
print(f"{talaba_1['ism'].title()}, {talaba_1['yosh']} yosh , {talaba_1['kurs']} kurs")

#qiymatni ochirib tashlash
# del
del talaba_1['yosh']
print(talaba_1)

del en_uz['cherry']
print(en_uz)

#lugatlarni bir necha qatorga bolib yozish mumkin
telefonlar = {
    'ali':'iphone',
    'vali':'redmi',
    'sardor':'pixel'
}
print(telefonlar)
print(telefonlar['ali'])

#agar biz lugatda yoq malumotni sorasak KeyError: deb javob qaytaradi

#get
tel = telefonlar.get('hasan', 'bunday ism yoq') #bunday ism yoq
print(tel)

tel = telefonlar.get('shokir',) #None
print(tel)