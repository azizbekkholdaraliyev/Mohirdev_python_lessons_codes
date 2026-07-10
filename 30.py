#Vorislik --- bir classdan boshqa bir yangi class yaratish
#Polimorfizm --- yangi yaratilgan classni ichida superclassdan biror bir argumentni ozgartirish

class Shaxs:
    """shaxslar haqida malumot"""
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism 
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """shaxs haqida malumot"""
        info = f"{self.ism} {self.familiya}"
        info += f"{self.passport}, {self.tyil}"
        return info
    def get_age(self, yil):
        """shaxsning yoshini korsatish uchun"""
        return yil - self.tyil

#classni meros qlb olganda undagi methodlar ham birga meros qlb olinadi (shaxsdagi methodni Talaba classida ham ishlatsa boladi)

class Talaba(Shaxs): #bu yerda Shaxs - super class / Talaba - voris class    deb ataladi
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil): #idraqam - talabaning id raqami
        """talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil) #bu malumotlar superklassdan meros bolib otypati yaniki Shaxs clasidan
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil #buni ichida qishloq, kocha, uy raqami larini alohida class yaratib manzilga saqlashimiz mumkin
    def get_id(self):
        """talabaning id raqami"""
        return self.idraqam
    def get_bosqich(self):
        """talabaning oqish bosqichi"""
        return self.bosqich
#Polimorfizm --- oldingi methodni ozgartirmoqchi bolsak 
    def get_info(self):
        """shaxs haqida malumot"""
        info = f"{self.ism} {self.familiya}"
        info += f"{self.bosqich}, {self.idraqam}"
        return info

class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """manzilni korish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani"
        manzil += f"{self.kocha} kochasi, {self.uy}-uy"
        return manzil

talaba1_manzil = Manzil(26, "istiqlol", 'bagdod', 'fergana')
talaba1 = Talaba('vali', 'farizov', 'KH323', '2000', 'dk23233433', talaba1_manzil)

talaba1.Talaba.get_manzil()