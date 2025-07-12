sk1 = 6
sk2= 16
sk3 = 874
#a
if sk1 == sk2:
   print('skaiciai lygus')
else: print('nelygus')
print()
#b
if sk2 == sk3:
   print('skaiciai lygus')
else: print('nelygus')
print()
#c
if sk1 > sk2:
   print(f'skaicius {sk1} yra didesnis uz {sk2}')
else: print(f'skaicius {sk1} yra mazesnis uz {sk2}')
print()
#d
if sk2 > sk3*2:
   print(f'skaicius {sk2} yra didesnis uz {sk3*2}')
else: print(f'skaicius {sk2} yra mazesnis uz {sk3*2}')
print()
#e
if sk1 % 2 ==0:
   print('skaicius lyginis')
else: print('skaicius nelyginis')
print()
#f
if sk2 % 2 !=0:
   print('skaicius nelyginis')
else: print('skaicius lyginis')
print()
#g
if sk3 > 0:
   print('skaicius teigiamas')
else: print('skaicius neigiamas')
print()
#h
if sk1 < 0:
   print('skaicius neigiamas')
else: print('skaicius teigiamas')
print()
#i
if sk2 %4 == 0:
   print('skaicius dalinasi is 4')
else: print('skaicius nesidalina is 4')
print()
#j
if sk3 %8 == 0:
   print('skaicius dalinasi is 8')
else:
   print('skaicius nesidalina is 8')
print()
#6 tema 2 uzd
print('==========================')
print()
# amzius = int(input('Iveskite savo amziu: '))
# if amzius >= 18:
#    print('jus galite balsuoti')
# else: print('balsuoti dar negalite')
print()
#6 tema 3 uzd
print('==========================')
print()
# skaicius = int(input('Iveskite norima pazymi: '))
# skaicius2 = int(input('Iveskite norima pazymi: '))
# skaicius3 = int(input('Iveskite norima pazymi: '))
# vidurkis = (skaicius+skaicius2+skaicius3)/3
# if vidurkis >= 5:
#    print('Vidurkis teigiamas')
# else: print('Vidurkis neigiamas')
print()
#6 tema 4 uzd
print('==========================')
print()
# skaicius = int(input('Iveskite norima skaiciu: '))
#a
print()
# if skaicius %5 == 0:
#    print(skaicius*1)
#    print(skaicius*2)
#    print(skaicius*3)
#    print(skaicius*4)
#    print(skaicius*5)
# else:print('Skaicius nesidalija is 5')
# #b
# print()
# if skaicius %2 == 0:
#    print(skaicius)
#    print(skaicius**2)
#    print(skaicius%2)
# else: print('Skaicius nelyginis')
# #c
# print()

# if skaicius %7 != 0:
#    kintamasis = int(input('Iveskite norima skaiciu: '))
#    print(skaicius+kintamasis)
#    print(skaicius-kintamasis)
#    print(skaicius*kintamasis)
#    print(skaicius/kintamasis)

# print()
#6 tema 5 uzd
# print('==========================')
# print()
# sk1 = 6
# sk2 = 10
# sk3 = 2
# if sk1 > sk2:
#    print(f'skaicius {sk1} > {sk2}')
# elif sk2 > sk3:
#    print(f'skaicius {sk2} > {sk3}')
# elif sk3 > sk1:
#    print(f'skaicius {sk3} > {sk1}')
# print()
# # 6 tema 6 uzd
# print('==========================')
# print()
# if sk1 == sk2:
#    print(f'{sk1} yra lygus {sk2}')
# elif sk2 == sk3:
#    print(f' {sk2} yra lygus {sk3}')
# elif sk1 == 0:
#    print('skaicius lygus 0')
# elif sk2 < 0:
#    print('skaicius yra neigiamas')
# elif sk3 > 0:
#    print('skaicius yra teigiamas')
# print()
# # 6 tema 7 uzd
# print('==========================')
# print()
# pazymys = int(input('Parasykite savo egzamino pazymi: '))
# if pazymys == 10:
#    print('Puiku')
# elif pazymys >= 9:
#    print('Labai gerai')
# elif pazymys >= 7:
#    print('Gerai')
# elif pazymys >= 5:
#    print('Patenkinamai')
# elif pazymys < 5:
#    print('Egzaminas neislaikytas')
# print()
# 6 tema 7 uzd
# print('==========================')
# print()
# norimas_skaicius = int(input('Iveskite norima skaiciu: '))
# sprendimas = 'skaicius lyginis' if norimas_skaicius %2 == 0 else 'skaicius nelyginis'
# print(sprendimas)
# if norimas_skaicius %2 ==0:
#    print('skaicius lyginis')
# else:
#    print('skaicius nelyginis')
# print()
#8
# print('==========================')
# print()
# norimas_skaicius2 = int(input('Iveskite norima skaiciu: '))
# sprendimas2 = 'skaicius dalijasi is 7' if norimas_skaicius2 %7 == 0 else 'skaicius nesidalija is 7'
# print(sprendimas2)
# # if norimas_skaicius2 %7 ==0:
# #    print('skaicius dalijasi is 7')
# # else:
# #    print('skaicius nesidalija is 7')
# # print()
# #9
# print('==========================')
# print()
# failas = input('Iveskite failo linka: ')
# sprendimas3 = 'prezentacijos skaidres' if failas.endswith('.ppt') else 'kito formato dokumentas'
# print(sprendimas3)
# if failas.endswith('.ppt'):
#    print('prezentacijos skaidres')
# else:
#    print('kito formato dokumentas')
# print()
# # 6 tema 10 uzd
# print('==========================')
# print()
# skaitmuo = int(input('Iveskite norima sveikaji skaiciu: '))
# if skaitmuo %2 == 0:
#    print('skaicius yra lyginis')
# elif skaitmuo %5 == 0:
#    print('skaicius dalijasi is 5')
# elif skaitmuo == 3:
#    print('skaicius yra lygus 3')
# else:
#    print('error')
print()

