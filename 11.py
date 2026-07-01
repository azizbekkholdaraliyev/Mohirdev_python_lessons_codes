#bu darsimizda if operatorini chuqurroq korib chiqdik

#bu hayvonot bogiga kirish uchun tonaladigan pul --- yosh orqali
yosh = int(input("yoshingiz nechida? "))
if yosh<=4:
    print("sizga kirish bepul")
elif yosh<=12:
    print("kirish 5 ming som")
else:
    print("kirish 10 ming som")

#dasturchilar dasturlarni qisqartirish va ozlariga qulay qilish uchun bunday yozishadi
yosh = int(input("yoshingiz nechida? "))
if yosh<=4:
    narx = 0
elif yosh<=12:
    narx = 5000
elif yosh<=16:
    narx = 8000
elif yosh<=18:
    narx = 10000
else:
    narx = 15000
print(f"sizga kirish {narx} so'm")

#bizda bir vaqtni ozida bir nechta shartlarni bajarilishini talab qilishi mumkin
# or / and
kun = input('bugun nima kun? \n>>>')
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print('bugun dam olish kuni')
else:
    print('bugun ish kuni')

#bir vaqtni ozida ikkita shartni tekshirmoqchi bolsak -and- dan foydalanamiz
day = input('bugun nima kun? \n>>>') 
temp = float(input('harorat qanday? \n>>>'))

if day.lower() == 'yakshanba' and temp>=30:
    print('cho\'milgani ketdik')
elif day.lower() == 'yakshanba' and temp<30:
    print('uyda dam olamiz')

today = input('bugun nima kun? \n>>>') 
tempura = float(input('harorat qanday? \n>>>'))

if (today.lower() == 'shanba' or today.lower() == 'yakshanba') and tempura>=30:
    print('cho\'milgani ketdik')
elif (today.lower() == 'shanba' or today.lower() == 'yakshanba') and tempura<30:
    print('uyda dam olamiz')

#boolen malumot turi --- bitta shart bajarilsa boldi qolgan shartlarni tekshirib otirmaydi
narh = 15000 #mijoz ovqat sotib oldi
choy = True
salat = False #agar boz salatni True qilsak  (choy and salat) ikkisi ham sotib olinganligi uchun 25 ming som boladi

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000

print(f"jami {narh} som boldi")

#quyidagi har bir shart alohida tekshiriladi va bir biriga bogliq emas
narxi = 15000 #mijoz ovqat sotib oldi
salad = True
free = True
kokteyl = False
tea = False
pizza = True

if salad:
    print('mijoz salad oldi')
    narxi = narxi + 5000
if free:
    print('mijor kartoshka free oldi')
    narxi = narxi + 10000
if kokteyl:
    print('mijor kokteyl sotib oldi')
    narxi = narxi + 15000
if tea:
    print('mijoz tea sotib oldi')
    narxi = narxi + 2000
if pizza:
    print('mijoz pizza sotib oldi')
    narxi = narxi + 50000
print(f"jami {narxi} som ")

#mijoz ovqat soraydi agar u ovqat berilgan menuda bolsa buyurtma qabul qilindi deydi unday bolmasa bizga unday ovqat yoq degan javob qaytaradi
#in / not in
menu = ['osh', 'manti', 'kabob', 'somsa', 'shurva']
ovqat = input('nima ovqat yeysiz? \n>>>')
if ovqat.lower() in menu:
    print('buyurtma qabul qilindi')
elif ovqat.lower() not in menu:
    print('bizda bunday ovqat yoq')


#mijoz bir nechta ovqat aytadi ular menuda bor yoki yoqligini aytib beradi bu dastur
menyu = ['osh', 'manti', 'kabob', 'somsa', 'shurva']
foods = ['osh', 'somsa', 'mastava', 'grechka', 'kabob']
if foods: #agar royhatda bitta bolsa ham ovqat bolsa bu ifoda true qaytaradi
    for food in foods:
        if food in menyu:
            print(f"menyuda {food} bor")
        else:
            print(f"menyuda {food} yoq")
else: #agar royhat bosh bolsa
    print('royhat bosh')