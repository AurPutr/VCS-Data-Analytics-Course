print('============1============')
# sarasas = ['Jonas', 'Petras', 'Antanas', 'Jurga', 'Stase']
#
# print('Pilnas sarasas: ', sarasas)
# print('Pirmasis narys: ', sarasas[0])
# print('Paskutinis narys:', sarasas[len(sarasas)-1])
# print('Viso sarase nariu: ', len(sarasas))

print('============2============')
# ugis = []
# ugis.append(1.80)
# ugis.append(1.65)
# ugis.extend([1.76, 1.98, 1.69])
# print('Ugiu sarasa: ', ugis)
# print('saraso ilgis: ', len(ugis))

print('============3============')
# pazymiai = []
# kiekis = int(input('Iveskite kiek pazymiu noresite ivesti: '))
#
# for sk in range(kiekis):
#     pazymys = int(input('Iveskite norima pazymi (atskirkite su enter): '))
#     pazymiai.append(pazymys)
# print('Pazymiu sarasas: ', pazymiai)
# print('Viso pazymiu yra: ', len(pazymiai))

print('============4============')
# miestai = ['Vilnius', 'Kaunas', 'Klaipeda', 'Druskininkai', 'Kernave', 'Birzai']
# print('Esamas miestu sarasas: ', miestai)
# prideti = input('Ar norite prideti miesta i sarasa? (taip/ne): ')
# while prideti == 'taip':
#     naujas = input('Iveskite miesto pavadinima, kuri norite prideti: ')
#     vieta = int(input('Nurodykite i kuria pozicija norite prideti miesta: '))
#     miestai.insert(vieta, naujas)
#     print('Atnaujintas miestu sarasa: ', miestai)
#     prideti = input('Ar norite prideti miesta i sarasa? (taip/ne): ')
# print('Galutinis miestu saras: ', miestai)
# print('Miestu saraso ilgis: ', len(miestai))

print('============5============')
# amzius = [23, 56, 26, 34, 67, 81]
# print('Dalyviu amziaus sarasas: ', amzius)
# # amzius.pop(4)
# # print('Atnaujintas dalyvius amziaus sarasas: ', amzius)
# pasalinti = input('Ar norite pasalinti irasa is saraso? (taip/ne): ')
# while pasalinti == 'taip':
#     pozicija = int(input('Iveskite pozicija iraso, kuri norite pasalinti: '))
#     amzius.pop(pozicija-1)
#     print('Atnaujintas dalyvius amziaus sarasas: ', amzius)
#     pasalinti = input('Ar norite pasalinti irasa is saraso? (taip/ne): ')
# print('Galutinis dalyvius amziaus sarasas: ', amzius)
# print('Dalyviu amziaus saraso ilgis: ', len(amzius))


print('============6============')
# daiktai = ['kede', 'stalas', 'knyga', 'TV', 'rasiklis']
# print('Daiktu sarasas: ', daiktai)
#
# if len(daiktai) > 5:
#     print('Saraso ilgis: ', len(daiktai))
#     print('Sarasas ilgesnis nei 5 irasai, todel buvo istrintas')
#     daiktai.clear()
#     print('Daiktu sarasas: ', daiktai)
#
# else:
#     print('Sarasas trumpesnis nei 5 irasai')
#     print('Daiktu sarasas: ', daiktai)
#     print('Saraso ilgis: ', len(daiktai))


print('============7============')
# zodziai = ['kate', 'pele', 'biciulis', 'puodelis', 'knyga', 'apelsinas']
#
# ieskomas_zodis = input('Iveskite ieskoma zodi: ')
# if ieskomas_zodis in zodziai:
#     print(f'{ieskomas_zodis} buvo rastas sarase')
#     print('Zodziu sarasas: ', zodziai)
#     print(zodziai.index(ieskomas_zodis))
# else:
#     print(f'{ieskomas_zodis} nebuvo rastas sarase')
#     print('Zodziu sarasas: ', zodziai)


