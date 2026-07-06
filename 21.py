#funksiyaga royhat uzatish 
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"{ism}ning bahosini qoying: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)