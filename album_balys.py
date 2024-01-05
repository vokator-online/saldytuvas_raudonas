def main():
    album = {
        "Artist":"Snoop Dogg",
        "Album name":"Doggystyle",
        "Year": 1993,
        "Tracks": []
        }
    while True:
        print('''
              ---- Main Album Menu XD ----
                exit = Exit.
                edit album = Album edit menu.
                edit tracklist = Add new album track.
                print a = Prints Album info.
                print b = Prints Tracklist info.
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            break
        elif choice.startswith("edit album"):
            edit_album(album)
        elif choice.startswith("edit tracklist"):
            edit_tracklist(album)
        elif choice.startswith("print"):
            print_album(album)
        else:
            print("Bad choice, try again")


def print_album(album):
    for key, value in album.items():
        print(f"{key} - {value}")


def print_tracklist(album):
    for index, value in enumerate(album["Tracks"]):
        print(f"{index}: {value}")


def edit_album(album):
    while True:
        print("""
            ----Album edit menu----
            1. Edit artist name.
            2. Edit album name.
            3. Edit album year.
            4. Tracklist edit menu.
            0. Back
            """)
        choice = input("Your choice")
        if choice.startswith("0"):
            break
        elif choice.startswith("1"):
            new_artist_name = input("Input new artist name")
            album["Artist"] = new_artist_name
        elif choice.startswith("2"):
            new_album_name = input("Input new album name")
            album["Album name"] = new_album_name
        elif choice.startswith("3"):
            new_album_year = input("Input new album year")
            album["Year"] = new_album_year
        elif choice.startswith("4"):
            edit_tracklist(album)
        else:
            print("Wrong choice")

def edit_tracklist(album):
    while True:
        print("""
            ----Tracklist edit menu----
            1. Edit track name.
            2. Edit track duration.
            3. Add new track.
            4. Album edit menu.
            0. Back
            """)
        print("Current album info:")
        print_tracklist(album)
        choice = input("Your choice")
        if choice.startswith("0"):
            break
        elif choice.startswith("1"):
            new_track_name = input("Input new track name")
            album["Tracks"] = new_track_name
        elif choice.startswith("2"):
            new_track_duration_s = input("Input new duration seconds")
            album["Album name"] = new_track_duration_s
        elif choice.startswith("4"):
            edit_album(album)
        else:
            print("Wrong choice")


if __name__ == "__main__":
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
