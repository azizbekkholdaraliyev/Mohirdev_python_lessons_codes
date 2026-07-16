#fayylar bilan ishlash

import pickle

# file = open('pi.txt') # open funksiyasi fileni ochadi va file ozgaruvchiga obeykni yuklaydi
# #va biz shu joyda etibor berishimiz kerak biz fileni ochganimizdan keyin uni yopib qoyishimiz ham kerak.
# # file.close()

# #va biz fileni oqishimiz ham mumkin ammo file ochiq holatda bolishi kerak
# PI = file.read()
# print(PI)
# file.close()

#lekin tepadagi usullar tavfsiya etilmaydi chunki fileni yopish esimizdan chiqib qolsa malumotimizga zarar yetishi mumkin
#uning orniga bunday qilish mumkin:
with open('pi.txt') as file: 
    pi = file.read()
#buning yaxshi tarafi ish tugagandan keyin file avtomatic yopiladi
print(pi)

#python filelarni open qilganda ularni string deb qabul qiladi

pi = pi.rstrip() #qatorni oxiridagi bosh joyni olib tashlaydi
pi = pi.replace('\n','') #matindagi berilgan beligini topib boshqasiga ozgartiradi
pi = float(pi) #string ni float ga ozgartiradi
print(pi)


#biz yangi file yaratib unga malumot yozishimiz ham mumkin
#lekin sen yaratayotgan file nomi boshqa file da bolmasligi kerak agar shunday bolsa python oldingi file malumotlarini ochirib tashlab qaytadan yozadi
# fayl_nomi = 'new_file.txt'
# ism = 'alibek'
# familiya = 'valiyev'
# tyil = 2003
# with open(fayl_nomi, 'w') as fayl:
#     fayl.write(ism+'\n') #\n qator tashlab yozadi
#     fayl.write(familiya+'\n')
#     fayl.write(str(tyil)+'\n') #str(tyil) --- chunki python fileni oqishda ham yozishda ham str bilan bajaradi




#biz mavjud filega malumot qoshishimiz ham mumkin
# file2 = 'new_file_2'

# with open(file2,'a') as file: #agar fayl bolmasa ozi yangi yaratib qoshadi
#     file.write('Alijon Valiyev\n')
#     file.write('2003')



# talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}
# talaba2 = {"ism": "alijon", "familiya": "valiyev", "tyil": 2004, "kurs": 1}

# with open("info", "wb") as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)


# talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}
# talaba2 = {"ism": "alijon", "familiya": "valiyev", "tyil": 2004, "kurs": 1}

# with open("info", "wb") as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)


# with open("info", "rb") as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)