#fayylar bilan ishlash

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

