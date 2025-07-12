# #„Python“ neturi funkcijos tipo matricoms. Tačiau sąrašo sąrašą galime traktuoti kaip matricą. Pavyzdžiui:
#
# # A = [[1, 4, 5], [-5, 8, 9],[-5, 8, 0],[-5, 8, 9]]
# # print(A)
#
# # Naudojant sąrašus kaip matricą, atliekamos paprastos skaičiavimo užduotys,
# # tačiau sudėtingesniems skaičiavimams atlikti patogiau dirbti su „Python“
# # matricomis naudojant „NumPy“ paketą.
#
import random

import numpy as np
# a = np.array([1, 2, 3])
# print(a)
# Rezultatas: [1, 2, 3]
# print(type(a)) # Rezultatas: <class 'numpy.ndarray'>
#
# # NumPy masyvo klasė vadinama ndarray
# # Matrica su „NumPy“
#
A=np.array([[2,3,-9],[2,3,5]])
print(A)
B=np.array([[9.5,-3.4,12.78],['k','l','m']]) #matricoje galima saugoti skirtingų tipų duomenis, taciau ji yra sutapatinimai
print(B)
C=np.array([5, 7.5, 'zodis', -3, 'tekstas', False, (3, 4), [4, 6]], dtype=object) # cia masyvas
print(C)
# D=np.array([2,5,7],[0,2]) #pagrindinis reikalavimas islaikyti vienoda eiluciu/stulpeliu skaiciu
# print(D)
#
# #Veiksmai su tarp kelių skaičius turinčių matricų galimi tik tada, kai matricos eilučių ir stulpelių skaičius sutampa.
A=np.array([[-12,15,7],[0,9,7]])
B=np.array([[-7,5,1],[-9,2,10]])
print('A matrica: \n',A)
print('B matrica: \n',B)
print('Matricų sudėtis: \n',A+B)
print('Matricų atimtis: \n',A-B)
print('Matricų daugyba: \n',A*B)
print('Matricų dalyba: \n',A/B) # dalyba negalima jei bent viena is dalmens matrcos skaiciu yra nulis
# # Funkcija np.all(X) grazina True/False jei yra skaiciu lygiu nuliui arba ne
print(np.all(A)) #grazina false jei yra nuliu
print(np.all(B)) #grazina true jei nera nuliu
# C=np.array([[7,3],[0,12]])
# print(A+C) #matricų dydis skirtingas
#
# # #Palyginimui. Jei A ir C kursime ne kaip matricas, o kaip sąrašus, sudedami bus ne jų elementai, o tiesiog apjungiami sąrašai.
A = [-12, 15, 7],[0, 9, 7]
C = [7, 3],[0, 12]
print(A + C)
#
# #Matricų dauginimas
# #Svarbiausia sąlyga dauginant matricas – eilučių skaičius turi atitikti kitos matricos stulpelių skaičių
# #Norėdami sudauginti dvi matricas, naudojame dot() metodą.
#
A = np.array([[-1, 2], [2, 2]])
print('A matrica\n', A)
B = np.array([[0, -3],[4, 2]])
print('B matrica\n', B)
print('Matricu daugyba1\n', A.dot(B))
A=np.array([[-12,15,7],[0,9,7]])
B=np.array([[-7,5],[-9,2],[0,0]])
print('Matricu daugyba2\n', A.dot(B))
#
# # Matricų transponavimas
# # Matricų transponavimui naudosime numpy.transpose()
#
A = np.array([[1, 1],[2, 1], [3, -3]])
print(A.transpose())
#
# # Veiksmai su matricos elementais, eilutėmis ir stulpeliais
# #Kaip sąrašus, taip ir matricos elementus galime pasiekti naudodami indeksą.
#
A = np.array([[-12, 0, 23], [7, 3, -2], [0.1, 0.2, 0.3]])
print('A matrica\n', A)
print('A matricos trecia eilute\n', A[2])
print('A matricos antra eilute nuo galo\n', A[-2])
print('A matricos antros eilutes trecio stulpelio emelemntas: ', A[1][2])
print('A matricos antros eilutes trecio stulpelio emelemntas: ', A[1,2])
#
# #Turint vienmatį masyvą, elementai skaičiuojami tik vienu parametru - eilute
A = np.array([-12, 0, 23, 7, 3, -2, 0.1, 0.2, 0.3])
print(A[5])
#
# #Masyvo/matricos elementų atrinkimas
A = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print('A matrica\n', A)
print('\nPirmas stulpelis: ', A[:1])
print('Pirma eilute: ', A[0,:])
print('Paskutine eilute: ', A[-1,:])
print('Paskutinis stulpelis: ', A[:,-1])
print('Visu eiluciu, 2-3 stulpeliai\n', A[:,[1,4]])
print('Visu eiluciu, 2-3 stulpeliai\n', A[:,1:2])
print('visu stulpeliu, 2-3 eilutes\n', A[[1,2],:])
print('Nuo antros iki paskutines eilutes, nuo pirmo iki trecio stulpeliai\n', A[1:,:3])
print('=========================================')
print('Nuo antros iki paskutines eilutes, stulpeliai - pirmas, trecias ir penktas\n', A[1:,[0,2,4]])
print('=========================================')
print('Nuo antros iki paskutines eilutes, stulpeliai nuo pradzios iki 5 zingsniu 2\n', A[1:,:5:2])
print('=========================================')
print('Nuo antros iki paskutines eilutes, stulpeliai nuo pradzios iki pabaigos zingsniu 2\n', A[1:,::2])
# # # ir taip toloau .......
#
mat = np.random.randint(20,size=(8,9))
print(mat)
print('=========================================')
# #
print(mat[::2,0]) #A[eilut,stulpel] , A[pre:pbe:zne, prs:pbs:zns]
print('=========================================')
print(mat[0::2,:]) #A[eilut,stulpel] , A[pre:pbe:zne, prs:pbs:zns]
print('=========================================')
print(mat[::2,::2]) #A[eilut,stulpel] , A[pre:pbe:zne, prs:pbs:zns]
print('=========================================')
print(mat[:,4:5]) #A[eilut,stulpel] , A[pre:pbe:zne, prs:pbs:zns]
print('=========================================')
#
# # Matricos dydzio - eiluciu ir stulpeliu nustatymas
mat = np.random.randint(20,size=(8,9))
print(np.size(mat)) # kiek elementu
print(len(mat)) # kiek elementu
print(np.shape(mat))
e,s = np.shape(mat)
print(e,s)
# #
# # print(len(mat[:,0]))
# # print(len(mat[0,:]))
#
# # Funkciju naudojimo pvz. :
eye_mas = np.eye(5,6)
print(eye_mas)
one_mas = np.ones((3,3), dtype=int)
print(one_mas)
flat_eye_mas = eye_mas.flatten()
print(flat_eye_mas)
print('=======================')
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
b1 = np.array([[5],[6]])
b2 = np.transpose(b)
print(b2)
print(np.concatenate((a, b), axis=0)) # 0 prijungia kaip eilute
print(np.concatenate((a, b1), axis=1)) # 1 prijungia kaip stulpeli
print(np.concatenate((a, b.T), axis=1)) # 1 prijungia kaip stulpeli. mat.T - greita trasponacija
#
# # https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
#
mat = np.random.randint(20,size=(8,9))
print(mat)
print(mat.min())
istiesinta = mat.flatten()
print(istiesinta)
print(np.count_nonzero(mat == mat.min()))
print(np.count_nonzero(mat == 5))

