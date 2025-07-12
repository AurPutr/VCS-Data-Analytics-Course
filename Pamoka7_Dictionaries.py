# knyga = {
# 'autorus': 'Jey k rauling',
# 'pavadinimas': 'toks ir anoks pasaulis',
# 'puslapiai': 245,
# 'kaina': 14.99,
# 'ar_prekyboje': True,
# }
# raktas = input('Kokios savybes apie knyga ieskote? ')
# # print(knyga[raktas])
# if knyga.get(raktas) == None:
#     print('Ivedete netinkama savybe')
# else:
#     print(knyga.get(raktas))
# print('labukas')
import datetime

print('===============1=========')
studentas = {'vardas':'Lukas',
             'pavarde':'Lukaitis',
             'amzius':23,
             'studiju programa':'biologija',
             'atsiskaitytu kreditu skaicius':10,
             'pazymiai':[7,8,7,9,10,6,9,10,7,8],
             'ugis':1.95,
             'kelintas kursas':3,
             'mokyklos pavadinimas':'VU'}
print(studentas)
for pozymis in studentas:
    print(f'{pozymis} : {studentas[pozymis]}')

print('===============3=========')
knyga1 = {'pavadinimas': 'Dievu miskas',
          'autorius':'Balys Sruoga',
          'zanras':'Atsiminimai',
          'kaina':26,
          'knygos apimtis': {
            'puslapiu kiekis':150,
            'skyriu skaicius':10
          },
          'isleidimo metai':2006,
          'ar galima rasti knygynuose':True}
knyga2 = {'pavadinimas': 'Begedziai',
          'autorius':'Beata Tiskevic',
          'zanras':'Romanas',
          'kaina':20,
          'knygos apimtis': {
            'puslapiu kiekis':115,
            'skyriu skaicius':15
          },
          'isleidimo metai':2022,
          'ar galima rasti knygynuose':True}
print('Knyga: ', knyga1)
print('Knyga: ', knyga2)
if knyga1 ['isleidimo metai'] < knyga2 ['isleidimo metai']:
    print(f'Knyga {knyga1['pavadinimas']} isleista {knyga1['isleidimo metai']} ir ji yra senesne nei knyga {knyga2['pavadinimas']}')
else:
    print(f'Knyga {knyga2['pavadinimas']} isleista {knyga2['isleidimo metai']} ir ji yra senesne nei knyga {knyga1['pavadinimas']}')

if knyga1['knygos apimtis']['puslapiu kiekis'] > knyga2['knygos apimtis']['puslapiu kiekis']:
    print(f'Knyga {knyga1['pavadinimas']} turi daugiau puslapiu nei knyga {knyga2['pavadinimas']} ')
else:
    print(f'Knyga {knyga2['pavadinimas']} turi daugiau puslapiu nei knyga {knyga1['pavadinimas']} ')

if knyga1['knygos apimtis']['skyriu skaicius'] > knyga2['knygos apimtis']['skyriu skaicius']:
    print(f'Knyga {knyga1['pavadinimas']} turi daugiau skyriu nei knyga {knyga2['pavadinimas']} ')
else:
    print(f'Knyga {knyga2['pavadinimas']} turi daugiau skyriu nei knyga {knyga1['pavadinimas']} ')

if knyga1['kaina'] > knyga2['kaina']:
    if knyga2['kaina'] * 2 > knyga1['kaina']:
        print(f'Padvigubinus {knyga2['pavadinimas']} kaina, ji yra didesne uz {knyga1['pavadinimas']} ')
    else:
        print(f'Padvigubinus {knyga2['pavadinimas']} kaina, ji yra mazesne uz {knyga1['pavadinimas']} ')
elif knyga1['kaina'] < knyga2['kaina']:
    if knyga1['kaina'] * 2 > knyga2['kaina']:
        print(f'Padvigubinus {knyga1['pavadinimas']} kaina, ji yra didesne uz {knyga2['pavadinimas']} ')
    else:
        print(f'Padvigubinus {knyga1['pavadinimas']} kaina, ji yra mazesne uz {knyga2['pavadinimas']} ')
else:
    print('Knygu kainos yra vienodos')

print('==============4==========')
preke1 = {'pavadinimas':'telefonas',
          'kaina':800,
          'savikaina':360,
          'kodas':4598312,
          'turimas kiekis sandelyje':23,
          'matmenys':{'x':12,
                      'y':15,
                      'z':24}}