print('==========================')
print()

# vardas = input('Iveskite savo varda: ')
# print(vardas.upper(), vardas.lower(), vardas.title(), vardas.capitalize())

# 6 tema 11 uzd
# print('==========================')
print()
# skaicius1 = int(input('Iveskite sveikaji skaiciu: '))
# skaicius2 = int(input('Iveskite sveikaji skaiciu: '))
# skaicius3 = int(input('Iveskite sveikaji skaiciu: '))
# if skaicius1 == skaicius2:
#    print(f'Skaiciai {skaicius1} ir {skaicius2} yra lygus')
# elif skaicius1 == skaicius3:
#    print(f'Skaiciai {skaicius1} ir {skaicius3} yra lygus')
# elif skaicius3 > skaicius1:
#    print(f'Skaicius {skaicius3} yra didesnis uz {skaicius1}')
# if skaicius2 == skaicius3 * 2:
#    print(f'Skaicius {skaicius2} yra dvigubai didesnis uz {skaicius3}')
# elif skaicius1 %3 == 0:
#    print('Skaicius dalijasi is 3')
# else:
#    print('error')


# failas = '' # jei yra tarp '' tekstas tai bus TRUE, jei '' tuscias - FALSE
# failas = [] # -turime tuščią objektą - FALSE
# failas = [1] # -turime pilna objektą - TRUE
# failas = None # -nurodyta None reikšmė
# failas = 12 # jei kazkia yra verte, kad ir skaicius - TRUE
# failas = 0 # -yra 0 - FALSE
# failas = 1 # -yra 0 - TRUE
# if failas == True: # if failas:
#     print('failo nuskaitymas...')
# else:
#     print('prasome nurodyti faila')


# if 0 < skaicius <= 100:
#     print('skaicius patenka tarp reziu [1-100]')

# # 6 tema 12 uzd
# print('==========================')
# print()
# skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
# skaicius2 = int(input('Iveskite norima sveikaji skaiciu: '))
# skaicius3 = int(input('Iveskite norima sveikaji skaiciu: '))
# #
# if skaicius > skaicius2 and skaicius > skaicius3:
#    print(f'skaicius {skaicius} yra didziausias')
# elif skaicius2 > skaicius and skaicius2 > skaicius3:
#    print(f'skaicius {skaicius2} yra didziausias')
# elif skaicius3 > skaicius and skaicius3 > skaicius2:
#    print(f'skaicius {skaicius3} yra didziausias')
# elif skaicius2 == skaicius3 and skaicius3 == skaicius:
#    print('Visi skaiciai lygus')
# elif skaicius == skaicius2 or skaicius == skaicius3 or skaicius2 == skaicius3:
#    print('Du skaiciai lygus')
# else:
#    print('error')
# #
# #
# #
# if skaicius < skaicius2 and skaicius < skaicius3:
#    print(f'skaicius {skaicius} yra maziausias')
# elif skaicius2 < skaicius and skaicius2 < skaicius3:
#    print(f'skaicius {skaicius2} yra maziausias')
# elif skaicius3 < skaicius and skaicius3 < skaicius2:
#    print(f'skaicius {skaicius3} yra maziausias')
# elif skaicius2 == skaicius3 and skaicius3 == skaicius:
#    print('Visi skaiciai lygus')
# elif skaicius == skaicius2 or skaicius == skaicius3 or skaicius2 == skaicius3:
#    print('Du skaiciai lygus')
# else:
#    print('error')
#
#  # 6 tema 14 uzd
# print('==========================')
# print()
# pazymys = int(input('Iveskite pirmojo egzamino pazymi: '))
# pazymys2 = int(input('Iveskite antrojo egzamino pazymi: '))
# pazymys3 = int(input('Iveskite treciojo egzamino pazymi: '))
# vidurkis = (pazymys + pazymys2 + pazymys3)/3
# if vidurkis >=8 and vidurkis <= 10:
#    print('vidurkis patenka i rezius 8-10')
# elif vidurkis >= 5 and vidurkis < 8:
#    print('vidurkis parenka i rezius 5-7')
# else:
#    print('vidurkis <5')
 # 6 tema 15 uzd
print('==========================')
print()
skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
skaicius2 = int(input('Iveskite norima sveikaji skaiciu: '))
if skaicius > skaicius2 or skaicius == 0:
   print(f' skaicius {skaicius} didesnis uz {skaicius2} arba lygus 0')
elif skaicius2 > skaicius or skaicius2 == 5:
   print(f' skaicius {skaicius2} didesnis uz {skaicius} arba lygus 5')
elif skaicius > skaicius2 and skaicius == 20:
   print(f' skaicius {skaicius} didesnis uz {skaicius2} ir lygus 20')
elif skaicius2 > skaicius and skaicius2 < 100:
   print(f' skaicius {skaicius2} didesnis uz {skaicius} ir mazesnis uz 100')
else:
   print('error')

print('==========================')
print()
print("+--------+--------+\n| Vardas | Amzius |\n+--------+--------+\n| Tomas  | 24     |\n| Jonas  | 26     |\n| Juste  | 25     |\n+--------+--------+")


