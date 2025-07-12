# Seaborn yra duomenų vizualizacijos biblioteka.
# Ji sukurta Matplotlib pagrindu.
# Stilistiškai kiek išbaigtesnė už Matplotlib.
# Labai gerai veikia su pandas DataFrame'ais.
# Labai plačiai naudojama duomenų analizėje.
#Dokumentaciją rasite čia - https://seaborn.pydata.org/

from numpy import block
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dažnai duomenų analizės bibliotekos turi integruotus dataset'us, demonstraciniams tikslams. Pasinaudokime vienu iš jų:
pd.set_option('display.max_rows', None)
tips = sns.load_dataset('tips')
print(tips)
print(tips.head())
print(tips.shape)
sns.set_style("dark") #Seaborn has five built-in themes to style its plots: darkgrid , whitegrid , dark , white , and ticks .
#sns.displot(tips['total_bill'])
#
#
# # parametras bins padidinti stulpelių skaičių
#sns.displot(tips['total_bill'], bins=10, kde=True)
#sns.displot(x=tips['total_bill'], y=tips['tip'])

# .jointplot()
# Matome, koks yra sąntykio tarp 'total_bill' ir 'tip' pasiskirstymas.
# Pagrindiniame lange yra sklaidos diagrama, o iš dešinės ir viršuje - tos pačios histogramos, iš kurių sukombinavome rezultatą.
#sns.jointplot(x='total_bill', y='tip', data=tips)

# Rezultatą galime koreguoti su parametru kind:
#sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

# reikšmė 'reg' stengiasi nubrėžti mums liniją, kuri atspindėtų tendenciją.
#sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')


#.scatterplot()
# parametruose nurodžius ašis ir šaltinį, nubrėžia mums sklaidos diagramą.
#sns.scatterplot(x='total_bill', y='tip', data=tips)

# Parametruose taip pat galima nurodyti hue ir size reikšmes:
#sns.scatterplot(x='tip', y='total_bill', data=tips, hue='sex', size='time')

# .pairplot()
# duoda mums visas įmanomas pasiskirstymo kombinacijas lentelėje:
#sns.pairplot(tips)
# sns.scatterplot(x='total_bill', y='size', data=tips)

# parametras hue išskiria kategorines reikšmes, o diag_kind šiuo atveju nurodo, kad įstrižainėje norime matyti ne linijas, o histogramas pvz.:

#sns.pairplot(tips, hue='sex', diag_kind='hist')

# Kategorizavimo histogramos

# .barplot() išskirsto kategorijas pagal kurį nors rodiklį ir leidžia tam rodikliui taikyti kokią nors funkciją:
#sns.barplot(x='sex', y='total_bill', data=tips) # ci=False

# Jeigu mes nenurodome, kokia ta funkcija, numatyta reikšmė yra vidurkis. 
# Taigi šiame pavyzdyje matome sąskaitos vidurkių pasiskirstymą tarp lyčių. 
# Jeigu norime nurodyti suma, turime naudoti estimator parametrą, pvz.:

#sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum)

# Šiuo atveju matome bendras sumas. 
# Taip pat panaudojome hue, tokiu būdu rezultatą išskirstydami savaitės dienomis.
#  Nekreipkite dėmesio į juodas linijas, jos yra error bars, rodo statistinį skaičiavimo patikimumą, 
# ir nėra mums aktualios. Norint jas išjungti, parametruose nurodykite ci=False

# .countplot() tiesiog suskaičiuoja kategorijas:
#sns.countplot(x='smoker', data=tips)



# Stilius ir spalvos
# .set_style()
# Seaborn leidžia nustatyti stilių su .set_style() metodu. Į parametrus reikia įkelti vieną iš šių reikšmių - darkgrid, whitegrid, dark, white, ticks.
# 
# sns.set_style('darkgrid')
# sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum)

# .despine() Nuima viršutinį ir dešinį rėmą.
# sns.set_style('whitegrid')
# sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum)
# sns.despine()

# palette parametras
# leidžia pasirinkti vieną iš paruoštų naudoti spalvų palečių. 
# Jas rasite čia. https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html#classes-of-colormaps
# Kai kurie metodai nepriima parametro palette, tuomet reikia bandyti tas pačias reikšmes nurodyti į cmap parametrą

# sns.set_style('white')
# sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum, palette='cividis')
# sns.despine()

plt.show() #block=True