print('============8============')
# pazymiai = [10, 8, 9, 8, 10, 6, 10]
# print('Pazymiu sarasas: ', pazymiai)
# prideti = input('Ar norite prideti pazymiu i sarasa? (taip/ne): ')
# while prideti == 'taip':
#     kiekis = int(input('Kiek pazymiu noresite prideti?: '))
#     for sk in range(kiekis):
#         naujas = int(input('Iveskite pazymi, kuri norite prideti: '))
#         pazymiai.append(naujas)
#     print('Atnaujintas pazymiu sarasas: ', pazymiai)
#     prideti = input('Ar norite prideti pazymiu i sarasa? (taip/ne): ')
# print('Galutinis pazymiu sarasas: ', pazymiai)
# print('Studentas is viso turi: ', pazymiai.count(10), 'desimtuku')


print('============9============')
# automobiliai = ['Audi', 'Toyota', 'BMW']
# print('Automobiliu sarasas: ', automobiliai)
# prideti = input('Ar norite prideti automobiliu markiu i sarasa? (taip/ne): ')
# while prideti == 'taip':
#     masina = input('Iveskite automobilio marke, kuria norite prideti: ')
#     automobiliai.append(masina)
#     print('Atnaujintas automobiliu markiu sarasas: ', automobiliai)
#     prideti = input('Ar norite prideti automobiliu markiu i sarasa? (taip/ne): ')
# automobiliai.sort()
# print('Galutinis automobiliu markiu sarasas: ', automobiliai)
# automobiliai.sort(reverse=True)
# print('Galutinis automobiliu markiu sarasas: ', automobiliai)

print('============10============')
# pazymiai = [10, 6, 8, 8, 8, 10, 5]
# print('Studento pazymiu sarasas: ', pazymiai)
# pazymiai.sort(reverse=True)
# print('Trys didziausi pazymiai: ', pazymiai[0], pazymiai[1], pazymiai[2])


print('============11============')
# pazymiai = [10, 6, 3, 8, 8, 4, 4, 5]
#
# print('Studento pazymiu sarasas: ', pazymiai)
# neigiami = []
# for pazymys in pazymiai:
#      if pazymys < 5:
#         neigiami.append(pazymys)
#
# print('Neigiamu studento pazymiu sarasas: ', neigiami)
# print(f'Studentas turi {len(neigiami)} neigiamu ivertinimu')


print('========PVZ=========')
matrica = [
[8, 7, 5, 3],
[4, 7, [[4, 7, 8, 3], 7, 5, 3], 2],
[4, 7, 8, 3],
[5, 2, 3, 1]
]
print(matrica)
mat_eil = matrica[1]
print(mat_eil)
print(mat_eil[2])
print(mat_eil[2][0])
print(mat_eil[2][0][-1])







print('============12============')
list = [2, 5, 98, 8, 53, 65, 47, 35, 6]

print(list[:3])
print(list[2:4])
print(list[-4::])
print(list[2:7:2])

print(list[::-1])



print('============13============')
list = [5, 9, 4, 8, 9, 10, 6, 6, 7, 9]
highest_score = []
list.sort(reverse=True)
print(list)
highest_score.extend(list[0:3])
print(highest_score)

print('============14============')
# zodynas = []
# prideti = input('Ar norite prideti zodi i zodyna? (taip/ne): ')
# while prideti == 'taip':
#     zodis = input('Iveskite zodi kuri norite prideti: ')
#     zodynas.append(zodis)
#     zodynas.sort()
#     print(zodynas)
#     prideti = input('Ar norite dar prideti zodi i zodyna? (taip/ne): ')
# print('Galutinis zodynas: ', zodynas)

print('============15============')
likuciai = [3, 2, 20, 8, 42, 10, 2, 2, 36, 1, 0, 4, 3, 5, 6, 8]
nepakanka = []
for kiek in likuciai:
    if kiek <= 5:
        nepakanka.append(kiek)