#
# # Elemento įterpimas masyve
A=np.random.randint( low=10,high=15,size=5)
print('Masyvas A:\n',A)
print('Vieno elemento įterpimas iš galo:\n',np.append(A,12))
sar=[7,14,15,16]
print('Sąrašo įterpimas iš galo:\n',np.append(A,sar))
print('Vieno elemento įterpimas į nurodytą vietą:\n', np.insert(A,0,111)) #(saltinis,pozicija,reiksme)
print('Saraso įterpimas į nurodytą vietą:\n', np.insert(A,0,sar)) #(saltinis,pozicija,reiksme)
#
# # Elemento įterpimas matricoje
#
# # Vieno elemento matricoje įterpti negalima. Bet galima įterpti vieną eilutę, ar vieną stulpelį.
# # Vienintelė sąlyga stulpelių skaičius eilutėje turi būti toks pat, kaip matricoje.
# # Arba eilučių skaičius stulpelyje turi būti toks pat, kaip matricoje.
# # A=np.insert(šaltinis, pozicija,[seka],axis=0/1)
# # Šaltinis - į kokią matricą įterpti
# # Pozicija - eilutės ar stulpelio numeris
# # Seka - privaloma tiek elementų, kiek yra tame stulpelyje ar eilutėje
# # Axis: 0 eilutės įterpimui; 1 stulpelio įterpimui
#
A= np.random.randint(low=5,high=7,size=(3,2))
print('A matrica \n',A)
B= np.insert (A,0,[88,88,88],axis=1)
print('A matricoje pirmame stulpelyje: \n', B)
C= np.insert(A,1, [123,123], axis=0)
print('A matricos antroje eilutėje \n',C)
#
# # Elemento istrinimas masyve
A= np.random.randint(low=0,high=7,size=10)
B= np.delete(A,2)
print(A)
print('A masyvas su panaikintu 2 pozicijos elementu \n',B)
#
# # Elemento istrinimas matricoje
A= np.random.randint(low=5,high=7,size=(3,2))
B= np.delete(A,1,axis=0)
print('A matrica, ištrynus pirmą eilutę \n',B)

