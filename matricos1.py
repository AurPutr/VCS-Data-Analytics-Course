# # Masyvas ir matrica duomenų saugykla
# # Python nėra standartinio įrankio masyvams/matricoms kurt
# # Masyvas/matrica Python‘e interpretuojamas kaip skaičių sąrašas
# # Masyvui/matricai kurti, reikia importuoti Numpy biblioteką
# # Masyvas/matrica skiriasi nuo kitų duomenų saugyklų
# # Griežta struktūra (Skaičiavimai Numpy pagalba yra greitesni, nei naudojant paprastus sąrašus)
import datetime
import random
#
# # Masyvo/matricos kūrimo etapai
# # Importuoti Numpy biblioteką
# # Sukurti matricą Numpy įrankio pagalba
import numpy #Pycharm ar kitos programavimo aplinkos Terminale pirmiausia isirasome numpy - pip install numpy
import numpy as np
#
# # import numpy as np # jei norime galime sutrumpinti bibliotekos pavadinima as np budu.
# A = numpy.array([1,2,3,4,5]) # vienmatis masyvas
# print(A)
# print(type(A))
#
# # Numpy masyvuose gali buti patalpinta ivairus kintamuju tipai - taciau jie turi vienodo tipo. Jei pamaisysime pamatysite kad jie yra suvienodinami pagal sudetingesni tipa.
# B1 = numpy.array([1,2,3,4,5]) # vienmatis masyvas
# print(B1)
# B2 = numpy.array([1,2.2,3,4,5])
# print(B2)
# B2 = numpy.array([1,True,3,4,5])
# print(B2)
# B3 = numpy.array([1,True,'Labas',3,4,5])
# print(B3)
# # B4 = numpy.array([[1,2,3],'labas',2,3]) #Sarasu prie vienalypiu duomenu negalima jungti i np masyva
# # print(B4)
# # B5 = numpy.array([[1,2,3],[1,3]]) #Sarasus jungiant i np masyva - jau matrica - listuose negali buti skirtingas elementu kiekis
# # print(B5)
# B6 = numpy.array([{1,2,3},{1,3,2}])
# print(B6)
# B7 = numpy.array([datetime.datetime.now(), datetime.datetime.today().date(), datetime.datetime.today().time()])
# print(B7)
# #
# # # Masyvo /matricos kurimo būdų yra labai daug priklauso nuo duomenų, kuriuos turite Lentelėje pateikti pagrindiniai
# # # būdai Kurie detaliau nagrinėjami pavyzdžiai:
# print('################Masyvo kurimas########################')
# mas=np.array([1,2,3,4,5])
# #
# mas1 = np.array(range(12))
# print(mas1)
# mas2 = np.array(range(-5,5, 2))
# print(mas2)
# mas3 = np.array([-1,-9,0,45,2], dtype=float) #dtype dalis nurodo kokio tipo duomenys bus
# print(mas3)
# mas4 = np.random.randint(low=-7, high=7,size = 5) # tik teigiami nuo 0, tada paliekam tik low
# print(mas4)
# mas5 = np.random.uniform(low=-6, high=6,size = 5) # be zingsnio nuo 0
# print(mas5)
# # # kai norime gauti intervala nuo iki
# mas6 = np.array([np.random.randint(-5,5) for sk in range(7)])
# #np.array vercia i tipa (pvz tuple/list/set)
# print(mas6)
# mas7 = np.array([round(random.random(),2) for sk in range(7)])
# print(mas7)
# mas8 = np.array([round(random.randrange(-5,5),2) for sk in range(7)])
# print(mas8)
# mas9 = np.array([round(np.random.uniform(-5,5),2) for sk in range(7)])
# print(mas9)
# mas10= numpy.random.random_sample(5)
# print(numpy.round(mas10,2))
#
# # Matricos kūrimo būdai
# # Masyvas yra vienmatė matrica Todėl sudarant nevienmatę matricą,
# # naudojami visi būdai kaip ir masyvui.
# # Verta įsiminti:
# # 1. Matricoje elementų skaičius kiekvienoje eilutėje/stulpelyje turi būti vienodas.
# # 2. Jei visi elementai yra sveikieji, matrica interpretuojama kaip sveikųjų skaičių
# # matrica.
# # 3. Jei tarp sveikųjų skaičių bus bent vienas realus skaičius, visa matrica
# # interpretuojama kaip realiųjų skaičių matrica.
# # 4. Jei tarp skaičių bus bent vienas simbolinis kintamasis, visa matrica
# # interpretuojama kaip simbolinių kintamųjų(kitaip dar vadinama string tipo)
# # matrica.
#
import numpy as np
matr=np.array([[7,2,9],[9,7,0]])
print('Matrica:')
print(matr)
print(type(matr))
#
C = np.random.randint( low=-10, high=10, size = (3,4))
print(C)
C1=np.random.randint(low=-7, high=3 , size = (2,5))
print(C1)
#
# # Sveikųjų atsitiktinių skaičių matricos sudarymas
# # Pavyzdys
# # Sudaryti A(4,3) matricą iš teigiamų sveikųjų skaičių, kur didžiausia reikšmė 10.
# # B(2,5) matrica iš sveikųjų skaičių, kur reikšmių diapazonas (-7,3).
# # Išvesti rezultatus į ekraną
#
A = np.random.randint(10, size = (4,3))
print('Matrica A')
print(A)
B = np.random.randint(low=-7,high=3, size =(2, 5))
print('Matrica B')
print(B)
#
# # Realiųjų atsitiktinių skaičių matricos sudarymas
# # Pavyzdys
# # Sudaryti A(3,4) matricą iš realiųjų skaičių, kurių reikšmių diapazonas yra
# # nuo -22 iki 4. Panaudojant standartines didžiausios max ir mažiausios min
# # reikšmių radimo funkcijas, atspausdinti sugeneruotos matricos ekstremumų
# # reikšmes ir pačią matricą.
#
A=np.round(np.random.uniform(low=-22, high=3 , size=(3,4)),2)
print('matrica A')
print(A)
print('Didiziausia matricos A reiksme:', A.max())
print('Maziausia matricos A reiksme:', A.min())
#
# # Matricos sudarymas iš masyvo
# # Turint masyvą, tam tikrais atvejais jį galima performuoti į matric. Pagrindinė ir
# # vienintelė sąlyga, kad formuojamos matricos eilučių ir stulpelių sandauga būtų lygi
# # masyvo elementų skaičiui.
# # mas=np.random.random(N)
# # matr=mas.reshape(n,m)
# # Būtina sąlyga n*m = N
# # Jei neatitinka šios sąlygos, suformuoti matricos negalima, programa rodys klaidą.
# # Lygiai tokiu pat būdu galima performuoti ir matricą, nepažeidžiant būtinosios sąlygos.
#
# # Pavyzdžiui A(20) masyvą performuokime į B(4,5) matricą
#
A=np.random.randint(15,size=20)
print('Masyvas A:')
print(A)
B=A.reshape(4,5)
print('Matrica B')
print(B)