print('Nepakankamu prekiu kiekiu sarasas: ', nepakanka)


likuciai = [['sviestas', 7],['duona', 77],['pienas', 44],['limonadas', 99],['alus', 7]]
maziausiai = []

for preke in likuciai:
    if preke[1] <= 5:
        maziausiai.append(preke)

if len(maziausiai) > 0:
    print('Prekes kuriu like maziau lygu 5 vienetai:')
    for preke in maziausiai:
        print(f'Prekes pavadinimas {preke[0]}, jos kiekis {preke[1]}')
else:
    likuciai.sort(key=lambda x: x[1])
    maziausiai = likuciai[:3]
    for preke in maziausiai:
        print(f'Prekes pavadinimas {preke[0]}, jos kiekis {preke[1]}')


print('============16============')
sarasas = ['Labas', 'vakaras', 'draugai', 'grazaus', 'jums', 'vakaro']

sakinys = ','.join(sarasas)
print(sakinys)

sakinys2 = '|'.join(sarasas)
print(sakinys2)

sakinys3 = ' '.join(sarasas)
print(sakinys3)

print('===================PVZ==================')
miestai = ['Kaunas', 'Vilnius', 'Klaipeda', 'Siauliai', 'Vilnius']
# print(miestai.index('Vilnius'))
for indeksas, miestas in enumerate(miestai, start=0): # default yra 0
    if miestas == 'Vilnius':
        print(indeksas)

print('=====================================================')
for i in range(len(miestai)):
    # print(i+1, miestai[i])
    if miestai[i] == 'Vilnius':
        print(i)

print('=====================================================')
i = 0
while i<len(miestai):
    # print(i + 1, miestai[i])
    if miestai[i] == 'Vilnius':
        print(i)
    i+=1



print('============17============')
a, b, c, *other = ['Python', 'dekstop', 'web', 'pamoka1.py', 'pamoka2.py', 'pamoka3.py']
print('Naudojama programavimo kalba: ', a)
print('Naudojamos aplinkos: ', b, 'ir', c)

print('Failai su kuriais yra dirbama: ', other)

print('============18============')
komanda = ['Jonas Jonaitis', 'Petras Petraitis', 'Saule Saulyte', 'Greta Gretaite']
print('Prie projekto dirba sie komandos nariai:')
for zmogus in komanda:
    print(zmogus)

print('============19============')
temos = ['Matematika', 'Skaiciavimai', 'Salyginiai sakiniai', 'Ciklai', 'List']
print('Mes jau mokemes:')
for sk in range(len(temos)):
    print(f'{sk + 1}-oji tema: {temos[sk]}')

print('============23============')
# pazymiai = [10, 8, 9, 8, 10, 6, 10]
# print('Pazymiu sarasas: ', pazymiai)
# prideti = input('Ar norite prideti pazymiu i sarasa? (taip/ne): ')
# while prideti == 'taip':
#     kiekis = int(input('Kiek pazymiu noresite prideti?: '))
#     for sk in range(kiekis):
#         naujas = int(input('Iveskite pazymi, kuri norite prideti: '))
#         pazymiai.append(naujas)
#     print('Atnaujintas pazymiu sarasas: ', pazymiai)
#     prideti = input('Ar norite prideti pazymiu i sarasa? (taip/ne): ')
# pazymiai.sort(reverse=True)
# for i,pazymys in enumerate(pazymiai, start=1):
#     if pazymys == 10:
#         print(i,'.', pazymys, '- Puiku')
#     elif pazymys >= 9:
#         print(i,'.', pazymys, '- Labai gerai')
#     elif pazymys >= 7:
#         print(i,'.', pazymys, '- Gerai')
#     elif pazymys >= 5:
#         print(i,'.', pazymys, '- Patenkinamai')
#     elif pazymys < 5:
#         print(i,'.', pazymys, '- Neigiamas')

