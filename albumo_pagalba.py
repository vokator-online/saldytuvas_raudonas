def main():
    while True:
        print('''
              ----Choose what you want to do with your CD----
                0 = Exit.
                1 = Add new album entry.
                2 = Remove an album entry.
                3 = Prints all album entries.
                4 = View album details.
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
            add_album(artist, title, track, track_number, duration)
        elif choice == "2":
            artist = input("Artist:")
            title = input('Title:')
            remove_album(artist, title)
        elif choice == "3":
            list_albums()
        elif choice == "4":
            view_album_details()
        else:
            print("Bad choice, try again")

albums = []

def add_album(artist, title, track, track_number, duration):
    album = {'artist': artist, 'title': title, 'tracks': [{'track': track, 'track_number': track_number, 'duration': duration}]}
    albums.append(album)
    print(f"Album {title} by {artist} {track} {track_number} and {duration} added.")

def remove_album(artist, title):
    for album in albums:
        if album['artist'] == artist and album['title'] == title:
            albums.remove(album)
            print(f"Album {title} by {artist} removed.")
            return
    print(f"Album {title} by {artist} not found.")

def list_albums():
    print('Albums in the collection:')
    for index, album in enumerate(albums, start=1):
        print(f'{index}. {album["title"]} by {album["artist"]}')

def view_album_details():
    if not albums:
        print("No albums available.")
        return

    index = int(input("Enter the index of the album to view details: "))
    if 1 <= index <= len(albums):
        album = albums[index - 1]
        print(f"Album details:")
        print(f"Artist: {album['artist']}")
        print(f"Title: {album['title']}")
        print(f"Number of tracks: {len(album['tracks'])}")
        total_duration_seconds = sum(
            convert_duration(track['duration']) for track in album['tracks']
        )
        print(f"Total duration of tracks: {total_duration_seconds // 60} min. {total_duration_seconds % 60} sec.")
        print("Tracks:")
        for track in album['tracks']:
            print(f"{track['track_number']}. {track['track']} - {track['duration']}")
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