A=np.random.uniform(low=10,high=7, size=5)
print('Realiųjų skaičių aibės masyvas: \n',A)
np.set_printoptions(precision=4)
print('Formatuotas masyvas: \n',A)
A = np.round(A,2)
print('Formatuotas masyvas: \n', A)

#####################################U Z D U O T Y S######################################
from random import randint
print('===================1================')
A = np.random.randint(10, size=5)
listas = [randint(0,21) for i in range(4)]
print(A)
print(listas)
B = np.delete(A, 2)
print('Masyvas su panaikintu elementu:', B)
C = np.insert(A,5, listas)
print('A masyvas sujungtas su B sarasu:', C)

print('===================2================')
# listas = [randint(0,21) for i in range(12)]
# A = np.array(listas)
# print(listas)
# print(A)
# indeksas = int(input('Iveskite elemento pozicija, kuri norite perkelti i masyvo gala (1-12): '))
# if indeksas > 0 and indeksas <= len(A):
#     elementas = A[indeksas -1]
#     masyvas = np.delete(A, indeksas-1)
#     masyvas = np.append(masyvas, elementas)
#     print("Pakeistas masyvas:", masyvas)
# else:
#     print("Netinkamas indeksas!")

print('===================3================')
# listas = [randint(0,21) for i in range(12)]
# print(listas)
# maziausia = min(listas)
# didziausia = max(listas)
# print('Maziausia reiksme: ', maziausia)
# print('Didziausia reiksme: ', didziausia)
# listas_be_min_max = [sk for sk in listas if sk != maziausia and sk != didziausia]
# print('Sarasas be min max reiksmiu:')
# print(listas_be_min_max)
# A = np.array(listas)
# pozicija = int(input('Iveskite elemento pozicija, i kuria norite iterpti skaiciu 12345 (1-12): '))
# print(np.insert(A, pozicija-1,12345))


print('===================4================')
# elementu_sk = int(input("Iveskite, kiek elementų tures masyvas: "))
#
# A = np.random.uniform(size=elementu_sk)
# print(A)
# print("Masyvas:", np.round(A, 3))
#
# while True:
#         eilutes = int(input("Iveskite eiluciu skaiciu: "))
#         stulpeliai = int(input("Iveskite stulpeliu skaiciu: "))
#         if eilutes * stulpeliai != elementu_sk:
#             print('Ivedete netinkamus skaicius. Prasome kartoti.')
#         else:
#             B = A.reshape(eilutes, stulpeliai)
#             np.set_printoptions(precision=2)
#             print('Matrica:', B)
#             break

# print('===================5================')
# A = np.random.randint(20, size=(5,4))
# print(A)
# # matrica = A.reshape(5,4)
# # print(matrica)
# while True:
#     istrynimas = int(input('Kuri stulpeli norite istrinti? (1-4): '))
#     if istrynimas >= 1 and istrynimas <= 4:
#         B= np.delete(A,istrynimas-1, axis=1)
#         print('Galutine matrica: \n', B)
#         break
#     else:
#         print('Ivedete netinkamus skaicius. Prasome kartoti')
#
# print('===================6================')
# A = np.random.randint(20, size=(random.randint(2,10), random.randint(2,10)))
# print(A)
# while True:
#     eilute = int(input('Pasirinkite eilute kurios skaiciu suma norite pamatyti: '))
#     if eilute > 0 and eilute <= 10:
#         print('Matrica')
#         print(A)
#         suma = sum(A[eilute-1])
#         print(f'Pasirinkta {eilute} eilute. Jos reiksmiu suma yra {suma}')
#         break
#     else:
#         print('Ivedete netinkama skaiciu. Prasome kartoti')

print('===================7================')
A = np.random.randint(20, size=(4,6))
elementai = []
print('Pradine matrica')
print(A)
for elementas in range(4):
    skaicius = int(input('Iveskite norima prideti skaiciu: '))
    elementai.append(skaicius)
print(elementai)
B = np.insert(A, -1, elementai, axis=1)
print('Atnaujinta matrica:')
print(B)