print('============24============')
# from random import randint
# list = []
# kiek = int(input('Kiek skaiciu turetu sudaryti sarasa?: '))
# for sk in range(kiek):
#     list.append(randint(1,100))
# print(list)

print('============26============')
# from random import randint
# list = []
# nelyginiai = []
# lyginiai = []
# dalinasi_is3 = []
# kiek = int(input('Kiek skaiciu turetu sudaryti sarasa?: '))
# for sk in range(kiek):
#     list.append(randint(1,100))
#     if sk %3 == 0:
#         dalinasi_is3.append(sk)
#     if sk %2 == 0:
#         lyginiai.append(sk)
#     elif sk %2 != 0:
#         nelyginiai.append(sk)
# print('Visi nelyginiai skaiciai yra: ', nelyginiai)
# print('Visi lyginiai skaiciai yra: ', lyginiai)
# print('Visi skaiciai dalinasi is 3: ', dalinasi_is3)



# from random import randint
# sarasas = []
# kiek = int(input('kiek skaiciu sukurti'))
# for i in range(kiek):
#         sarasas.append(randint(1,100))
# print(sarasas)
#
# print("Lyginiai skaičiai:")
# for skaicius in sarasas:
#     if skaicius % 2 == 0:
#         print(skaicius)
#
# print("\nVisi nelyginiai skaičiai:")
# for skaicius in sarasas:
#     if skaicius % 2 != 0:
#         print(skaicius)
# print("\nVisi skaičiai, kurie dalinasi iš 3:")
# for skaicius in sarasas:
#     if skaicius % 3 == 0:
#         print(skaicius)









print('============27============')
# from random import randint
# list = []
#
# kiek = int(input('Kiek skaiciu turetu sudaryti sarasa?: '))
# for sk in range(kiek):
#     list.append(randint(1,100))
# print(list)
# suma = sum(list)
# print('suma: ', suma)
# vidurkis = suma/len(list)
# print('vidurkis yra: ', round(vidurkis, 0))
# didesni_nei_vid = []
# for sk in list:
#     if sk > vidurkis:
#          didesni_nei_vid.append(sk)
# didesni_nei_vid.sort(reverse=True)
# print(didesni_nei_vid)




######random zodziams######
# from RandomWordGenerator import RandomWord
#
# rw1 = RandomWord(max_word_size=5,
#                  constant_word_size=True,
#                  special_chars=r"@#$%.*",
#                   include_special_chars=True)
#
# print(rw1.generate())
# #
# rw2 = RandomWord()
# print(rw2.generate())
#
# import random
# from random_word import RandomWords
# r = RandomWords()
#
# # Return a single random word
# print(r.get_random_word())
# atsitiktiniai_zodziai = []
# kiek = random.randint(1,20)
# for i in range(kiek):
#       atsitiktiniai_zodziai.append(r.get_random_word())
# print(atsitiktiniai_zodziai)

# https://pypi.org/project/Random-Word/
# https://pypi.org/project/Random-Word-Generator/


print('============32============')
zodziai = ['amazonism', 'socializations1', 'besmoothed', 'unrepining', 'papalize', 'prohuman', 'wrongheadedness', 'cheder', 'telpherway', 'coenobitism', 'rontgenology', 'aboveproof', 'aldm', 'isothermally']
ilg_z = zodziai[0]
# print(ilg_z)

for zodis in zodziai:
    if len(zodis) > len(ilg_z):
        ilg_z = zodis
print('Ilgiausio zodzio raidziu kiekis', len(ilg_z))

for zodis in zodziai:
    if len(zodis) == len(ilg_z):
        print(zodis)

trump_z = zodziai[0]
# print(trump_z)

for zodis in zodziai:
    if len(zodis) < len(trump_z):
        trump_z = zodis
print('Trumpiausio zodzio raidziu kiekis: ', len(trump_z))

