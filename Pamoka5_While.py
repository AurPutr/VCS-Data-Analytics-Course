# from random import randint
#
# while True: # jei turime true ciklas turi tureti BREAK
#     skaicius = randint(1,100)
#     if skaicius % 7 == 0 and skaicius % 2 == 0:
#         print(f'Skaicius {skaicius} dalinasi is 7 ir is 2')
#         break
#     else:
#         print(skaicius)
#
# print('==============================')
# skaicius = 7
#
# while skaicius % 7 != 0 or skaicius % 2 != 0:
#     skaicius=randint(1,100)
#
#     if skaicius % 7 == 0 and skaicius % 2 == 0:
#         print(f'Skaicius {skaicius} dalinasi is 7 ir is 2')
#     else:
#         print(skaicius)

# skaicius = 0
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1
#
# skaicius = 1
# while skaicius <= 50:
#     if skaicius %2 == 0:
#         print(skaicius, 'lyginis')
#     else:
#         print(skaicius)
#     skaicius += 1


# pradzia = 25
# pabaiga = 50
# skaicius = 25
# while skaicius >= pradzia and skaicius <= pabaiga:
#     if skaicius %3 == 0:
#         print('Skaicius dalijasi is 3')
#     else:
#         print(skaicius)
#     skaicius += 1


# pabaiga = 100
# skaicius = 1
# while skaicius <= pabaiga:
#     if skaicius % 7 == 0:
#         print(skaicius)
#     skaicius += 1


# skaicius = 1
# while True:
#     if skaicius % 3 == 0 and skaicius % 5 == 0:
#         print(f'Skaicius {skaicius} dalinasi is 3 ir is 5')
#         break
#     else:
#         print(skaicius)
#     skaicius += 1
#
#
# pradzia = int(input('Iveskite reziu pradzia: '))
# pabaiga = int(input('Iveskite reziu pabaiga: '))
# while pradzia > pabaiga:
#     print('Reziai ivesti neteisingai, kartokite dar karta: ')
#     pradzia = int(input('Iveskite reziu pradzia: '))
#     pabaiga = int(input('Iveskite reziu pabaiga: '))
# print('Aciu, ivedete teisingai!')
# for skaicius in range(pradzia, pabaiga):
#     if skaicius %2 == 0:
#         print(skaicius, '===', skaicius**2, '===', 'lyginis')
#     elif skaicius %2 != 0:
#         print(skaicius, '===', skaicius ** 2, '===', 'nelyginis')

# kartoti = 't'
# while kartoti == 't':
#     print('Iveskite du norimus skaicius (atskiriame enter): ')
#     pirmas = int(input())
#     antras = int(input())
#     print(f'{pirmas} + {antras} = {pirmas + antras}')
#     kartoti = input('Ar norite kartoti? (t/n): ')
# print('Pabaiga')
#
# pr = int(input('Iveskite intervalo pradzia: '))
# pb = int(input('Iveskite intervalo pabaiga: '))
#
# while pr > pb:
#     print('Kartokite intervalo pr pb ivedima')
#     pr = int(input('Iveskite intervalo pradzia: '))
#     pb = int(input('Iveskite intervalo pabaiga: '))
#
# print('Aciu ivedete teisingai')


# skaicius = -5
# while skaicius < 10:
#     print(skaicius)
#     skaicius += 1
#
# zodis = 'mano vardas Aurelija'
# kartai = 5
# while kartai > 0:
#     print(zodis)
#     kartai -= 1
#
# prekiu_sk = 24
# while prekiu_sk > 0:
#     print(f'turimas prekiu kiekis {prekiu_sk}')
#     pirkimo_kiekis = int(input('Kiek prekiu norite nusipirkti? '))
#     if pirkimo_kiekis > prekiu_sk:
#         pirkimo_kiekis = prekiu_sk
#     print(f'nupirkote {pirkimo_kiekis}\n')
#     prekiu_sk -= pirkimo_kiekis




# skaicius = 1
# while skaicius %7 != 0 or skaicius %3 != 0:
#     skaicius = randint(1, 100)
#     print(skaicius)

# while True:
#     skaicius = randint(1,100)
#     print(skaicius)
#     if skaicius %7 == 0 and skaicius %2 == 0:
#         print(f'skaicius {skaicius} dalinasi ir is 7 ir is 3')
#         break

