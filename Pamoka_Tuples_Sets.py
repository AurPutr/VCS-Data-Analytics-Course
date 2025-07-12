print('==========1============')

studiju_programos = ('Biologija', 'Biofizikaa', 'Matematika', 'Chemija')
ilgiausia = len(studiju_programos[0])

for programa in studiju_programos:
    print(f'Studiju programa - {programa}')
    print(f'Programa {programa} susideda is {len(programa)} raidziu')
    if len(programa) > ilgiausia:
        ilgiausia = len(programa)
print('Ilgiausia programa susideda is raidziu: ', ilgiausia)
print('Daugiausia raidziu turintys zodziai:')
for programa in studiju_programos:
    if len(programa) == ilgiausia:
        print(programa)

# print('Ilgiausios programos yra: ', ilgiausios_programos)

print('==========2============')

print('======1variantas======')
# menesiai = ("Sausis", "Vasaris", "Kovas", "Balandis", "Gegužė", "Birželis",
#             "Liepa", "Rugpjūtis", "Rugsėjis", "Spalis", "Lapkritis", "Gruodis")
#
# ziema1 = []
# vasara1 = []
# pavasaris1 = []
# ruduo1 = []
#
# ziema1.append(menesiai[-1])
# ziema1.append(menesiai[0:2])
# ziema= tuple(ziema1)
#
# print('Ziema: ', ziema)
#
# pavasaris1.append(menesiai[2:5])
#
# pavasaris = tuple(pavasaris1)
# print('Pavasaris: ', pavasaris)
#
# vasara1.append(menesiai[5:8])
# vasara = tuple(vasara1)
# print('Vasara: ', vasara)
#
# ruduo1.append(menesiai[8:11])
# ruduo = tuple(ruduo1)
# print('Ruduo: ', ruduo)

print('======2variantas======')
menesiai = ("Sausis", "Vasaris", "Kovas", "Balandis", "Gegužė", "Birželis",
            "Liepa", "Rugpjūtis", "Rugsėjis", "Spalis", "Lapkritis", "Gruodis")

ziema = menesiai[0:2] + menesiai[-1:]
vasara = menesiai[2:5]
pavasaris = menesiai[5:8]
ruduo = menesiai[8:11]

for indeksas, menesis in enumerate(ziema, start=1):
    print(indeksas, menesis)

print('Ziema: ', ziema)
print('Vasara: ', vasara)
print('Pavasaris: ', pavasaris)
print('Ruduo: ', ruduo)

print('==========1============')
likuciai = [3, 2, 20, 8, 42, 10, 2, 2, 36, 1, 0, 4, 3, 5, 6, 8]
unikalios_vertes = set(likuciai)

print(unikalios_vertes)

skaiciai = {2, 5, 80, 9, 9, 10, 80, 65, 2, 2, 10, 9}
print(skaiciai)
for sk in skaiciai:
    print(sk + 10)

zodziai = {'kate', 'pele', 'kede', 'biciulis', 'puodelis', 'knyga', 'apelsinas'}
daiktai = {'kede', 'stalas', 'pele', 'kate', 'knyga', 'TV', 'rasiklis'}

unikalus_zodziai = zodziai | daiktai
print('Unikalus zodziai:', unikalus_zodziai)

pasikartojantys_zodziai = zodziai & daiktai
print('Pasikartojantys zodziai:', pasikartojantys_zodziai)


#
# vardas = input('Iveskite savo varda: ')
# print('Tiesa' if vardas == 'Gintare' else 'Melas')
# sar0 = [1,2,3,1]
# sar1 = [x-10 for x in sar0]
# sar2 = {x-10 for x in sar0}
# print(sar0)
# print(sar1)
# print(sar2)
# Nelyginius saraso skaicius pakelkite kvdratu, o kitus skaicius pakelkite kubu ir sudekite i nauja sarasa.
# sarasas = [1,2,3,54,5,6,7,8]
# print(sarasas)
#
# mod0 = []
# for sk in sarasas:
#     if sk%2!=0:
#         mod0.append(sk**2)
#     else:
#         mod0.append(sk**3)
# print(mod0)
#
# mod1=[sk**2 if sk%2!=0 else sk**3 for sk in sarasas]
# print(mod1)
# atsakymas0 = []
# for i in sarasas:
#     if i%2!=0:
#         atsakymas0.append(f'{i} - nelyginis')
#     else:
#         atsakymas0.append(f'{i} - lyginis')
#
# atsakymas1 = [f'{i} - nelyginis' if i%2!= 0 else f'{i} - lyginis' for i in sarasas]
# print(atsakymas0)
# print(atsakymas1)