#####################################U Z D U O T Y S########################################
# 1 uzduotis:
# Sudaryti masyvą iš 10 elementų, atsitiktiniu būdu sugeneruojant
# sveikuosius teigiamus skaičius iki 50.Spausdinti masyvą, jo didžiausią ir
# mažiausią reikšmę.
print('===============1==============')
A = np.random.randint(low=0, high=50, size=10)
print('Masyvas A')
print(A)
print('Didziausia reiksme: ', A.max())
print('Maziausia reiksme: ', A.min())

# Rezultatas:
# A masyvas : [27 15 24 18 34 27 25 14 17 12]
# Didiausia reikšmė : 34
# Mažiausia reikšmė : 12
###########################################################################################
# 2 uzduotis:
# Sudaryti masyvą iš atsitiktinių sveikųjų skaičių, jo elementų skaičių ir reikšmių
# diapazoną parenkant input būdu.Ekrane atspausdinti masyvą, didžiausią ir
# mažiausią jo reikšmę.

print('===============2==============')
# elementu_sk = int(input('Iveskite skaiciu, kiek norite, kad elementu sudarytu masyva?: '))
# didziausia_reiksme = int(input('Iveskite galima didziausia masyvo reiksme: '))
# maziausia_reiksme = int(input('Iveskite galima maziausia masyvo reiksme: '))
# A = np.random.randint(low=maziausia_reiksme, high=didziausia_reiksme, size=elementu_sk)
# print('Kiek masyve elementu: ', elementu_sk)
# print('Masyvas A')
# print(A)
# print('Didziausia masyvo reiksme: ', A.max())
# print('Maziausia masyvo reiksme: ', A.min())


