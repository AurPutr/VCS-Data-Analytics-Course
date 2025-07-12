print('=========1=1===========')
# skaicius = int(input('Iveskite sveikaji skaiciu: '))
# sk = 1
# atspausdinta = 0
# while atspausdinta < skaicius:
#     kiek_eiluteje = 1
#     for eilute in range(1, skaicius+1):
#         for sk in range(1, eilute+1):
#             print(sk)
#         print('')
#         sk += 1
#     print()
#     atspausdinta += kiek_eiluteje
#     kiek_eiluteje += 1



print('=========1============')
# kartai = int(input('Iveskite kiek kartu norite kartoti fraze: '))
# fraze = input('Iveskite norima fraze: ')
# while True:
#     if kartai > 0:
#         print((fraze + '\n') * kartai)
#         break
#     else:
#         print('Salyga nekorektiska')

print('=========2============') #nesigauna padaryt break po dvieju atspausdinimu
# atspausdinta = 0
# kartai = int(input('Iveskite kiek kartu norite kartoti fraze: '))
# fraze = input('Iveskite norima fraze: ')
# while True:
#     atspausdinta += kartai
#     if kartai > 0:
#         print((fraze + '\n') * kartai)
#         if atspausdinta > 2:
#             break
#     else:
#         print('Salyga nekorektiska')
#

# atspausdinta = 0
# kartai = int(input('Iveskite kiek kartu norite kartoti fraze: '))
# fraze = input('Iveskite norima fraze: ')
# while kartai > 0:
#     atspausdinta += 1
#     print(fraze)
#     if atspausdinta >= 2:
#         break

print('=========3============')
# atspausdinta = 0
# kartai = int(input('Iveskite kiek kartu norite kartoti fraze: '))
# fraze = input('Iveskite norima fraze: ')
# while True:
#     atspausdinta += 1
#     if kartai > 0:
#         print(((str(atspausdinta * kartai) + fraze) + '\n') * kartai)
#         break
#     else:
#         print('Salyga nekorektiska')


print('=========4============')
# atspausdinta = 0
# kartai = int(input('Iveskite kiek kartu norite kartoti fraze: '))
# fraze = input('Iveskite norima fraze: ')
# while True:
#     if atspausdinta == 2:
#         atspausdinta += 1
#         continue
#     if kartai == atspausdinta:
#         break
#     print(f'{atspausdinta+1} {fraze}')
#     atspausdinta += 1


# atspausdinta = 0
# kartai = int(input('Iveskite kiek kartu norite kartoti fraze: '))
# fraze = input('Iveskite norima fraze: ')
# while atspausdinta < kartai:
#     atspausdinta += 1
#     if atspausdinta == 3:
#         continue
#     print(f'{atspausdinta} {fraze}')




print('=========5============')
# seka = [10,100,3]
# lyginiai = 0
# nelyginiai = 0
# while True:
#     for skaicius in seka:
#         if skaicius %2 == 0:
#             # print(skaicius, 'lyginis')
#             lyginiai += 1
#         else:
#             # print(skaicius, 'nelyginis')
#             nelyginiai += 1
#     break
# print('lyginiu skaiciu yra: ', lyginiai)
# print('nelyginiu skaiciu yra: ', nelyginiai)


print('=========6============')
# seka = [9,99,4]
# lyginiai = 0
# nelyginiai = 0
# while True:
#     kiek_elementu = int(input('Kiek nelyginiu elementu norite, kad butu atspausdinta?: '))
#     for skaicius in seka:
#         if skaicius %2 != 0:
#             print(skaicius, 'nelyginis')
#             nelyginiai += 1
#             if nelyginiai >= kiek_elementu:
#                 break
#         else:
#             print(skaicius, 'lyginis')
#             lyginiai += 1
#     break
# # print('lyginiu skaiciu yra: ', lyginiai)
# # print('nelyginiu skaiciu yra: ', nelyginiai)


print('=========7============')
# seka = list(range(9,99,4))
# suma = 0
# i = 0 # sekos indeksas
# while i < len(seka):
#     if seka[i] %2 != 0:
#         print(seka[i], 'nelyginis')
#         suma += seka[i]
#     i += 1
# print('Pasirinktu skaiciu suma: ', suma)


print('=========8============')
# seka = list(range(9,99,4))
# suma = 0
# i = 0
# nelyginiai = []
# kiek_elementu = int(input('Kiek nelyginiu elementu norite, kad butu atspausdinta?: '))
# while i < len(seka):
#     if seka[i] %2 != 0:
#         nelyginiai.append(seka[i])
#         print(seka[i], 'nelyginis')
#         suma += seka[i]
#     i += 1
# print('Pasirinktu skaiciu suma: ', suma)






print('=========1=2============')
# nelyg_sveikas_skaicius = int(input('Iveskite nelygini sveikaji skaicius: '))
# for sk in range(1, nelyg_sveikas_skaicius//2+2): #nuo 1 iki pasirinkto skaiciaus padalinus is 2 ir numetus liekana +2 (nes pask neieina)
#     print('*' * sk)
# for sk in range(nelyg_sveikas_skaicius//2, 0, -1): #atvirkstinis variantaas
#     print('*' * sk)

print('=========1=3============')
# skaicius_n = int(input('Iveskite norima sveikaji skaiciu: '))
# skaicius_m = int(input('Iveskite norima sveikaji skaiciu: '))
# if skaicius_m < skaicius_n:
#     for sk in range(skaicius_m, skaicius_n+1):
#         print(sk)
# elif skaicius_m > skaicius_n:
#     for sk in range(skaicius_m, skaicius_n-1, -1):
#         print(sk)
# else:
#     print('Salyga nekorektiska')


print('=========1=4============')
# skaicius_n = int(input('Iveskite norima sveikaji skaiciu: '))
# skaicius_m = int(input('Iveskite norima sveikaji skaiciu: '))
# if skaicius_m < skaicius_n:
#     for sk in range(skaicius_m, skaicius_n+1):
#         if sk %2 != 0:
#             print(sk)
# elif skaicius_m > skaicius_n:
#     for sk in range(skaicius_m, skaicius_n-1, -1):
#         if sk %2 != 0:
#             print(sk)
# else:
#     print('Salyga nekorektiska')


print('=======04.07====1=============')
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma = 0
# for sk in list:
#     suma += sk
# print('skaiciu suma: ', suma)


print('=======04.07====2=============')
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lyginiai_suma = 0
# nelyginiai_suma = 0
# for sk in list:
#     if sk %2 == 0:
#         lyginiai_suma += sk
#     elif sk %2 != 0:
#         nelyginiai_suma += sk
#     else:
#         print('Salyga nekorektiska')
# print('lyginiu suma: ', lyginiai_suma)
# print('nelyginiu suma: ', nelyginiai_suma)


print('=======04.07====3=============')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for sk in list:
    if sk > 0:
        new_list.append(sk**2)
    else:
        print('Salyga nekorektiska')
print('orginalus sarasas: ', list)
print('naujasis sarasas: ', new_list)


print('=======04.07====4=============')
skaicius = int(input('Iveskite norima skaiciu: '))
skaicius2 = skaicius #kad issisaugoti pradini skaiciu ji issaugoti kaip kintamaji
rezultatas = 1
while skaicius > 0:
    rezultatas *= skaicius
    skaicius -= 1 #nes faktoriala skaiciuojam mazejimo tvarka (5*4*3...)
print(f'Skaiciaus {skaicius2} faktorialas yra {rezultatas}')