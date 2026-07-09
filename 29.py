#OOP

#Objects

#shunchaki qoidalar 
#talaba1.get_name() --- bu yerda get_name() method hisoblanadi
#class Talaba: --- bu yerda Talaba class hisoblanadi

class Talaba:
    def __init__(self, ism, familiya, tyil): 
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1  #uni (self, ism....) qatoriga qoshmaymiz, u avtomat tarzda 1 kurs boladi 
        #biz talabaga ism, familiya... larni kiritganda bosqichni kiritmaymiz.
    
    def get_info(self):
        return f"ismi: {self.ism}, familiya: {self.familiya}, tugilgan yil: {self.tyil}, {self.bosqich}-bosqich talabasi"

    def get_name(self):
        return self.ism

    def get_familiya(self):
        return self.familiya
    
    def get_age(self, yil):
        return yil - self.tyil

    #talabaning kursini yangilovchi method
    def set_bosqich(self, yangi_bosqich):
        self.bosqich =  yangi_bosqich

    def uptade_bosqich(self):
        """talabaning bosqichini bittaga kopaytirish"""
        self.bosqich += 1

    


talaba1 = Talaba('olim', 'olimov', 2000)
talaba2 = Talaba('ali', 'valiyev', 2000)
talaba3 = Talaba('valijon', 'asadov', 2000)

#lekin biz talabani bosqich tekshirdagan bolsak 
#print(talaba1.bosqich) #bu tavfsiya etilmaydi undan ism , familiya ... lar uchun alohida methodlar yaratganimiz maqul

#bu tavfsiya etilmaydi undan ism , familiya ... lar uchun alohida methodlar yaratganimiz maqul
print(talaba3.get_name())

#bu yerda bosqichni ozgartirsak boladi
talaba1.bosqich = 2 #lekin bu tavfsiya qilinmaydi
print(talaba1.get_info())

#set_bosqich() methodi orqali talabaning bosqichini yangilaymiz yani ozgaritramz
talaba1.set_bosqich(3)
print(talaba1.get_info())

print("\n")
#uptade_bosqich() methodi orqali talabaning bosqichini 1 taga kopaytiradi
talaba2.uptade_bosqich() #qavslar orasiga hech narsa yozish shart emas u ozi avtomatik bosqichni 1 ga oshiradi
print(talaba2.get_info())
talaba2.uptade_bosqich()
print(talaba2.get_info())

#qoshimcha malumot agar methodlar malumot korsatuvchi method bolsa ularni yaratishda get_.... bilan boshla
#agar ular ozgartirish bolsa set_... bilan boshla

print("\n"*3)

class Fan():
    """Fan nomli class"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba): #matem faniga talabalar qoshish uchun method
        """fanga talabalar qoshish"""
        self.talabalar.append(talaba) #biz kiritgan talabani talabalar degan bosh royhatga qoshadi
        self.talabalar_soni += 1 #har gal shu method yordamida talaba qoshganimizda talabalar_soni 1 ga oshadi yani talabalar sonini korsatadi

matem = Fan("Oliy matematika") #matem degan obeykt Fan degan classga tegishli

print(matem.talabalar)
print(matem.talabalar_soni, "\n")
 


#keling talabalarni qoshaylik
matem.add_student(talaba1)
print(matem.talabalar_soni)

matem.add_student(talaba2)
print(matem.talabalar_soni)

print(matem.nomi)

#biz talabalarni ekranga chiqarmoqchimiz biz oddiygina uni chaqirish bilan chiqaraolmaymiz
#print(matem.talabalar) #[<__main__.Talaba object at 0x0000024A297A86E0>, <__main__.Talaba object at 0x0000024A297AC7D0>]

#bu usuldan ham foydalansak boladi ammo bu noqulay va bunday qilish tavfsiya etilmaydi
print(matem.talabalar[0].ism)
print(matem.talabalar[1].get_info())

