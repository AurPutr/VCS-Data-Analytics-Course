# Python DateTime modulis

# 1. calendar išveda kalendorių ir teikia funkcijas naudojant idealizuotą Grigaliaus kalendorių.
# 2. DateTime tiekia klases, skirtas manipuliuoti datomis ir laiku.
# 3. time suteikia su laiku susijusias funkcijas, kai datos nereikia.

# Pagrindinis „DateTime“ tikslas yra palengvinti prieigą prie objekto atributų,
# susijusių su datomis ir laiku.

# „DateTime“ pateikia tris klases, kurias naudoja dauguma žmonių:

# DateTime.date yra idealizuota data, kuri reiškia, kad Grigaliaus kalendorius tęsiasi be galo į ateitį ir praeitį. Šis objektas saugo metus, mėnesį ir dieną kaip atributus.
# DateTime.time yra idealizuotas laikas, kai daroma prielaida, kad per dieną yra 86 400 sekundžių be šuolio sekundžių. Šis objektas saugo valandą, minutę, sekundę, mikrosekundę ir tzinfo (laiko juostos informaciją).
# DateTime.datetime yra datos ir laiko derinys. Jis turi visus abiejų klasių atributus.

# Datetime kintamasis gali išsaugoti datą ir/arba laiką.
# Jis importuojamas per import datetime


import datetime


# # Dabartinė data ir laikas:
data_ir_laikas_dabar = datetime.datetime.today()
data_ir_laikas_dabar_2 = datetime.datetime.now()

print(data_ir_laikas_dabar)
print(type(data_ir_laikas_dabar))
print(data_ir_laikas_dabar_2)

# #Tik data:
data_dabar = datetime.date.today()
data_dabar_2 = datetime.datetime.today().date()
print(data_dabar_2)
print(data_dabar)
#
# # Tik laikas:
laikas_dabar = datetime.datetime.today().time()
print(laikas_dabar)
#
# # Nustatome patys data ir laiką
nusistatatome_data_ir_laika1 = datetime.datetime(1990, 3, 14, 12,30,14)
nusistatatome_data_ir_laika2 = datetime.date(1990, 3, 14)
nusistatatome_data_ir_laika3 = datetime.time(12, 30, 14)
print(nusistatatome_data_ir_laika1)
print(nusistatatome_data_ir_laika2)
print(nusistatatome_data_ir_laika3)
#
# # Nusistatome kokiu formatu bus atspausdinta data ir laikas
print(nusistatatome_data_ir_laika1.strftime("%d %B %Y ")) #%p = PM/AM
#
#
# # Datetime formatavimo kodai: https://www.w3schools.com/python/python_datetime.asp
#
# #Laikas su lietuviškumu:
import locale
#
# # Nusistatome laika patys
locale.setlocale(locale.LC_TIME, 'lt_LT.UTF8')
nustatyta_lietuviska_data_ir_laikas = datetime.datetime(2022, 9, 14, 23, 55, 00)
print(nustatyta_lietuviska_data_ir_laikas)
print(nustatyta_lietuviska_data_ir_laikas.strftime("%A, %d %B %Y %I:%M ").replace('Ä ','č')) #%p - popiet
kringeliai=['Ä ','Å¡','Å¾','Å«','Ä—']
liet_zenk = ['č','š','ž','ū','ė']
# # pakeitimai = [('',''),('',''),('',''),('',''),('','')]
isvedimas = nustatyta_lietuviska_data_ir_laikas.strftime("%A, %d %B %Y %I:%M ")
print('Pries pakeitima: ',isvedimas)
#
if 'Ä ' in isvedimas:
        isvedimas = isvedimas.replace('Ä ','č')
if 'Å¡' in isvedimas:
        isvedimas = isvedimas.replace('Å¡','š')
if 'Å¾' in isvedimas:
        isvedimas = isvedimas.replace('Å¾','ž')
if 'Å«' in isvedimas:
        isvedimas = isvedimas.replace('Å«','ū')
if 'Ä—' in isvedimas:
        isvedimas = isvedimas.replace('Ä—','ė')
print('Po pakeitimo: ', isvedimas)
#
print(isvedimas.title())
#
#
# # Kaip pridėti ar atimti laiką:
dabar = datetime.datetime.now()
dabar1 = datetime.date.today()
print(dabar)
print(dabar1)
#
# # Jei norime atimti pvz 5 dienas iš dabar
print(dabar - datetime.timedelta(days = 5))
print(dabar1 - datetime.timedelta(days = 5))
#
# # Jei norime prideti pvz 5 valandas prie dabar
print(dabar + datetime.timedelta(hours = 5))
#
# # Jei norime prideti pvz 20 dienu ir 8 valandas prie dabar
print(dabar + datetime.timedelta(days = 20, hours = 5))
#
# # Kaip sužinoti datų skirtumą (pvz. dienomis):
nepriklausomybes_diena = datetime.date(1990, 3, 11)
skirtumas = dabar1 - nepriklausomybes_diena
print(skirtumas.days)
#
# # Kaip įvesti datą/laiką:
# ivesti_data = input("Iveskite data tokiu formatu metai-menuo-diena val:min:s : ")
# data = datetime.datetime.strptime(ivesti_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data)
# print(skirtumas.days)
#
# # Kaip iš datetime atskirai ištraukti metus, mėnesį, valandas...?
dabar1 = datetime.datetime.now()
print('sitas', dabar)
print(dabar1.year, type(dabar1.year))
print(dabar1.month)
print(dabar1.weekday())
print(dabar1.day)
print(dabar1.hour)
print(dabar1.minute)
print(dabar1.second)
print(dabar1.microsecond)
#
# # Naudodami timedelta galime pamatuoti,
# # per kiek laiko mūsų kompiuteris susidorojo su užduotimi,
# # pvz.:

# pradzia = datetime.datetime.today()
# for n in range(300000):
#     print("Labas")
# pabaiga = datetime.datetime.today()
# print(f"Programa uztruko {(pabaiga - pradzia).total_seconds()}")

# Taip pat galime į kodą įdėti pauzę:
import time

for m in range(10):
    print("Labas rytas")
    time.sleep(2)