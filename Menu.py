from rw import album
import os
import rw

album = rw.album
chosenList = [ 2, 3, 4, 5]
def clear():           #log clear
    os.system('cls' if os.name=='nt' else 'clear')


def fomenu(album):    #fomenu
    print("(1) View all imported albums.")
    print("(2) Listings")
    print("(3) Full report")
    print("(4) Exit")
    choice = input("Kérlek add meg mit szeretnél csinálni: ")
    clear()
    almenu(choice,album)
def almenu(choice,album):            #fomenu utan, indítja a választott def-et
    # első almenü (view all)
    if choice == 1:
        printer(album,chosenList)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    

def printer(album,chosenList):    #printel, pont anzokat a sorokat amiket bekérünk
    print("___________________________________________________________________________")
    for i in chosenList:
        print(f"| {album[i].artist_name.center()} | {album[i].album_name.center()} | {album[i].release_year.center()} | {album[i].genre.center()} | {album[i].lenght.center()}")
        print("___________________________________________________________________________")


printer(album,chosenList)