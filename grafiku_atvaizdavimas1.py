# Grafikų atvaizdavimas (Matplotlib):
# Kaip suformuoti grafiką iš sąrašų:
# %matplotlib inline #Jupyter notebook
from matplotlib import pyplot as plt

# metai = [1978, 1988, 1998, 2008, 2018]
# temperatura = [5.8, 5.9, 6.2, 6.9, 7.2]
#
# plt.figure(1)
# plt.plot(metai, temperatura)
#
# # Kaip apipavidalinti grafiką:
# plot2 = plt.figure(2)
# plt.plot(metai, temperatura)
#
# plt.title("Vidutinė temperatūra")
# plt.xlabel("Metai")
# plt.ylabel("Laipsniai (Celcijaus)")
#


#Kaip pridėti papildomą kreivę:
#
# metai = [1978, 1988, 1998, 2008, 2018]
# vilnius = [5.8, 5.9, 6.2, 6.9, 7.2]
# ispanija = [15.8, 15.9, 16.2, 16.9, 17.2]
#
# plt.title("Vidutinė temperatūra")
# plt.xlabel("Metai")
# plt.ylabel("Laipsniai (Celcijaus)")
# # plot1 = plt.figure(1)
# plt.plot(metai, vilnius)
# # #
# # # # # print('#####################')
# # # # plot2 = plt.figure(2)
# plt.plot(metai, ispanija)
# plt.legend(["Vilnius", "Ispanija"], loc= 'lower right') # Kaip įvardinti kreive - legenda


plt.show()

# # Kaip atspausdinti grafiką iš Pandas duomenų paketo:

import pandas as pd
from matplotlib import pyplot as plt
#
orai = {
'data': ['7/1/2019', '7/2/2019',
'7/3/2019','7/4/2019','7/5/2019'],
'temperatura': [32, 35, 28, 24, 22],
'vejas': [6,7,2,4,5],
'oras': ['Lietus', 'Saulėta',
'Saulėta','Saulėta','Debesuota']}
# #
df = pd.DataFrame(orai)
# plt.plot(df.data, df.temperatura)
# plt.show()

# Kitokio tipo grafikas:
#
# plt.plot(df.data, df.temperatura, "*")
# plt.show()
# #
# Kaip atspausdinti grafiką iš atrinkto duomenų paketo:
#
# pd.set_option('display.max_rows', None)
# data = pd.read_csv('countries12.csv')
# # #
# print(data)
# us = data[data.country == 'United States']
# china = data[data.country == 'China']
# print(us)
# print("===============")
# print(china)
# # # #
# plt.plot(us.year, us.population / 10**6)
# plt.plot(china.year, china.population / 10**6)
# plt.legend(['JAV', 'Kinija'])
# plt.xlabel('Metai')
# plt.ylabel('Populiacija (mln.)')
# plt.show()

# # Užduotis:
#
# # Parsisiųsti countries.csv failą iš https://www.csdojo.io/data
# # Susikurti iš jo duomenų paketą (Pandas DataFrame)
# # Atspausdinti tik metų stulpelį
# # Atspausdinti norimos šalies didžiausius/mažiausius/vidutinius gyventojų kiekius
# # Atspausdinti bendrą lentelės ataskaitą
# # Išsaugokite sukurtą DataFrame į duomenų bazę.
# # Grafike atvaizduoti kelių skirtingų šalių populiacijos pokytį per metus
# # Padaryti, kad grafikas turėtų pavadinimą, būtų įvardintos x/y ašys bei kreivės ir dar kass tik norite.