""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""


class Saldytuvas:
    def __init__(self):
        self.turinys = {}

    def prideti_produktus(self, produktai):
        for produktas, kiekis in produktai.items():
            if produktas in self.turinys:
                self.turinys[produktas] += kiekis
            else:
                self.turinys[produktas] = kiekis

    def isimti_produktus(self, produktai):
        for produktas, kiekis in produktai.items():
            if produktas in self.turinys:
                self.turinys[produktas] -= kiekis
                if self.turinys[produktas] <= 0:
                    del self.turinys[produktas]
            else:
                print(f"{produktas} neegzistuoja šaldytuve.")

    def tikrinti_kieki(self, produktas, reikalingas_kiekis):
        if produktas in self.turinys and self.turinys[produktas] >= reikalingas_kiekis:
            return True
        else:
            return False

    def spausdinti_turini(self):
        print("Šaldytuvo turinys:")
        for produktas, kiekis in self.turinys.items():
            print(f"{produktas}: {kiekis}")

def patikrinti_recepta(saldytuvas, receptas):
    recepto_produktai = dict(item.split(':') for item in receptas.split(', '))
    truksta_produktu = {}

    for produktas, reikalingas_kiekis in recepto_produktai.items():
        reikalingas_kiekis = float(reikalingas_kiekis)
        if not saldytuvas.tikrinti_kieki(produktas, reikalingas_kiekis):
            truksta_produktu[produktas] = reikalingas_kiekis - saldytuvas.turinys.get(produktas, 0)

    if not truksta_produktu:
        print("Receptas išeina!")
    else:
        print("Receptas neišeina. Trūksta šių produktų:")
        for produktas, trukstamas_kiekis in truksta_produktu.items():
            print(f"{produktas}: {trukstamas_kiekis}")

# Sukuriamas šaldytuvas
saldytuvas = Saldytuvas()

# Pridedami produktai į šaldytuvą
saldytuvas.prideti_produktus({"Pienas": 2, "Kiaušiniai": 6, "Pomidoras": 4})

# Išspausdinamas šaldytuvo turinys
saldytuvas.spausdinti_turini()

# Pridedami papildomi produktai
saldytuvas.prideti_produktus({"Kiaušiniai": 4, "Sūris": 0.5, "Duona": 1})

# Išspausdinamas šaldytuvo turinys
saldytuvas.spausdinti_turini()

# Išimami produktai iš šaldytuvo
saldytuvas.isimti_produktus({"Pienas": 1, "Pomidoras": 2, "Sviestas": 0.2})

# Išspausdinamas šaldytuvo turinys
saldytuvas.spausdinti_turini()

# Patikrinamas receptas
receptas = "Sūris: 0.3, Pomidoras: 2, Duona: 0.5"
patikrinti_recepta(saldytuvas, receptas)
