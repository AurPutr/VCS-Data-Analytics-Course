# mano = 1
# atsakymas = f'mano zodziai {mano}'
# with open('rasau.txt','w') as failas:
#     failas.write(atsakymas + '\n')
#     failas.write('Saulyte')


# failas = open('matricos.txt','w',encoding='utf8')
# A=np.random.uniform(low=10,high=7, size=5)
# print(f'Realiųjų skaičių aibės masyvas: \n{A}')
# failas.write(f'Realiųjų skaičių aibės masyvas: \n{A}\n')
# np.set_printoptions(precision=4)
# print(f'Formatuotas masyvas: \n{A}')
# failas.write(f'Formatuotas masyvas: \n{A}\n')
# A = np.round(A,2)
# print(f'Formatuotas masyvas: \n{A}')
# failas.write(f'Formatuotas masyvas: \n{A}')
# failas.close()


from csv import reader
with open('autoparkas.csv') as failas:
    csv_reader = reader(failas)
next(csv_reader) # praleidziam pirma eilute
for eilute in csv_reader:
    print(failas)


with open('autoparkas.csv',encoding='utf8') as failas:
    csv_reader = reader(failas,delimiter=',')
    listas = list(csv_reader)
    # for eilute in csv_reader:
    #     print(eilute)

for eilute in listas:
    print(eilute)

from csv import reader, DictReader, writer

with open('atsakymai.csv','w',newline='') as failas1:
    csv_writer = writer(failas1)
    for eilute in listas:
        csv_writer.writerow([eilute[1],eilute[2]])


import datetime as dt
with open('autoparkas.csv',encoding='utf8') as failas:
    csv_reader = reader(failas,delimiter=',')
    next(csv_reader)
    with open('atsakymai.csv','w',newline='') as failas1:
        csv_writer = writer(failas1)
        for eilute in csv_reader:
            csv_writer.writerow([eilute[1].upper(),dt.datetime.now().year - int(eilute[3])])


import datetime as dt
with open('autoparkas.csv',encoding='utf8') as failas:
    csv_reader = reader(failas,delimiter=',')
    next(csv_reader)
    with open('atsakymai.csv','w',newline='') as failas1:
        csv_writer = writer(failas1)
        csv_writer.writerow(['Gamintojas','Amzius'])
        for eilute in csv_reader:
            csv_writer.writerow([eilute[1].upper(),dt.datetime.now().year - int(eilute[3])])


# from csv import reader
#
# with open('./autoparkas.csv', encoding='utf8') as failas3:
#     csv_reader = reader(failas3, delimiter=';')
#     for eilute in csv_reader:
#         print(eilute)
#
# from csv import DictReader
# with open('./autoparkas.csv', encoding='utf8') as failas4:
#     csv_reader = DictReader(failas4, delimiter=';')
#     for eilute in csv_reader:
#         print(eilute)