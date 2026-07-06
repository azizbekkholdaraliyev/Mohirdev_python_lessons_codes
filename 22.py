#moslasuvchan funksiya

#foydalanuvchi istagancha argument kritsin biz avvalgi darsimizda biz funksiyada nechta argument soragan
#bolsak shuncha argument kritilishi kerak edi

# def summa(*sonlar):  #foydalanuvchi hohlagancha argument kritishi mumkin
#     """kiritilgan sonlar yigindisini hisoblovchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
    
# print(summa(1,2))
# print(summa(1,2,3,4))
# print(summa(2,3,1,8,1))



# def summa(x,y,*sonlar):  #foydalanuvchi bu yerda x va y ga argument kritishi shart qolgani hohishiga bogliq
#     """kiritilgan sonlar yigindisini hisoblovchi funksiya"""
#     return x+y+sum(sonlar)
    
# print(summa(1,2))
# print(summa(1,2,3,4))
# print(summa(2,3,1,8,1))

# print(summa(3)) #bu yerda sen 2 ta argument kritishing shart shuning uchun bu xato

def avto_info(kompaniya, model, **malumotlar): # 2 cha bilan yozdik bu **malumotlar degan lugat yaratdi
    """avto haqidagi malumotlarni lugat korinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info('GM', 'malibu', rang='qora', karobka='avto')
avto2 = avto_info('kia', 'k5', rang='qizil', karobka='mexanik', yil=2020)

print(avto1)
print(avto2)