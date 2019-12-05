from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':    Room("Outside Cave Entrance",
 "North of you, the cave mount beckons", 
 Item("rock", "That rock looks heavy, but it might be a good idea to take it with you...")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", Item("sword", "You find a sword in a stone")),

    'overlook':    Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. To the west is a dark passage.""", 
Item("notepad", "There's a notepad underneath some rubble. There's some writing in it. Are they spells?")),

    'narrow':    Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", 
Item("coin", "You see something sparkle on the ground. You walk closer to it and see that it's a gold coin. The treasure must be close.")),

    'dark':    Room("Dark Passage", """You can't see. The smell of damp water and dust fill the air. Keep going west or turn around?."""),

    'waterfall':    Room("Underground Waterfall", """The trouble was worth it, you found a beautiful underground waterfall! The room seems to be sparkling. There are plent of treasures here, but not the one you came looking for.""",
Item("gems", "There are beautiful gems in here that must be worth a fortune!")),
    
    'treasure':    Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", 
Item("key", "Looks like something was left behind. You found a mysterious key, but what does it do?")),
}

# What happens when I add a second item to the room?
# If there are two items in a room and you only want the second one, you have to get the first item and then the second item, then drop the first item.
# Solution would be to make the items an

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].w_to = room['dark']
room['dark'].e_to = room['overlook']
room['dark'].w_to = room['waterfall']
room['waterfall'].e_to = room['dark']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Type Your Name: ")

player = Player(player_name, room['outside']) # This shows what room the player is currently in

print(f"Hello, {player_name}! Go look for the hidden treasure!")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    current_room = player.current_room
    print(current_room)

    direction = ["n", "s", "e", "w"]
    actions = ["get", "drop"]
    player_cmd = input("Move North (n), South (s), East (e), or West (w). Look around (l), 'get' or 'drop' an item, and check inventory (i). Quit (q) the game >> ").split(" ")
    player_action = player_cmd[0]
    if len(player_cmd) > 1:
        item_of_interest = player_cmd[1]
    if player_action in direction:
        player.player_move(player_action)
    elif player_action == "q":
        print("See you next time!\n")
        exit() # can also use break here
    elif player_action == "i":
        player.list_inventory()
    elif player_action == "l":
        current_room.items_avail()
    elif player_action in actions:
        if player_action == "get":
            item_location = current_room.item_locate(item_of_interest)
            if item_location:
                player.add_item_in(item_location)
                current_room.delete_item(item_location)
            else:
                print("Can't find this item\n")
        elif player_action == "drop":
            item_removed = player.remove_item_in(item_of_interest)
            current_room.add_item(item_removed)
    else:
        print("Invalid, please try again")