# pradzia, pabaiga = 1, 100
# skaicius = 0
# while skaicius < pradzia or skaicius >= pabaiga:
#     skaicius = int(input('Iveskite skaiciu reziuose [1-100]: '))
#     if skaicius < pradzia or skaicius > pabaiga:
#         print('Blogai ivestas rezis')
# print('Pabaiga')
# print('Ivestas skaicius:', skaicius)

from random import randint
# lyginius_suma = 0
# lyginius_kiekis = 0
# while lyginius_kiekis < 5:
#     skaicius = randint(1, 10)
#     if skaicius %2 == 0:
#         print(skaicius, 'lyginis')
#         lyginius_kiekis += 1
#         lyginius_suma += skaicius
#     else:
#         print(skaicius)
# print('rasta lyginiu suma: ', lyginius_suma)

# slaptas = randint(1, 10)
# spejimas = None
# while slaptas != spejimas:
#     spejimas = int(input('Spekite skaiciu tarp 1 ir 10: '))
#
# slaptas = randint(1, 10)
# spejimas = None
# while slaptas != spejimas:
#     spejimas = int(input('Spekite skaiciu tarp 1 ir 10: '))
#     if slaptas != spejimas:
#         print('Deja natspejote, bandykite dar karta!')
#     else:
#         print('Atspejote!')

# pazymiu_suma = 0
# pazymiu_kiekis = 0
# kartoti = 't'
# while kartoti == 't':
#     pazymys = int(input('Iveskite pazymi: '))
#     pazymiu_suma += pazymys
#     pazymiu_kiekis += 1
#     kartoti = input('Ar dar norite ivest? (t/n): ')
# vidurkis = round(pazymiu_suma / pazymiu_kiekis, 1)
# print('Suvestu pazymiu vidurkis yra: ', vidurkis)
print('====================1===================')
# skaicius = 1
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1
print('===================2====================')
# while skaicius <= 50:
#     if skaicius %2 == 0:
#         print(skaicius, 'lyginis')
#     elif skaicius %2 != 0:
#         print(skaicius, 'nelyginis')
#     skaicius += 1
print('==================3=====================')

# skaicius = 25
# while skaicius <= 50:
#     if skaicius %3 == 0:
#         print(skaicius, 'dalinasi is 3')
#     else:
#         print(skaicius)
#     skaicius += 1
print('==================4=====================')
# skaicius = 1
# while skaicius <= 100:
#     print(skaicius)
#     if skaicius %7 == 0:
#         print(skaicius)
#         break
#     skaicius += 1
print('==================5=====================')
# skaicius = 1
# while True:
#     if skaicius %5 == 0 and skaicius %3 == 0:
#         print(skaicius, 'dalinasi ir is 3 ir 5')
#         break
#     else:
#         print(skaicius)
#     skaicius += 1
print('==================6=====================')
# pradzia = int(input('Iveskite reziu pradzia: '))
# pabaiga = int(input('Iveskite reziu pabaiga: '))
# while pradzia > pabaiga:
#     print('Jusu reziai ivesti neteisingai.\nPrasau iveskite dar karta.')
#     pradzia = int(input('Iveskite reziu pradzia: '))
#     pabaiga = int(input('Iveskite reziu pabaiga: '))
# print('Aciu ivedete teisingai')
# for skaicius in range(pradzia, pabaiga):
#     if skaicius %2 == 0:
#         print(skaicius, '===', skaicius**2, '===','lyginis')
#     else:
#         print(skaicius, '===', skaicius**2, '===','nelyginis')
print('==================7=====================')
# skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
# skaiciu_suma = 0
# while skaicius != 0:
#     skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
#     skaiciu_suma += skaicius
# print('Suvestu skaiciu suma: ', skaiciu_suma)
print('==================9=====================')
# skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
# skaicius1 = int(input('Iveskite norima sveikaji skaiciu: '))
# skaiciu_suma = 0
# skaicius_atimtis = 0
# skaiciu_daugyba = 0
# skaiciu_dalyba = 0
# kartoti = 'taip'
# while kartoti == 'taip':
#     skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
#     skaicius1 = int(input('Iveskite norima sveikaji skaiciu: '))
#     skaiciu_suma += (skaicius + skaicius1)
#     skaicius_atimtis += (skaicius - skaicius1)
#     skaiciu_daugyba += (skaicius * skaicius1)
#     skaiciu_dalyba += (skaicius / skaicius1)
#     print('Skaiciu suma: ', skaiciu_suma)
#     print('Skaiciu atimtis: ', skaicius_atimtis)
#     print('Skaiciu daugyba: ', skaiciu_daugyba)
#     print('Skaiciu dalyba: ', skaiciu_dalyba)
#     kartoti = input('Ar norite kartoti? (taip/ne): ')
# print('Pabaiga')
print('==================10=====================')
# kartoti = 'taip'
#
# while kartoti == 'taip':
#     daugiklis = 1
#     skaicius = int(input('Iveskite norima skaiciu: '))
#     while daugiklis <= 10:
#         print(f'skaicius {skaicius} * {daugiklis} = {skaicius * daugiklis}')
#         daugiklis += 1
#     kartoti = input('Ar norite kartoti skaiciavimus? (taip/ne): ')
# print('Pabaiga')

