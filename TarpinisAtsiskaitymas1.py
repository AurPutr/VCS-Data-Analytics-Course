print('Apklausa taikoma kepyklos vadovui.\nPrasome atsakyti i zemiau pateiktus klausimu.'
      '\nVeliau bus atliekami skaiciavimai ir rezultatus pamatysite ekrane.')
kepalai_per_h = int(input('Iveskite kiek duonos kepalu per valanda gali pagaminti vienas Jusu darbuotojas: '))
darbuotoju_sk = int(input('Iveskite kiek darbuotoju yra Jusu kepykloje: '))
savikaina_per_kepala = float(input('Iveskite kokia yra vieno kepalo savikaina Jusu kepykloje: '))
kepalo_pardavimo_kaina = float(input('Iveskite duonos kepalo pardavimo kaina: '))
uzsakymu_sk = int(input('Iveskite koks yra vidutinis uzsakymu kiekis per diena Jusu kepykloje: '))

kepalai_per_visa_diena = (kepalai_per_h * 7.5) * darbuotoju_sk #7.5 kadangi isminusavau 0.5 pietu pertrauka
print()
print(f'Per visa darbo diena yra imanoma iskepti {kepalai_per_visa_diena} duonos kepalu')
print()
print('Visu iskeptu duonos kepalu savikaina yra: ', kepalai_per_visa_diena * savikaina_per_kepala)
print('Gautos pajamos pardavus visus, per diena uzsakytus, duonos kepalus: ', uzsakymu_sk * kepalo_pardavimo_kaina)
print('Gautas grynas pelnas pardavus, visus per diena uzsakytus, duonos kepalus yra: ',
      (uzsakymu_sk * kepalo_pardavimo_kaina) - (uzsakymu_sk * savikaina_per_kepala))
print()
if uzsakymu_sk - kepalai_per_visa_diena <= 0:
      print('Kepykla spes ivykdyti visus tos dienos pateiktus uzsakymus')
elif uzsakymu_sk - kepalai_per_visa_diena > 0:
      print(f'Kepykla visu uzsakymu ivykdyti nespes.'
            f'\n{uzsakymu_sk - kepalai_per_visa_diena} uzsakymai liks neivykdyti.')
else:
      print('Klaida uzklausoje')

nespes_pagaminti = uzsakymu_sk - (uzsakymu_sk - kepalai_per_visa_diena)
spes_pagaminti = kepalai_per_visa_diena - (kepalai_per_visa_diena - uzsakymu_sk)

if uzsakymu_sk > kepalai_per_visa_diena:
      print('Gautos pajamos skaiciuojant tik pagaminta kieki: ', nespes_pagaminti * kepalo_pardavimo_kaina)
      print('Gautas grynas pelnas skaiciuojant tik pagaminta kieki: ',
            (nespes_pagaminti * kepalo_pardavimo_kaina) - (nespes_pagaminti * savikaina_per_kepala))
elif uzsakymu_sk < kepalai_per_visa_diena:
      print('Gautos pajamos skaiciuojant tik pagaminta kieki: ', spes_pagaminti * kepalo_pardavimo_kaina)
      print('Gautas grynas pelnas skaiciuojant tik pagaminta kieki: ',
            (spes_pagaminti * kepalo_pardavimo_kaina) - (spes_pagaminti * savikaina_per_kepala))
elif uzsakymu_sk == kepalai_per_visa_diena:
      print('Gautos pajamos skaiciuojant tik pagaminta kieki: ', kepalai_per_visa_diena * kepalo_pardavimo_kaina)
      print('Gautas grynas pelnas skaiciuojant tik pagaminta kieki: ',
            (kepalai_per_visa_diena * kepalo_pardavimo_kaina) - (kepalai_per_visa_diena * savikaina_per_kepala))




