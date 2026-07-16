# from uuid import uuid4


# class Avto:
#     """Avtomobil klassi"""

#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4() # __id yaniki foydalanuvchiga bir marta id beriladi va uni umuman ozgartirib bolmaydi.

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")


# # avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# # print(f"ID: {avto1.get_id()}")
# # avto1.add_km(1500)
# # print(avto1.get_km())

from uuid import uuid4


class Avto:
    """Avtomobil klassi"""

    __num_avto = 0   #bu Avto classiga tegishli
    # PI = 3.14159  #bu yerga ozgarmas qiymatlarni ham kirib qoyish mumkin va ularni obeykt yaratganda foydalanish ham mumkin

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1 #foydalanuvchi bizni classimizdan foydalanib obeykt yaratsa num_avto bitta ga kopayadi

    @classmethod
    def get_num_avto(cls): #bu yerda biz self deb obeyktni emas cls deb class ni uzatayapmiz
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")


class Bus:
    pass


class Train:
    pass