# Rezultatas:
# Kiek masyve elementų ? 7
# Įveskite mažiausia galima masyvo reišmė ? -33
# Įveskite didžiausia galima masyvo reišmė ? 21
# A masyvas : [ 5 -33 -26 -31 18 14 -17]
# Didiausia reikšmė : 18
# Mažiausia reikšmė : -33
###########################################################################################
# 3 uzduotis:
# Sudaryti masyvą iš atsitiktinių sveikųjų skaičių, jo elementų skaičių
# sugeneruojant random būdu (didžiausia leistina reikšmė 10). Ekrane išvesti masyvą ir jo dydį
# Jei sąlygoje nenurodyta, trūkstamas reikšmes nusirodome patys patys.
# Masyvui sugeneruoti, reikia nurodyti reikšmių diapazoną savo nužiūra. Rezultate nurodyta 10.

print('===============3==============')
# elementu_sk = int(input('Iveskite skaiciu, kiek norite, kad elementu sudarytu masyva?: '))
# A = np.random.randint(10, size=elementu_sk)
# print('Kiek masyve elementu: ', elementu_sk)
# print('A masyvas: ', A)

# Rezultatas:
# A masyvas : [5 3 2 4 9 8]
# Masyvo elementų skaičius : 6

###########################################################################################
# 4 uzduotis:
# Sudaryti masyvą iš atsitiktinių sveikųjų skaičių, jo elementų skaičių sugeneruojant
# random būdu iš diapazono(-5,10).Jei sugeneruojamas neigiamas
# masyvo elementų skaičius, programa nutraukiama, spausdinamas pranešimas.
# Jei sugeneruojamas masyvas, jis atspausdinamas ekrane.Taip pat spausdinamas masyvo dydis.

print('===============4==============')
# masyvo_dydis = int(input('Iveskite skaiciu masyvo dydziui nusakyti: '))
# if masyvo_dydis > 0:
#     A = np.random.randint(low=-5, high=10, size=masyvo_dydis)
#     print('Masyvas A')
#     print(A)
#     print('Masyvo elementu skaicius: ', masyvo_dydis)
# else:
#     print('Deja, masyvo is tokio skaiciaus sugeneruoti negalima')


# Rezultatas1 :
# Sugeneruotas skaičius : -2
# Masyvo sugeneruoti iš tokio skaičiaus negalima
# Rezultatas2 :
# A masyvas : [5 8 4 8]
# Masyvo elementų skaičius : 4

###########################################################################################
# 5 uzduotis:
# Sudaryti masyvą iš atsitiktinių realiųjų skaičių, jo elementų kiekį nurodant INPUT būdu.
# Performuoti į matricą, kurios eilučių ir stulpelių skaičius nurodomas INPUT būdu.
# 1. Jei matricos suformuoti negalima, spausdinamas pranešimas ir programa nutraukiama.
# 2. Jei matricos suformuoti negalima, užklausa kartojama tol,kol pavyksta. while

print('===============5==============')
# elementu_sk = int(input('Iveskite skaiciu, kiek norite, kad elementu sudarytu masyva?: '))
# A = np.random.randint(30, size=elementu_sk)
# print('Masyvas: ', A)
# eilutes = int(input('Kiek eiluciu norite tureti matricoje?: '))
# stulpeliai = int(input('Kiek stulpeliu norite tureti matricoje?: '))
#
# if eilutes * stulpeliai == elementu_sk:
#     B = A.reshape(eilutes,stulpeliai)
#     print('Matrica:', B)
# else:
#     print('Programa nutraukiama')

# elementu_sk = int(input('Iveskite skaiciu, kiek norite, kad elementu sudarytu masyva?: '))
# A = np.random.randint(30, size=elementu_sk)
# print('Masyvas: ', A)
# while True:
#     eilutes = int(input('Kiek eiluciu norite tureti matricoje?: '))
#     stulpeliai = int(input('Kiek stulpeliu norite tureti matricoje?: '))
#     if eilutes * stulpeliai != elementu_sk:
#         print('Ivedete netinkamus skaicius. Prasome kartoti.')
#     else:
#         B = A.reshape(eilutes, stulpeliai)
#         print('Matrica:', B)
#         break

# Rezultatas 1:
# Kiek elementų sudaro masyvą ? 18
# Masyvas: [ -9 -2 -3 -9 9 2 11 3 11 11 10 14 12 5 3 7 -10 -3]
# Kiek formuojamoje matricoje eilučių ? 9
# Kiek formuojamoje matricoje stulpelių ? 9
# Tokios matricos sudaryti negalima

# Rezultatas 2:
# Kiek elementų sudaro masyvą ? 6
# Masyvas: [-11 13 -3 -2 0 -12]
# Kie formuojamoje matricoje eilučių ? 2
# Kiek formuojamoje matricoje stulpelių ? 3
# Matrica:
# [[-11 13 -3]
# [-2 0 -12]]
