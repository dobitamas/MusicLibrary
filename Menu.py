from rw import album
import os
import rw


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


album = rw.album
def fomenu(album):
    print("(1) View all imported albums.")
    print("(2) Listings")
    print("(3) Full report")
    print("(4) Exit")
    choice = input("Kérlek add meg mit szeretnél csinálni: ")
    clear()
    almenu(choice,album)
def almenu(choice,album):
    # első almenü (view all)
    
    print("__________________________________________________________________________")
    for elem in range(len(album)):
        print("| {} | {} | {} | {} | {} |".format(album[elem].artist_name,album[elem].album_name,album[elem].release_year,album[elem].genre, album[elem].lenght))
        print("__________________________________________________________________________")
fomenu(album)