preke2 = {'pavadinimas':'televizorius',
          'kaina':500,
          'savikaina':540,
          'kodas':65747884,
          'turimas kiekis sandelyje':13,
          'matmenys':{'x':100,
                      'y':54,
                      'z':76}}
preke3 = {'pavadinimas':'kompiuteris',
          'kaina':1500,
          'savikaina':890,
          'kodas':658424587,
          'turimas kiekis sandelyje':26,
          'matmenys':{'x':56,
                      'y':23,
                      'z':45}}
turis1 = preke1['matmenys']['x'] * preke1['matmenys']['y'] * preke1['matmenys']['z']
turis2 = preke2['matmenys']['x'] * preke2['matmenys']['y'] * preke2['matmenys']['z']
turis3 = preke3['matmenys']['x'] * preke3['matmenys']['y'] * preke3['matmenys']['z']
print('Pirmos prekes dezes turis: ', turis1)
print('Antros prekes dezes turis: ', turis2)
print('Trecios prekes dezes turis: ', turis3)
print(preke1)
print(preke2)
print(preke3)
print(f'pirma preke kainuoja - {preke1['kaina']}, antra preke kainuoja - {preke2['kaina']}, trecia preke kainuoja - {preke3['kaina']}')
if preke1['kaina'] > preke2['kaina'] and preke1['kaina'] > preke3['kaina']:
    print(f'Preke {preke1['pavadinimas']} yra brangiausia ir kainuoja {preke1['kaina']}')
elif preke2['kaina'] > preke1['kaina'] and preke2['kaina'] > preke3['kaina']:
    print(f'Preke {preke2['pavadinimas']} yra brangiausia ir kainuoja {preke2['kaina']}')
elif preke3['kaina'] > preke1['kaina'] and preke3['kaina'] > preke2['kaina']:
    print(f'Preke {preke3['pavadinimas']} yra brangiausia ir kainuoja {preke3['kaina']}')
elif preke1['kaina'] == preke2['kaina'] and preke1['kaina'] > preke3['kaina']:
    print(f'Prekes {preke1['pavadinimas']} ir {preke2['pavadinimas']} kainuoja vienodai po {preke1['kaina']} ir yra brangiausios sarase')
elif preke1['kaina'] == preke3['kaina'] and preke1['kaina'] > preke2['kaina']:
    print(f'Prekes {preke1['pavadinimas']} ir {preke3['pavadinimas']} kainuoja vienodai po {preke1['kaina']} ir yra brangiausios sarase')
elif preke2['kaina'] == preke3['kaina'] and preke2['kaina'] > preke1['kaina']:
    print(f'Prekes {preke2['pavadinimas']} ir {preke3['pavadinimas']} kainuoja vienodai po {preke2['kaina']} ir yra brangiausios sarase')
elif preke3['kaina'] == preke1['kaina'] and preke3['kaina'] == preke2['kaina']:
    print('Visos prekes kainuoja vienodai')


prekes = [preke1, preke2, preke3]


import datetime
print('==============5==========')
automobilis = {}
print(automobilis)
automobilis['marke'] = 'Toyota'
automobilis['modelis'] = 'C-HR'
automobilis['rida'] = 20000
automobilis['gamybos metai'] = 2020
automobilis['spalva'] = 'Juoda'
automobilis['darbinis turis'] = 1.6
automobilis['dauzta'] = False
automobilis['parduodama'] = False
print(automobilis)
siandien = datetime.date.today()
automobilio_amzius = siandien.year - automobilis['gamybos metai']
print('Automobiliui yra metu: ', automobilio_amzius)
print('Automobilis vid per metus nuvaziuoja (km): ', automobilis['rida']/automobilio_amzius)



print('==============8==========')
studentas1 = {'vardas':'Lukas',
             'pavarde':'Lukaitis',
             'amzius':23,
             'studiju programa':'biologija',
             'pazymiai':[10,8,9,9,10,6,9,10,7,8],
             'mokyklos pavadinimas':'VU'}

studentas2 = {'vardas':'Saule',
             'pavarde':'Saulyte',
             'amzius':28,
             'studiju programa':'biofizika',
             'pazymiai':[9,8,6,10,7,9,10,8,6,10],
             'mokyklos pavadinimas':'VU'}

vidurkis_stud1 = sum(studentas1['pazymiai']) / len(studentas1['pazymiai'])
vidurkis_stud2 = sum(studentas2['pazymiai']) / len(studentas2['pazymiai'])

studentas1['pazymiu vidurkis'] = vidurkis_stud1
studentas2['pazymiu vidurkis'] = vidurkis_stud2

