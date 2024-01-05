def main():
    while True:
        print('''
              ----Choose what you want to do with your CD----
                0 = Exit.
                1 = Add new album.
                2 = Remove an album.
                3 = View album details.
              ''')
        choice = input("Your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            artist = input("Artist:")
            title = input('Title:')
            track = input('Track:')
            track_number = int(input("Track number: "))
            duration = input('Duration (minutes:seconds):')
            add_album(artist, title, track,track_number, duration)
        elif choice == "2":
            artist = input("Artist:")
            title = input('Title:')
            remove_album(artist, title)
        elif choice == "3":
            list_albums()
        else:
            print("Bad choice, try again")

albums = []

def add_album(artist, title, track, track_number, duration):
    album = {'artist': artist, 'title': title, 'track': track, 'duration': duration}
    albums.append(album)
    print(f"Album {title} by {artist} {track} {track_number} and {duration} added.")

def remove_album(artist, title, track, track_number, duration):
    for album in albums:
        if album['artist'] == artist and album['title'] == title and album['track'] == track and album['track number'] == track_number and album['dutation'] == duration:
            albums.remove(album)
            print(f"Album {title} by {artist} {track} {track_number} and {duration} removed.")
            return
    print(f"Album {title} by {artist} {track} {track_number} and {duration} not found.")

def list_albums():
    if not albums:
        print("No albums available.")
        return
    print('Albums in the collection:')
    for index, album in enumerate(albums, start=1):
        print(f'{index}. {album["title"]} by {album["artist"]} {album['track']} {album['track number']} {album['duration']}')
    index = int(input("Enter the index of the album to view details: "))
    if 1 <= index <= len(albums):
        album = albums[index -1]
        print(f"Album details:")
        print(f"Artist: {album['artist']}")
        print(f"Title: {album['title']}")
        print(f"Number of tracks: {len(album['tracks'])}")
        total_duration_seconds = sum(
            convert_duration(track['duration']) for track in album['tracks']
        )
        print(f"Total duration of tracks: {total_duration_seconds // 60} min. {total_duration_seconds % 60} sec.")
        print("Tracks:")
    else:
        print("Invalid index.")

def convert_duration(duration):
    try:
        minutes, seconds = map(int, duration.split(':'))
        return minutes * 60 + seconds
    except ValueError:
        print(f"Invalid duration format: {duration}")
        return 0


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
