#string malumot turi "" ichiga olib yozilgan har qanday malumot string malumot turi deb ataladi

print("salom")
print("34u8324fldjsjk")
print("+-*/fdf4334")

#unicodedagi stikerlar ni dasturlash da ham bemalol ishlataolamiz
print("😁")

ism = "Azizbek"
print("mening ismmim " + ism)

ism1 = "Ahad"
familiya1 = "Qoyum"
print(ism1 + " " + familiya1)

ism_sharif = f"{ism1} {familiya1}"
print(ism_sharif)

ism2 = "Lola"
familya2 = "Zokirova"
print(f"salom mening ismim {ism2} {familya2}")
ismbek = f"salom men {ism2} {familya2} man"
print(ismbek)

print(" \t    uzun boshliq qoladi")
print("hello \tworld")

#string methodlar
# methodni chaqirish uchun (matn.method)  dan foydalanamiz

piola = "Ali"
choynak = "Valiyev"

print(piola.upper())

piolabek = piola.upper(), choynak.upper()
print(piolabek)


meva = "OLMA"
print(meva.lower())

salom = "      olma      "
print(salom.strip())
print(salom.rstrip())
print(salom.lstrip())

matn = "lorem salom nega ketib qoldi men yaxshi"
print(matn.title())
print(matn.capitalize())


#input foydalanuvchiga beriladigan savol

ismingiz = input("ismingiz nima? \n>>> ")
print("salom " + ismingiz)
print(ismingiz.capitalize())

#all 

hammasi = "    hammasi    "
print(hammasi.upper())
print(hammasi.capitalize())
print(hammasi.title())
print(hammasi.lower())
print(hammasi.strip())
print(hammasi.lstrip())
print(hammasi.rstrip())

print(" salom hammaga \nmening ismim")
print(" salom hammaga \tmening ismim")