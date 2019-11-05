from rw import album
import os
import rw

album = rw.album

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
        printer(album,music1)
    elif choice == 2:
        # def
    elif choice == 3:
        #def
    elif choice == 4:
        #exit()
    

def printer(album,chosenlist):    #printel, pont annyi sort amennyit éppen bekérünk
    print("___________________________________________________________________________")
    for i in chosenList:
        print(f"| {album[i].artist_name} | {album[i].album_name} | {album[i].release_year} | {album[i].genre} | {album[i].lenght}")
        print("___________________________________________________________________________")


