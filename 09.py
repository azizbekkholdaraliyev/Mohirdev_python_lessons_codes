#for sikli
mehmonlar = ['ali', 'asad', 'aziz', 'hasan', 'lola']

print('salom', mehmonlar[0])
print('salom', mehmonlar[1])
print('salom', mehmonlar[2])

#for bilan qilsak hamma uchun alohida salom berishimiz shart emas
print('for sikli --------- ')

for mehmon in mehmonlar:
    print('salom', mehmon)
#printni oldidagi bosh joy for ning badani hisoblanadi agar bu ochiq joy bolamasa, fordan tashqarida hisoblanadi va codening oxirida bitta bolib chiqadi

#example
ismlar = ['ali', 'asad', 'aziz', 'hasan', 'lola']

for ism in ismlar:
    print('salom', ism, 'nima gap tinchmi')
    print('hayr', ism)

#sonlar bilan

sonlar = list(range(0,11))

for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

#example 2
numbers = list(range(11))
raqamlar = []

for num in numbers:
    raqamlar.append(num**2)

print(numbers)
print(raqamlar)

#example 3: dostlar royhatini tuzib beradigan kichik dasturcha
doslar = []
print('dost qoshing:')
for n in range(5):
    doslar.append(input(f"{n+1}-dostingizni kriting: "))
print(doslar)
