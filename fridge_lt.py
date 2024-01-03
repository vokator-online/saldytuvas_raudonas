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


def main():
    saldytuvas = Saldytuvas()

    while True:
        print("\nPasirinkimai:")
        print("1. Pridėti produktą į šaldytuvą")
        print("2. Išimti produktą iš šaldytuvo")
        print("3. Patikrinti produkto kiekį šaldytuve")
        print("4. Spausdinti šaldytuvo turinį")
        print("5. Patikrinti receptą")
        print("6. Baigti programą")

        choice = input("Įveskite pasirinkimo numerį: ")

        if choice == '1':
            insert_item(saldytuvas)
        elif choice == '2':
            remove_item(saldytuvas)
        elif choice == '3':
            search_item(saldytuvas)
        elif choice == '4':
            print_items(saldytuvas)
        elif choice == '5':
            check_recipe(saldytuvas)
        elif choice == '6':
            break
        else:
            print("Netinkamas pasirinkimas. Bandykite dar kartą.")


def insert_item(saldytuvas):
    produktai = {}
    produktas = input("Įveskite produkto pavadinimą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))
    produktai[produktas] = kiekis
    saldytuvas.prideti_produktus(produktai)
    print(f"{produktas} pridėtas prie šaldytuvo.")


def remove_item(saldytuvas):
    produktai = {}
    produktas = input("Įveskite produkto pavadinimą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))
    produktai[produktas] = kiekis
    saldytuvas.isimti_produktus(produktai)
    print(f"{produktas} išimtas iš šaldytuvo.")


def search_item(saldytuvas):
    produktas = input("Įveskite produkto pavadinimą: ")
    kiekis = float(input("Įveskite reikiamą produkto kiekį: "))
    if saldytuvas.tikrinti_kieki(produktas, kiekis):
        print(f"{produktas} kiekis šaldytuve užtenka.")
    else:
        print(f"{produktas} kiekio šaldytuve nepakanka.")


def print_items(saldytuvas):
    saldytuvas.spausdinti_turini()


def check_recipe(saldytuvas):
    receptas = input("Įveskite receptą (pavyzdys: Sūris: 0.5, Pomidoras: 2, Duona: 0.4): ")
    patikrinti_recepta(saldytuvas, receptas)


if __name__ == "__main__":
    main()
