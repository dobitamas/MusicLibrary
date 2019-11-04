import csv
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.
import operator
import collections
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    sorted(inventory)
    for item in inventory:
        print("{}: {}".format(item, inventory[item]))

display_inventory(inventory)

added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def add_to_inventory(inventory, added_items):
    for loot in added_items:
        if loot in inventory:
            inventory[loot] += 1
        else:
            inventory[loot] = 1

    return inventory

    print(inventory)

add_to_inventory(inventory, added_items)
print(inventory)

def import_inventory(inventory, filename="import_inventory.csv"):

    try:
        with open(filename) as f:
            for row in f:
                added_items = row.split(',')
                add_to_inventory(inventory, added_items)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def print_table(inventory, order=None):
    if(order == "count,desc"):
        inventory_list = sorted(inventory, key=inventory.__getitem__, reverse=True)
    elif(order == "count,asc"):
        inventory_list = sorted(inventory, key=inventory.__getitem__)
    else:
        inventory_list = inventory
    maxlen = 7
    for x in inventory_list:
        if len(x) > maxlen:
            maxlen = len(x)
    print((maxlen+10)*"-")
    print("item name".center(maxlen), "|", "count")
    print((maxlen+10)*"-")
    for x in inventory_list:
        print(x.rjust(maxlen+2, ' '), end="")
        print(" |", str(inventory.get(x)).rjust(5, ' '))
    print((maxlen+10)*"-")


print_table(inventory, order= "count,asc")








def export_inventory(inventory, filename="export_inventory.csv"):

    exportedInventory = []
    for item, number in inventory.items():
        for i in range(number):
            exportedInventory.append(item)
    exportedWithComma = ','.join(exportedInventory)

    try:
        with open(filename,'w') as f:
            f.write(exportedWithComma)
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")







