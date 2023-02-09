#Christmas Gifts 
#Setting: The mall
#Game Summary:
#    It's a week away from Christmas and you still dont have the gifts for your family. 
#   You have to go to four different stores to retrieve four differnet items. I have given you a list of the items. Your goal is to memorize the different items and retrieve them without going back to remember them.
# Global Variables:
# num_items (starts at 0 and increase my 1 everytime you pick up the right item. You win game if it equals 4 by the end.)
#import modules
#######

########
#define functions
#######
def start():
    print("Welcome!")
    print("\nIt's a week away from christmas and you have no gifts for your family.")
    print("\n Your at the enternce of the mall and need to retrieve 4 items.")
    print("\n This is what you have to retrieve. \n   necklace \n   nike \n   spaceship lego set \n   sweater\n")
    choice = input("\n Where are you going first? \n    pandora \n    footlocker \n    legos \n    zara\n")
    if choice == "pandora":
        pandora()
    elif choice == "footlocker":
        footlocker()
    elif choice == "legos":
        legos()
    elif choice == "zara":
        zara()
    else:
        print("This is not a valid input. I assume your going to Pandora first")
        pandora()

def pandora():
    global num_items
    print("\nYou are in pandora, select the correct item")
    item = input("\n  necklace \n  earings \n  bracelet\n")
    if item == "necklace":
        num_items = num_items +1
    else:
        num_items = num_items +0
    move = input("\nWhere would you like to go? Say one of these choices:\n\tfootlocker\n\tlegos\n\tzara\n\tpandora\n")
    if move == "footlocker":
        footlocker()
    if move == "legos":
        legos()
    if move == "zara":
         zara()
    else:
        print("This is not a valid input. I assume your going to footlocker")
        footlocker()
      

def footlocker():
    print("You are in footlocker, select the correct item")
    item_2 = input("\n  addidas \n  nike \n  socks\n")
    global num_items
    if item_2 == "nike":
        num_items = num_items +1
    else:
        num_items = num_items +0
    move = input("\nWhere would you like to go? Say one of these choices:\n\tfootlocker\n\tlegos\n\tzara\n\tpandora\n")
    if move == "legos":
        legos()
    elif move == "zara":
        zara()
    else: 
        print("This is not a valid input. I assume your going to legos")
        legos()
        

def legos():
    print("You are in legos, select the correct item")
    item_3 = input("\n  spaceship lego set \n  mall lego set \n  mars lego set\n")
    global num_items
    if item_3 == "spaceship lego set":
        num_items = num_items +1
    else:
        num_items = num_items +0
    move = input("\nWhere would you like to go? Say one of these choices:\n\tfootlocker\n\tlegos\n\tzara\n\tpandora\n")
    if move == "zara":
        zara()
    else:
        print("I assume you are going to zara")
        zara()
        
def zara():
    print("You are in zara, select the correct item")
    item_4 = input("\n  dress \n  sweater \n  hat\n")
    global num_items
    if item_4 == "sweater":
        num_items = num_items +1
    else:
        num_items = num_items +0
    if num_items == 4:
        print("You did it! Congradulations!")
    else:
        print("You have failed, try again.")
   

########
#main
#######
#TODO: Add some global variables
num_items = 0
start()