print(studentas1)
print(studentas2)
if studentas1['pazymiu vidurkis'] > studentas2['pazymiu vidurkis']:
    print(f'Studento {studentas1['vardas']} {studentas1['pavarde']} vidurkis yra didesnis: {studentas1['pazymiu vidurkis']}')
elif studentas1['pazymiu vidurkis'] < studentas2['pazymiu vidurkis']:
    print(f'Studento {studentas2['vardas']} {studentas2['pavarde']} vidurkis yra didesnis: {studentas2['pazymiu vidurkis']}')
else:
    print('Studentu vidurkiai yra vienodi')



# studentas = dict(
# vardas = 'Tomas',
# pavarde = 'Tomauskas',
# amzius = 23,
# ugis = 1.7,
# pazymiai = [7, 7, 2, 3, 9, 8, 10, 9],
# grupe = 'IFM-3/4'
# )
# for raktas in studentas:
#     if raktas == 'vardas' or raktas == 'pazymiai':
#         print(raktas, studentas[raktas])
#
# while True:
#     raktas = input('Iveskite savybe kurios reiksme norite gauti: ')
#     if studentas.get(raktas) != None:
#         print(raktas, studentas.get(raktas))
#     else:
#         print('Ivedete neteisinga savybe!')
#     stop = input('Jei norite stabdyti rasykite s')
#     if stop == 's':
#         break


# darbuotojas = {
# 'vardas': 'Petras',
# 'pavarde': 'Petrauskas',
# 'amzius': 25
# }
#
# if'telefonas'in darbuotojas:
#     print('telefonas:', darbuotojas['telefonas'])
# else:
#     print('nera nurodytas telefono numeris')
#     numeris = input('Nurodykite telefono numeri: ')
#     darbuotojas['telefonas'] = numeris
# print(darbuotojas)

print('==============10==========')
darbuotojas1 = {
        'vardas': 'Jonas',
        'pavarde': 'Jonaitis',
        'telefonas': '123456789',
        'atlyginimas': 2500
    }
darbuotojas2 = {
        'vardas': 'Petras',
        'pavarde': 'Petraitis',
        'telefonas': '987654321',
        'etatas': 'Dalinis',
        'atlyginimas': 1800,
        'patirtis metais': 8,
        #'isilavinimas': 'magistras'
    }
print('Darbuotojas 1 turi tokias savybes:')
for raktas in darbuotojas1:
    print(raktas)
print('Darbuotojas 2 turi tokias savybes:')
for raktas in darbuotojas2:
    print(raktas)
print()
print('vardas' in darbuotojas2)
print('pavarde' in darbuotojas2)
print('telefonas' in darbuotojas2)
print('profesija' in darbuotojas2)
print('atlyginimas' in darbuotojas2)
print()
print('vardas' in darbuotojas1)
print('pavarde' in darbuotojas1)
print('telefonas' in darbuotojas1)
print('etatas' in darbuotojas1)
print('atlyginimas' in darbuotojas1)


# print('Darbuotojas 1')
# for raktas in darbuotojas2:
#     if raktas not in darbuotojas1:
#         savybe = input('Įveskite trukstama savybę: ')
#         profesija = input('Įveskite norimą savybės vertę: ')
#         darbuotojas1[savybe] = profesija
# print(darbuotojas1)
# print('Darbuotojas 2')
# for raktas in darbuotojas1:
#     if raktas not in darbuotojas2:
#         savybe = input('Įveskite trukstama savybę: ')
#         profesija = input('Įveskite norimą savybės vertę: ')
#         darbuotojas2[savybe] = profesija
# print(darbuotojas2)
#
# if darbuotojas1.keys() != darbuotojas2.keys():
#     print('Darbuotojas 1 ir darbuotojas 2 zodynu savybes nesutampa')
#     ivesti = input('Ar norite sarasa papildyti savybemis? (t/n): ')
#     if ivesti == 't':
#         for raktas in darbuotojas2:
#             if raktas not in darbuotojas1:
#                 verte = input(f'Įveskite norimą {raktas} vertę: ')
#                 darbuotojas1[raktas] = verte
#         print('Galutinis sarasas:')
#         print(darbuotojas1)
#     else:
#         print('Pasirinkote kad nenorite papildyti trukstamu savybiu')
#         print('Galutinis sarasas:')
#         print(darbuotojas1)
# else:
#     print('Darbuotojas 1 ir darbuotojas 2 zodynu savybes sutampa')
#     print('Galutinis sarasas:')
#     print(darbuotojas1)
#     print(darbuotojas2)