for zodis in zodziai:
    if len(zodis) == len(trump_z):
        print(zodis)


print('============33============')
from random import randint
skaiciai = []
for sk in range(101):
    skaiciai.append(randint(1, 100))
didziausias = skaiciai[0]
maziausias = skaiciai[0]

for sk in skaiciai:
    if sk > didziausias:
        didziausias = sk
print('Didziausias skaicius yra: ', didziausias)
for sk in skaiciai:
    if sk == didziausias:
        print('Sarase didziausias skaicius pakartotas: ', skaiciai.count(didziausias), 'kartu')

for sk in skaiciai:
    if sk < maziausias:
        maziausias = sk
print('Maziausias skaicius yra: ', maziausias)
for sk in skaiciai:
    if sk == maziausias:
        print('Sarase maziausias skaicius pakartotas: ', skaiciai.count(maziausias), 'kartu')

vidurkis = sum(skaiciai) / len(skaiciai)
print('Sarase esanciu skaiciu vidurkis yra: ', round(vidurkis, 1))

zemesni_vid = []
for sk in skaiciai:
    if sk < vidurkis:
        zemesni_vid.append(sk)
print('Zemesniu nei vidurkis skaiciu sarasas susideda is :', len(zemesni_vid))
print(zemesni_vid)

didesni_vid = []
for sk in skaiciai:
    if sk > vidurkis:
        didesni_vid.append(sk)
print('Didesniu nei vidurkis skaiciu sarasas susideda is :', len(didesni_vid))
print(didesni_vid)

print('Pradiniai duomenys:')
print('Maziausias skaicius: ', maziausias)
print('Didziausias skaicius: ', didziausias)
print('Saraso vidurkis: ', round(vidurkis,2))
mazesniu_vidurkis = sum(zemesni_vid) / len(zemesni_vid)
didesniu_vidurkis = sum(didesni_vid) / len(didesni_vid)
print('Didesniu skaiciu vidurkis: ', round(didesniu_vidurkis,2))
print(didesni_vid)
print('Mazesniu skaiciu vidurkis: ', round(mazesniu_vidurkis,2))
print(zemesni_vid)


print('============34============')
zodziai = ['amazonism', 'socializations', 'besmoothed', 'unrepining', 'papalize', 'prohuman', 'wrongheadedness', 'cheder', 'telpherway', 'coenobitism', 'rontgenology', 'aboveproof', 'aldm', 'isothermally']
ilgiausias = zodziai[0]
trumpiausias = zodziai[0]

for zodis in zodziai:
    if len(zodis) > len(ilgiausias):
        ilgiausias = zodis
for zodis in zodziai:
    if len(zodis) == len(ilgiausias):
        print('Ilgiausias zodis yra: ', ilgiausias)
        print('Sis zodis turi: ', len(ilgiausias), 'raidziu')
for zodis in zodziai:
    if len(zodis) < len(trumpiausias):
        trumpiausias = zodis
for zodis in zodziai:
    if len(zodis) == len(trumpiausias):
        print('Trumpiausias zodis yra: ', trumpiausias)
        print('Sis zodis turi: ', len(trumpiausias), 'raidziu')

print(f'Ilgiausias "{ilgiausias}" {len(ilgiausias)} raidziu, o trumpiausias "{trumpiausias}" {len(trumpiausias)}, skirtumas tarp ju {len(ilgiausias)} - {len(trumpiausias)} = {len(ilgiausias) - len(trumpiausias)} simboliai')

print('============40============')
from random import randint
skaiciai = []
for sk in range(21):
    skaiciai.append(randint(1, 100))
dalinasi3 = []
print(skaiciai)
for sk in skaiciai:
    if sk %3 == 0:
        dalinasi3.append(sk)
print(dalinasi3)
suma = sum(dalinasi3)
vidurkis = suma / len(dalinasi3)
print('Saraso suma: ', suma)
print('Saraso vidurkis: ', round(vidurkis, 2))



