def main():
    while True:
        print('''\n\n
    --- Choose what you want to do with your CD ---
                0 = Leave the system.
                1 = Add a new CD to collection.
                2 = Remove CD from collection.
                3 = View my collection.
              \n\n''')
        choice = input("Select the menu item you want: ")
        if choice == "0":
            break
        elif choice == "1":
            artist = input("Artist: ")
            title = input('Title: ')
            add_cd(artist, title)
        elif choice == "2":
            artist = input("Artist: ")
            title = input('Title: ')
            remove_album(artist, title)
        elif choice == "3":
            list_cds()
        else:
            print("Bad choice, please try again!")

albums = []

def add_cd(artist, title):
    album = {'artist': artist, 'title': title }
    albums.append(album)
    print(f"\nCD\t{artist} - {title}\tadded to collection.")

def remove_album(artist, title):
    for album in albums:
        if album['artist'] == artist and album['title'] == title:
            albums.remove(album)
            print(f"\nCD\t{artist} - {title}\tremoved from collection.")
            return
    print(f"\nCD\t{artist} - {title}\tnot found in collection.")

def list_cds():
    print('CDs in the collection:')
    for index, album in enumerate(albums, start=1):
        print(f'\n{index}. {album["artist"]} - {album["title"]}')



main()