# for raktas in darbuotojas1.keys():
#     print(f'Pirmas darbuotojas: {raktas, darbuotojas1[raktas]}')
# print('___________________________________________________________')
# for raktas in darbuotojas2.keys():
#     print(f'Antras darbuotojas: {raktas, darbuotojas2[raktas]}')
# for savybe1 in darbuotojas1:
#     if savybe1 not in darbuotojas2:
#         print(f' Darbuotojas2 neturi {savybe1}.')
#         atsakymas1 = input("Ar norite įvesti trūkstamą savybę?T/N")
#         if atsakymas1 == 'T':
#             darbuotojas2[savybe1] = input('Įveskite trūkstamą savybės vertę:')
#             print(f'Atnaujintos antro darbuotojo savybės: {darbuotojas2}')
#         else:
#             print('Sąrašas nėra atnaujintas')
# print(f'Atnaujintas sąrašas: {darbuotojas2}')

print('==============11==========')
# kepykla1 = {
#     'pavadinimas': 'MonAmi',
#     'darbuotoju_kiekis': 5,
#     'adresas': 'Gatvė 1',
#     'iskepti_kepiniai': [20, 25, 30, 28, 35, 22, 24]
# }
# kepykla2 = {
#     'pavadinimas': 'Birzu duona',
#     'darbuotoju_kiekis': 7,
#     'adresas': 'Gatvė 2',
#     'iskepti_kepiniai': [15, 18, 20, 23, 17, 19, 21]
# }
# kepykla3 = {
#     'pavadinimas': 'Kepykla C',
#     'darbuotoju_kiekis': 4,
#     'adresas': 'Gatvė 3',
#     'iskepti_kepiniai': [30, 32, 28, 35, 29, 31, 33]
# }
# kepykla3.clear()
# print(kepykla3)
# kopija = kepykla1.copy()
# print(kepykla1)
# print(kopija)
# print(kepykla2.fromkeys(['gatve']))
# kepykla3.update(kepykla2)
# print(kepykla3)
# kepykla3.popitem()
# kepykla3.popitem()
# print(kepykla3)
# kepykla3.pop('pavadinimas')
# print(kepykla3)
# print(kepykla2)
# kepykla_rikiuota = dict(sorted(kepykla2.items()))
# print(kepykla_rikiuota)
#
#
# skaiciai = {'a':1,
#             'fd':56,
#             'asd':4,
#             'h':9}
# print(skaiciai)
# surikiuota = dict(sorted(skaiciai.items(), key=lambda item:item[1],reverse=True))
# print(surikiuota)
#
# print('==============14==========')
# import datetime
# automobiliai = [
#     {'pavadinimas': 'Audi', 'metai': 2018},
#     {'pavadinimas': 'BMW', 'metai': 2017},
#     {'pavadinimas': 'Mercedes', 'metai': 2019},
#     {'pavadinimas': 'Toyota', 'metai': 2016}
# ]
# siandien = datetime.date.today()
# for masina in automobiliai:
#     masina['masinos amzius'] = siandien.year - masina['metai']
#     print(f'Automobilis, kurio marke yra {masina['pavadinimas']} buvo pagamintas {masina['metai']} m. ir siuo metu siam automobiliui yra {masina['masinos amzius']} m.')

print('==============15==========')
imones = [
    {
        'pavadinimas': 'Vinted',
        'ikurimo metai': 2015,
        'darbuotojai': 1600,
        'pelnas': 3000000
    },
    {
        'pavadinimas': 'Telia',
        'ikurimo metai': 2009,
        'darbuotojai': 900,
        'pelnas': 150000
    },
    {
        'pavadinimas': 'Thermo Fisher Scientific',
        'ikurimo metai': 2001,
        'darbuotojai': 1300,
        'pelnas': 7000000
    }
]
siandien = datetime.date.today()
for imone in imones:
    imone['gyvavimo trukme'] = siandien.year - imone['ikurimo metai']

    print(f'Imone {imone['pavadinimas']} gyvuoja {imone['gyvavimo trukme']} m.')

suma = 0
for imone in imones:
    suma+= imone['gyvavimo trukme']

vidurkis_gyvavimo = round(suma / len(imones),1)
print('Bendras imoniu gyvavimo vidurkis: ', vidurkis_gyvavimo)

darbuotojai = 0
for imone in imones:
    darbuotojai += imone['darbuotojai']

