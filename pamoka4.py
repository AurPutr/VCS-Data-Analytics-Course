# # seka = list(range(1, 100, 7))
# # print(seka)
# # print()
# # seka2 = list(range(3, 94, 11))
# # print(seka2)
# # print()
# # seka3 = list(range(10, 0, -1))
# # print(seka3)
# # print()
# # seka4 = list(range(100, 0, -10))
# # print(seka4)
# # print()
# # seka5 = list(range(10, -1, -1))
# # print(seka5)
# # print()
# # seka6 = list(range(50, 0, -5))
# # print(seka6)
# #
# # for skaicius in range(-4, 11):
# #     if skaicius % 2 == 0:
# #         print(f'skaicius {skaicius} yra lyginis')
# #     else:
# #         print(f'skaicius {skaicius} yra nelyginis')
# #1
# # vardas = input('Iveskite savo varda: ')
# # kiek = int(input('Iveskite kiek kartu: '))
# #
# # for kartai in range(1,kiek + 1):
# #     print(kartai, vardas)
# #2
# for skaicius in range(0, 16):
#     print(skaicius)
# print('=======================')
# #3
# for skaicius in range(1, 20, 3):
#     print(f'[{skaicius}]')
# print('=========================')
# #4
# for skaicius in range(1, 21):
#     if skaicius %4 == 0:
#         print(skaicius, 'dalinasi is 4')
# print('=======================')
# #6
# for skaicius in range(1, 16):
#     if skaicius %2 == 0:
#         print(skaicius, 'lyginis')
#     else:
#         print(skaicius, 'nelyginis')
#
# print('=======================')
# #7
# # pradzia = int(input('Iveskite reziu pradzia: '))
# # pabaiga = int(input('Iveskite reziu pabaiga: '))
# # if pradzia < pabaiga:
# #     for skaicius in range(pradzia, pabaiga+1):
# #         print(skaicius, ' ', skaicius**2)
# # else:
# #     print('pasirinkti skaiciai netinka salygai')
# print('=======================')
# #8
# # pradzia = int(input('Iveskite reziu pradzia: '))
# # pabaiga = int(input('Iveskite reziu pabaiga: '))
# # if pradzia < pabaiga:
# #     for skaicius in range(pradzia, pabaiga+1):
# #         if skaicius %2 != 0 or skaicius %8 ==0:
# #             print(skaicius, 'nelyginis arba dalijasi is 8')
# # else:
# #     print('pasirinkti skaiciai netinka salygai')
# print('=======================')
# #9
# # vardas = input('Iveskite savo varda: ')
# # for kartai in vardas:
# #     print('Labas,', vardas)
# print('=======================')
# #10
# # elementas = [88, 65, 21, 26, 47]
# # for sk in elementas:
# #     if sk %2 == 0:
# #         print(sk, 'skaicius yra lyginis')
# print('=======================')
# #11
# # pradzia = int(input('Iveskite reziu pradzia: '))
# # pabaiga = int(input('Iveskite reziu pabaiga: '))
# # if pradzia < pabaiga:
# #     skaicio_tipas = input('Koki skaicius norite matyti lyginiai/nelyginiai: ')
# #     if skaicio_tipas == 'lyginiai' or skaicio_tipas == 'Lyginiai':
# #         for skaicius in range(pradzia, pabaiga+1):
# #             if skaicius %2 == 0:
# #                 print(skaicius, 'yra lyginis')
# #     if skaicio_tipas == 'nelyginiai' or skaicio_tipas == 'Nelyginiai':
# #         for skaicius in range(pradzia, pabaiga+1):
# #             if skaicius %2 != 0:
# #                 print(skaicius, 'yra nelyginis')
# # else:
# #     print('Ivesti reziai neatitinka salygos')
# print('=======================')
# #12
dydis = int(input('Iveskite sveikaji skaiciu: '))
for eilute in range(1, dydis+1):
    print('*' * eilute)
# print('=======================')
# #13
# # zodis = input('Iveskite norima zodi: ')
# # kartai = int(input('Iveskite kiek kartu: '))
# # for raide in zodis:
# #     print(raide * kartai)
# print('=======================')
# #14
# # skaicius1 = int(input('Iveskite norima skaiciu: '))
# # skaicius2 = int(input('Iveskite norima skaiciu: '))
# # rezultatas = 0
# # for sk in range(skaicius2):
# #     rezultatas += skaicius1
# #     # if rezultatas == skaicius1 * skaicius2:
# # print('Sandauga: ', rezultatas)
# # print('=======================')
# #15
# suma = 0
# for sk in range(100):
#     suma += sk
# print('Suma yra: ', suma)
# print('=======================')
# #16
# suma = 0
# for sk in range(20,50):
#     if sk %2 == 0:
#         suma += sk
# print('Lyginiu suma: ', suma)
# print('=======================')
# # 17
# suma = 0
# for sk in range(30,60):
#     if sk % 2 != 0:
#         suma += sk
# print('Nelyginiu suma: ', suma)
# print('=======================')
# # 18
# suma = 0
# for sk in range(1000):
#     if sk %3 == 0 or sk %5 == 0:
#         suma += sk
# print('Skaiciu zemesniu uz 1000 kurie dalinasi is 3 arba 5 suma: ', suma)
# print('=======================')
# # 19
# for number in range(1,101):
#     if number %3 == 0 and number %5 == 0:
#         print('FizzBuzz')
#     elif number %5 == 0:
#         print('Buzz')
#     elif number %3 == 0:
#         print('Fizz')
#     else:
#         print(number)
#
# for i in range(1, 4):
#     print('pirmo ciklo pradzia, i =', i)
#     for j in range(1, 4):
#         print('antras ciklas pradzia, j =', j)
#         for k in range(1, 4):
#             print('trecias ciklas pradzia, k =', k)
#         print('antras ciklas pabaiga')
#     print('pirmo ciklo iteracijos pabaiga')