def main():
    while True:
        print('''
              ----Choose what you want to do with your CD----
                0 = Exit.
                1 = Add new album entry.
                2 = Remove an album entry.
                3 = Prints all album entries.
              ''')
        choice = input("Your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            artist = input("Artist:")
            title = input('Title:')
            add_album(artist, title)
        elif choice == "2":
            artist = input("Artist:")
            title = input('Title:')
            remove_album(artist, title)
        elif choice == "3":
            list_albums()
        else:
            print("Bad choice, try again")



def add_album(artist, title):
    album = {'artist': artist, 'title': title }
    albums.append(album)
    print(f"Album {title} by {artist} added.")

def remove_album(artist, title):
    album = 
    