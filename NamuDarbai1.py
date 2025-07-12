# #1
# skaicius = float(input('Iveskite norima skaiciu: '))
# skaicius2 = float(input('Iveskite dar viena norima skaiciu: '))
# print('Ivestu skaiciu suma: ', skaicius+skaicius2)
# #2
# print()
# print('==========================================')
# print()
# vardas = input('Iveskite savo varda: ')
# print('Sveiki ', vardas)
# #3
# print()
# print('==========================================')
# print()
# ilgis = float(input('Iveskite staciakampio ilgi: '))
# plotis = float(input('Iveskite staciakampio ploti: '))
# print('Staciakampio plotas: ', round(ilgis*plotis,3))
# #4
# print()
# print('==========================================')
# print()
# celsijus = float(input('Iveskite temperatura Celsijaus laipsniais: '))
# farenheitas = (celsijus*9/5)+32
# print('Temperatura Farenheito laipsniais: ', (celsijus*9/5)+32)
# print('Temperatura Farenheito laipsniais: ', farenheitas)
# #5
# print()
# print('==========================================')
# print()
# skaicius = int(input('Iveskite norima sveikaji skaicius: '))
# if skaicius %2 == 0:
#     print('Skaicius yra lyginis')
# else:
#     print('Skaicius yra nelyginis')
# #6
# print()
# print('==========================================')
# print()
# skaicius = int(input('Parasykite norima sveikaji skaiciu: '))
# skaicius2 = int(input('Parasykite dar viena norima sveikaji skaiciu: '))
# if skaicius > skaicius2:
#     print('Didesnis skaicius yra: ', skaicius)
# elif skaicius < skaicius2:
#     print('Didesnis skaicius yra: ', skaicius2)
# else:
#     print('Skaiciai lygus')
# #7
# print()
# print('==========================================')
# print()
# spalva = input('Parasykite savo megstamiausia spalva: ')
# print('Mano megstamiausia spalva taip pat yra ', spalva)
# #8
# print()
# print('==========================================')
# print()
# skaicius = int(input('Parasykite norima sveikaji skaiciu: '))
# if skaicius > 0:
#     print(f' {skaicius} yra teigiamas')
# elif skaicius < 0:
#     print(f'{skaicius} yra neigiamas')
# elif skaicius == 0:
#     print('Skaicius lygus 0')
# # 9
# print()
# print('==========================================')
# print()
# amzius = int(input('Iveskite savo amziu: '))
# lytis = input('Iveskite savo lyti (is mazosios raides): ')
# if amzius >= 18 and lytis == 'vyras':
#     print('Vyras')
# elif amzius < 18 and lytis == 'vyras':
#     print('Berniukas')
# elif amzius >= 18 and lytis == 'moteris':
#     print('Moteris')
# elif amzius < 18 and lytis == 'moteris':
#     print('Mergaite')
# # 10
# print()
# print('==========================================')
# print()
# skaicius = int(input('Iveskite norima vienzenkli skaicius: '))
# print(skaicius, skaicius * (skaicius + 1) // 2)
# # 11
# print()
# print('==========================================')
# print()
# ugis = float(input('Iveskite savo ugi (metrais): '))
# svoris = float(input('Iveskite savo svori (kg): '))
# KMI = svoris/(ugis**2)
# print('Jusu kuno mases indeksas (KMI) yra: ', round(KMI,2))
# # 12
# print()
# print('==========================================')
# print()
# balansas = float(input('Iveskite savo saskaitos likuti: '))
# issigryninti = int(input('Iveskite suma, kuria norite issigryninti: '))
# if balansas - issigryninti >= 0:
#     print(f'Issigryninote: {issigryninti}\nSaskaitos likutis: {balansas-issigryninti}')
# elif balansas - issigryninti < 0:
#     print('Jusu saskaitoje nepakanka lesu')