vidurkis_darbuotojai = round(darbuotojai / len(imones))
print('Bendras darbuotoju vidurkis: ', vidurkis_darbuotojai)

bendras_pelnas = 0
for imone in imones:
    bendras_pelnas += imone['pelnas']

print('Bendras visu imoniu pelnas yra: ', bendras_pelnas)

print('==============16==========')
ligonines = [
    {
        'pavadinimas': 'Vilniaus universitetinė ligoninė',
        'adresas': 'Saulėtekio al. 2, Vilnius',
        'lankytojai_per_metus': 50000,
        'darbuotoju_skaicius': 1500
    },
    {
        'pavadinimas': 'Kauno klinikinė ligoninė',
        'adresas': 'Eivenių g. 2, Kaunas',
        'lankytojai_per_metus': 40000,
        'darbuotoju_skaicius': 1200
    },
    {
        'pavadinimas': 'Klaipėdos ligoninė',
        'adresas': 'Liepų g. 15, Klaipėda',
        'lankytojai_per_metus': 30000,
        'darbuotoju_skaicius': 1000
    }
]

for ligon in ligonines:
    print(f'{ligon['pavadinimas']}\nAdresas: {ligon['adresas']}')

darbuotojai = 0
for ligon in ligonines:
    darbuotojai += ligon['darbuotoju_skaicius']

print(f'Bendras darbuotoju kiekis yra: ', darbuotojai)
vidutinis_darb_sk = round(darbuotojai / len(ligonines))
print('Vidutinis darbuotoju skaicius: ', vidutinis_darb_sk)

lankytojai = 0
for ligon in ligonines:
    lankytojai += ligon['lankytojai_per_metus']

print('Bendras lankytoju skaicius:', lankytojai)
vidutinis_lankytoju_sk = round(lankytojai / len(ligonines))
print('Vidutinis lankytoju skaicius: ', vidutinis_lankytoju_sk)


print('==============17==========')
studentu_sarasas = [
    {
        "vardas": "Jonas",
        "pavarde": "Jonaitis",
        "amzius": 20,
        "pazymiai": [8, 9, 7, 10],
        "studiju_programa": "Informatika",
        "kursas": 2
    },
    {
        "vardas": "Petras",
        "pavarde": "Petraitis",
        "amzius": 21,
        "pazymiai": [7, 6, 8, 9],
        "studiju_programa": "Ekonomika",
        "kursas": 3
    },
    {
        "vardas": "Ona",
        "pavarde": "Onaite",
        "amzius": 19,
        "pazymiai": [9, 9, 10, 10],
        "studiju_programa": "Biologija",
        "kursas": 1
    }
]


for studentas in studentu_sarasas:
    suma = sum(studentas['pazymiai'])
    studentas['vidurkis'] = suma / len(studentas['pazymiai'])
    print(f'Studentas: {studentas['vardas']} {studentas['pavarde']}, amzius: {studentas['amzius']}, studiju programas: {studentas['studiju_programa']}, kursas: {studentas['kursas']}')
    print(f'Pazymiai: {studentas['pazymiai']}')
    print(f'Pazymiu vidurkis: {studentas['vidurkis']}')
print('-------------------------')

bendra_suma = sum(studentas['vidurkis'] for studentas in studentu_sarasas)
bendras_vidurkis = bendra_suma / len(studentu_sarasas)
print('Bendras visų studentų pažymių vidurkis: ', bendras_vidurkis)

print('==============18==========')
parduotuve = {
    "pavadinimas": "Topo centras",
    "adresas": "Ukmerges 234, Vilnius",
    "darbuotoju_kiekis": 59,
    "prekiu_sarasas": [
        {
            "pavadinimas": "Kompiuteris",
            "kodas": "KP123",
            "kaina": 999.99,
            "savikaina": 700.0,
            "turimas_kiekis": 20
        },
        {
            "pavadinimas": "Televizorius",
            "kodas": "TV456",
            "kaina": 699.99,
            "savikaina": 500.0,
            "turimas_kiekis": 15
        },
        {
            "pavadinimas": "Telefonas",
            "kodas": "TF789",
            "kaina": 399.99,
            "savikaina": 250.0,
            "turimas_kiekis": 30
        }
    ]
}
print("Parduotuvės informacija:")
print("Pavadinimas:", parduotuve["pavadinimas"])
print("Adresas:", parduotuve["adresas"])
print("Darbuotojų kiekis:", parduotuve["darbuotoju_kiekis"])

