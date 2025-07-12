print('pirmas', end=' ir ')
print('antras')
print()
print('pirmas', 'antras', 'trecias', sep=' ir ')

tekstas = '2'
skaicius = 2
skaicius_su_kableliu = 2.9

tekstas_kaip_skaicius_su_kableliu = float(tekstas)
print(tekstas_kaip_skaicius_su_kableliu, type(tekstas_kaip_skaicius_su_kableliu))
print('==========================================================')
tekstas_kaip_sveikas_skaicius = int(tekstas)
print(tekstas_kaip_sveikas_skaicius, type(tekstas_kaip_sveikas_skaicius))

print('==========================================================')
skaicius_i_teksta = str(skaicius)
skaicius_su_kableliu_i_teksta = str(skaicius_su_kableliu)
print(skaicius_i_teksta, type(skaicius_i_teksta))
print(skaicius_su_kableliu_i_teksta, type(skaicius_su_kableliu_i_teksta))
print('==========================================================')
skaicius_i_skaiciu_su_kableliu = float(skaicius)
skaicius_su_kableliu_i_skaiciu = int(skaicius_su_kableliu)
print(skaicius_i_skaiciu_su_kableliu, type(skaicius_i_skaiciu_su_kableliu))
print(skaicius_su_kableliu_i_skaiciu, type(skaicius_su_kableliu_i_skaiciu))

print('==========================================================')
print()
print('===============')
vardas = 'Aurelija'
amzius = 28
kodel_programuoti = '\nNoriu praplesti savo galimybes ir ismokti kazka naujo'
print('Mano vardas', vardas, 'man', amzius, 'metai', kodel_programuoti)
print()
print('=============================')
eilerastis = 'Mano batai buvo du\nVienas dingo nerandu'
eiler = '\nAs su vienu batuku\nNiekur eiti negaliu'
eiler += '\nDvi rankytes iesko bato'
print(eilerastis + eiler)
print()
print('============')
kvadratas = '***'
kvadratas += '\n* *'
kvadratas += '\n***'
print(kvadratas)
print()
print('======================')
pavadinimas = 'Kate'
metai = 6
kailio_spalva = 'pilka'
svoris = '5 kg'

print(f'Gyvunas {pavadinimas} ({metai}m.) turi {kailio_spalva} kailio spalva ir sveria {svoris}')
print()
print('=================')
numeris = 14
numeris_kitas_var = '14'
print(numeris, numeris, numeris, numeris, numeris)
print(numeris_kitas_var * 5)
print()
print('=========================')
trikampis = '*'
trikampis += '\n**'
trikampis += '\n***'
print(trikampis)
print()
print('=====================')
print('Mano vardas', vardas,'\nAs turiu', pavadinimas,'\nmokausi programuoti, nes', kodel_programuoti)
print()
print('==========================')
print()
print('-------------------')
print('| Vardas | Amzius |')
print('-------------------')
print('| Tomas  | 24     |\n| Jonas  | 26     |\n| Juste  | 25     |')
print('-------------------')