print('==================11=====================')
# skaiciu_suma = 0
# skaiciu_kiekis = 0
#
# while True:
#     skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
#     if skaicius == 6:
#         print('Atspejote')
#         break
#     else:
#         skaiciu_kiekis += 1
#         skaiciu_suma += skaicius
#         print('Skaiciaus neatspejote, bandykite dar karta')
#
# vidurkis = round(skaiciu_suma/skaiciu_kiekis, 2)
# print('Ivestu skaiciu vidurkis: ', vidurkis)


print('==================12=====================')
# kartoti = 'taip'
#
# while kartoti == 'taip':
#     pazymiu_suma = 0
#     pazymiu_kiekis = 0
#     pazymys = -1
#     print('Iveskite tiek pazymiu kiek norite (atskiriant enter)')
#     print('Norint baigti irasykite 0')
#     studentas = int(input('Iveskite studento LSP numeri: '))
#     while pazymys != 0:
#         pazymys = int(input('Iveskite pazymi: '))
#         if pazymys != 0:
#             pazymiu_suma += pazymys
#             pazymiu_kiekis += 1
#     vidurkis = round(pazymiu_suma / pazymiu_kiekis, 1)
#     print('Suvestu pazymiu vidurkis:', vidurkis)
#     kartoti = input('Ar norite skaiciuoti kito studento vidurki? (taip/ne): ')

print('==================13=====================')
from random import randint
print('pasirinkite zaidimo parametrus:')
print('1. Sudetingumas: ')
print('Lengvas: skaicius reziuose [1,50]')
print('Vidutinis: skaicius reziuose [1,100]')
print('Sunkus: skaicius reziuose [1,150]')
print('2. Pagalbos galimybes: ')
print('Taip / Ne')
while True:
    sudetingumas = input('Iveskite pasirinkta sudetingumo lygi (lengvas/vidutinis/sunkus): ')
    if sudetingumas in ['lengvas', 'vidutinis', 'sunkus']:
        break
    else:
        print('Neteisingas pasirinkimas. Prasome pasirinkti tik is galimu variantu.')

while True:
    pagalba = input('Iveskite ar norite gauti pagalbos? (taip/ne): ')
    if pagalba in ['taip', 'ne']:
        break
    else:
        print('Neteisingas pasirinkimas. Prasome pasirinkti tik is galimu variantu.')

print('Pradekime zaidima!')
spejimai = 0

if sudetingumas == 'lengvas':
    skaicius = randint(1,50)
elif sudetingumas == 'vidutinis':
    skaicius = randint(1,100)
elif sudetingumas == 'sunkus':
    skaicius = randint(1,150)

while True:
    spejimas = int(input('Atspekite skaiciu: '))
    spejimai += 1
    if spejimas == skaicius:
        print(f'Teisingai! skaicius buvo {spejimas}. Jums prireike {spejimai} spejimu.')
        break
    else:
        print('Neteisingai, bandykite dar karta.')
        if pagalba == 'taip':
            if skaicius < spejimas:
                print('Jusu pasirinktas skaicius yra didesnis')
            elif skaicius > spejimas:
                print('Jusu pasirinktas skaicius yra mazesnis')
