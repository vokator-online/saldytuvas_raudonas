def main():
    album_info = {
        'Artist': 'Rammstein',
        'Album': 'Made In Germany 1995-2011',
        'Label': 'Universal Music Group – 0602527864273',
        'Format': ['2 x CD', 'Compilation', 'Reissue', 'Remastered', 'Kruspe Cover'],
        'Country': 'Europe',
        'Released': '2011',
        'Genre': ['Electronic', 'Rock'],
        'Style': 'Industrial'
        }
    
    while True:
        print('''\n\n
    --- Choose what you want to do with your CD ---
                
                1 = Add a new CD to collection.
                2 = Remove CD from collection.
                3 = View my collection.
                4 = Leave the system.
              \n\n''')
        choice = input("Select the menu item you want: ")
        if choice == "4":
            break
        elif choice == "1":
            artist = input("Artist: ")
            title = input('Title: ')
            add_album(artist, title)
        elif choice == "2":
            artist = input("Artist: ")
            title = input('Title: ')
            remove_album(artist, title)
        elif choice == "3":
            list_albums()
        else:
            print("Bad choice, try again!")

    for key, value in album_info.items():
        printable_key = key + ":"
        if type(value) == list:
            value = ', '.join(value)
        print(f"{printable_key:10} {value}")

main()