import random

print('=============================================')
def pasisveikinimas():
    print('Sveiki atvyke!')

def pagalba():
    print('Kuo galetume siandien jums padeti?')

def bendras():
    pasisveikinimas()
    pagalba()
    print('Aciu kad lankotes pas mus!')
    print()

bendras()

print('=============================================')

from random import randint

def suma():
    skaicius1 = randint(1,20)
    skaicius2 = randint(1,20)
    print(f'{skaicius1} + {skaicius2} = {skaicius1+skaicius2}')

for sk in range(5):
    suma()

print('=============================================')

def didesnis(a,b):
    if a > b:
        print(f'skaicius {a} yra didesnis nei skaicius {b}')
    elif b > a:
        print(f'skaicius {b} yra didesnis nei skaicius {a}')
    else:
        print(f'skaiciai {a} ir {b} yra lygus')

for sk in range(4):
    skaicius1 = randint(1,20)
    skaicius2 = randint(1,20)
    didesnis(skaicius1,skaicius2)

print('=============================================')

def suma(a,b):
    suma = a + b
    print(f'{a} + {b} = {a+b}')

def skirtumas(a,b):
    skirumas = a - b
    print(f'{a} - {b} = {a - b}')

def sandauga(a,b):
    sandauga = a * b
    print(f'{a} * {b} = {a * b}')

def dalyba(a,b):
    dalyba = round(a / b,2)
    print(f'{a} / {b} = {a / b}')

def skaiciai():
    skaicius1 = randint(1,10)
    skaicius2 = randint(1,10)
    print('Pirmasis skaicius yra: ', skaicius1)
    print('Antrasis skaicius yra: ', skaicius2)
    print('Skaicius suma: ')
    suma(skaicius1, skaicius2)
    print('Skaiciu skirtumas: ')
    skirtumas(skaicius1, skaicius2)
    print('Skaiciu sandauga: ')
    sandauga(skaicius1, skaicius2)
    print('Skaiciu dalyba: ')
    dalyba(skaicius1,skaicius2)

for kartai in range(3):
    skaiciai()

print('=============================================')

# def studento_info(vard, pavard, masyvas):
#     print('Vardas: ', vard)
#     print('Pavarde: ', pavard)
#     print('Pazymiai\n', masyvas)
#     vidurkis = sum(masyvas)/len(masyvas)
#     print('Pazymiu vidurkis: ', vidurkis)
#
# vardas = input('Iveskite studento varda: ')
# pavarde = input('Iveskite studento pavarde: ')
# pazymiai = [8, 7, 6, 9, 10, 10, 9, 7, 6, 10]
#
# studento_info(vardas, pavarde, pazymiai)


print('=============================================')
def skaiciu_suma(masyvas):
    suma = 0
    for sk in masyvas:
        suma += sk
    return suma

pazymiai = [8, 7, 6, 9, 10, 10, 9, 7, 6, 10]
pazymiai2 = [8, 7, 6, 6, 10, 7, 9, 7, 8, 9]

bendra_suma = skaiciu_suma(pazymiai)
bendra_suma2 = skaiciu_suma(pazymiai2)
print('Bendra I-ojo studento pazymiu suma yra: ', bendra_suma)
print('Bendra II-ojo studento pazymiu suma yra: ', bendra_suma2)

if bendra_suma > bendra_suma2:
    print(f'I-ojo studendo pazymiu suma yra didesne: {bendra_suma}')
elif bendra_suma2 > bendra_suma:
    print(f'II-ojo studendo pazymiu suma yra didesne: {bendra_suma2}')
else:
    print(f'Abu studentai turi vienoda pazymiu suma: {bendra_suma}')


print('=============================================')

def didziausi_sk(sarasas):
    didziausias = sarasas[0]
    for sk in sarasas:
        if sk > didziausias:
            didziausias = sk
    return didziausias

def kartai_didz(sarasas,didziausias):
    kiek = 0
    for sk in sarasas:
        if sk == didziausias:
            kiek += 1
    return kiek
def maziausi_sk(sarasas):
    maziausias = sarasas[0]
    for sk in sarasas:
        if sk < maziausias:
            maziausias = sk
    return maziausias
def kartai_maz(sarasas,maziausias):
    kiek = 0
    for sk in sarasas:
        if sk == maziausias:
            kiek += 1
    return kiek

def vidurkis(sarasas):
    vidurkis = sum(sarasas)/len(sarasas)
    return round(vidurkis, 1)

from random import randint
def saraso_kurimas(kiek = 11):
    listas = []
    for sk in range(11):
        listas.append(randint(1, 10))
    return listas
def spausdinimas(maziausias,kartai, komentaras):
    print(maziausias)
    print(f'Sarase {komentaras} skaicius pakartotas: {kartai} kartu')

listas = saraso_kurimas()
print(listas)
didziausias = didziausi_sk(listas)

kartai = kartai_didz(listas,didziausias)
spausdinimas(didziausias,kartai, 'didziausias')
maziausias = maziausi_sk(listas)
kartai = kartai_maz(listas,maziausias)
spausdinimas(maziausias, kartai, 'maziausias')

vid = vidurkis(listas)
print(vid)

print('=============================================')

# def vertinimas(sarasas):
#     sarasas.sort(reverse=True)
#     for i, s in enumerate(sarasas, start=1):
#         if s == 10:
#             print(i,'.', s, '- Puiku')
#         elif s >= 9:
#             print(i,'.', s, '- Labai gerai')
#         elif s >= 7:
#             print(i,'.', s, '- Gerai')
#         elif s >= 5:
#             print(i,'.', s, '- Patenkinamai')
#         elif s < 5:
#             print(i,'.', s, '- Neigiamas')
#
# pazymiai = []
# for pazymys in range(11):
#     pazymiai.append(randint(2, 10))
# print('Pazymiu sarasas: ', pazymiai)
# prideti = input('Ar norite prideti pazymiu i sarasa? (taip/ne): ')
# while prideti == 'taip':
#     kiekis = int(input('Kiek pazymiu noresite prideti?: '))
#     for sk in range(kiekis):
#         naujas = int(input('Iveskite pazymi, kuri norite prideti: '))
#         pazymiai.append(naujas)
#     print('Atnaujintas pazymiu sarasas: ', pazymiai)
#     prideti = input('Ar norite prideti pazymiu i sarasa? (taip/ne): ')
# vertinimas(pazymiai)

# import sqlite3
# conn = sqlite3.connect('manoDB.db')
# c = conn.cursor()