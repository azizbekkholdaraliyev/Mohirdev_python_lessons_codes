#OOP

#chiziqli dastur --- dastur ketma ketlik bilan bajariladi, boshi va oxiri aniq belgilangan
# import random

# def sontop(x=10):
#     tasodifiy_son = random.randint(1, x)
#     print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin < tasodifiy_son:
#             print("Kattaroq son ayting:", end="")
#         elif taxmin > tasodifiy_son:
#             print("Kichikroq son ayting:", end="")
#         else:
#             print("Yutdingiz!")
#             break

#     print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
#     return taxminlar


# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = random.randint(quyi, yuqori)
#         else:
#             taxmin = quyi
#         javob = input(
#             f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
#             f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
#         )
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan topdim!")
#     return taxminlar


# def play(x=10):
#     yana = True
#     while yana:
#         taxminlar_pc = sontop_pc(x)
#         taxminlar_user = sontop(x)

#         if taxminlar_user > taxminlar_pc:
#             print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
#         elif taxminlar_user < taxminlar_pc:
#             print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
#         else:
#             print("Durrang!")
#         yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


# play()

#*************************************************************************************************************
x = 10
print(type(x)) #bu yerda 10 obeykt va u int classiga tegishli, 
matn = 'salom'
print(type(matn)) #bu yerda matn obeykt va u str classiga tegishli

#har bir obeyktni va classni oziga yarasha funksiya yani methodlari boladi
print(matn.upper()) #bu yerda upper() methodi faqat str classlari uchun ishlaydi

#agar biz upper() methodini boshqa classga ishlatsak u xato beradi
#print(x.upper()) #AttributeError: 'int' object has no attribute 'upper

#misol uchun kelinglar bir funksiya yaratamiz uni chaqirsak assalomu alaykum deb javob bersin
def salom():
    print('assalomu alaykum')

salom()
#keling endi manashu funksiyani ham turini koraylik
print(type(salom)) #<class 'function'>


#keling endi ozimiz abeykt yaratamiz
#uning uchun esa biz class yaratishimiz kerak
#bu yerda class bizni obeyklarimiz uchun shablon bolib hizmat qiladi
#biz bir marta class yaratib olsak keyin undan foydalanib istalgancha obeykt yaratishimiz mumkin

#classga nom berishda birinchi harfini doim katta harf bilan boshla chunki kelajakda ozgaruvchi bilan classni ajratib olish osoon boladi
class Talaba: #class bu class yaratish uchun kalit soz, talaba esa classimizning nomi 
    def __init__(self, ism, familiya, tyil): #self bu yerda kelajakda classni ichidagi funksiyaga obeyktni ozini uzatish uchun
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self): #bu yerda get_name methodini chaqirganimizda bu abeykt ozining ismini qaytaradi
        return self.ism

    def get_familiya(self):
        return self.familiya
    
    def tanishtir(self): #method yaratamiz tanishtir degan uni chaqirganimizda talaba ozini tanishtirsin
        return f"ismim {self.ism}, familyam {self.familiya}, tugilgan yilim {self.tyil}"
        #ozi bu yerda print() ishlatish xato biz return ishlatsak bizga matn korinishida malumot qaytarsa biz uni istalgan joyda ishlataolam
    
    #keling biz yana bir method yarataylik unda ozimiz ham selfdan tashqari argument kritaylik
    def get_age(self, yil): #talabaning yoshini chiqaramiz
        return yil - self.tyil #yil bu hozirgi yil va undan talabaning tugilgan yilini ayirsak uning yoshi kelib chiqadi
    


#keling endi bu classdan obeykt yaratishni koramiz
talaba1 = Talaba('olim', 'olimov', 2000)
talaba2 = Talaba('ali', 'valiyev', 2000)
talaba3 = Talaba('valijon', 'asadov', 2000)

print(talaba2.get_name())
print(talaba3.get_name())

print(talaba3.get_familiya())
print(talaba2.get_familiya())

#endi tanishtir methodini ishlatib koramiz 
print(talaba1.tanishtir())
print(talaba2.tanishtir())

#get_age() methodini ishlatib koramiz
print(talaba3.get_age(2026)) #26
#biz hozirgi yilni kritishimiz shart agar kritmasak dastur xatolik beradi
#print(talaba3.get_age()) #TypeError: Talaba.get_age() missing 1 required positional argument: 'yil'