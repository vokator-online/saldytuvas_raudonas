albumas = []

def prideti_albuma(atlikejas, pavadinimas):
    album = {'atlikejas': atlikejas, 'pavadinimas': pavadinimas}
    albumas.append(album)
    print(f'Albumas {pavadinimas} {atlikejas} prideti. ')

def isimti_albuma(atlikejas, pavadinimas):
    for album in albumas:
        if album['atlikejas'] == atlikejas and album['pavadinimas'] == pavadinimas:
            albumas.remove(album)
            print(f"Albumas {pavadinimas} {atlikejas} pasalintas. ")
            return
        print(f"Albumas {pavadinimas} {atlikejas} nerastas")

def sarasas():
    print('Albumai kolekcijoje: ')
    for list, album in enumerate(albumas, start=1):
        print(f'{list} {album['pavadinimas']}{album['atlikejas']}')

def main():
    while True:
        print('''
              ---Pasirink ka nori daryti---
              0 = Iseiti.
              1 == Prideti.
              2 = Istrinti.
              3 = Atspausdinti albumus.
              ''')
        pasirinkimas =input(" Jusu pasirinkimas: ")
        if pasirinkimas == "0":
            break
        elif pasirinkimas == "1":
            atlikejas = input("Atlikejas: ")
            pavadinimas = input("Pavadinimas: ")
            prideti_albuma(atlikejas, pavadinimas)
        elif pasirinkimas == "2":
            atlikejas = input("Atlikejas: ")
            pavadinimas = input("Pavadinimas: ")
            isimti_albuma(atlikejas, pavadinimas)
        elif pasirinkimas == "3":
            sarasas()
        else:
            print("Blogas pasirinkimas")

main()























""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""
