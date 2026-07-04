#(FUNCTIONS) --- funksiyalar
#malum bir kop ishlatiladigan jumlalarni qayta qayta yozmaslik uchun funksiyadan foydalanamiz
#misol uchun print() funksiyasi biz oddiygina print deb yozb malumotlarni ekranga chiqaramiz ammo uning orqasida qator-qator codelar bor

# #def --- funksiya yaratish
# def salom_ber(): #bu funksiyani qayerga yozsak assalomu alaykum deb ekranga chiqadi
#     """salom beruvchi funksiya""" #funksiya haqida malumot bu dasturchilar funksiyamizni oson tushunishi uchun
#     print('assalomu alaykum')

# salom_ber() #funksiyaga nom berganda koproq biror bir harakatni anglatuvchi nomlardan foydalan keyinchalik chalkashib ketmaslik va osongina ajratib olish uchun

# #foydalanuvchidan ism sorasn va ismi bilan salom bersin
# def salom_ber(ism): #parametr
#     """foydalanuvchidan ism sorab,
#      unga salom beruvchi funksiya""" 
#     print('assalomu alaykum')
#     print(f"salom, hurmatli {ism.title()}")

# salom_ber('hasan')
# salom_ber('aziz')

#!!!!! eslab qol agar sen yaratgan funksiya juda murakkab bolsa sen unga doim batafsil malumot ber bu ("""""") orqali

# #funksiyaning tarifini korish
# print(salom_ber.__doc__)

# def toliq_ism(ism, familiya): #mana 
#     """foydalanuvchini ismini va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"foydalanuvchining ismi: {ism.title()}\n"
#           f"foydalanuvchining familiyasi: {familiya.title()}")

# toliq_ism('aziz', 'kholdaraliyev') #ketma ketlikka doim amal qil birinchi isim, ikkinchi familiya chunki tepada shunday tartibda yozgansan

# #yoki tartibni buzmaslik uchun parametr nomi bilan qiymat kirit:
# toliq_ism(familiya="hasanov", ism='ali')


#yoshni hisoblovchi funksiya
def yosh_hisobla(tugilgan_yil, joriy_yil=2026): #foydalanuvchi joriy_yilga qiymat kiritmasaham u 2026- yilni olaveradi
    """foydalanuvchini tugilgan yilidan uning yoshini hisoblaydi"""
    print(f"siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(2009)