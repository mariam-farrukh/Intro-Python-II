# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_item_in(self, item):
        self.inventory.append(item)
        print(f"Added {item.name} to inventory")

    def remove_item_in(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                print(f"You dropped {item.name}")
                return item
            else:
                return None

    def list_inventory(self):
        if self.inventory == []:
            print("Inventory: Empty")
        else:
            inventory = ", ".join([item.name for item in self.inventory])
            print(f"Inventory: {inventory}")

    def item_locate(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
            else:
                return None

    def player_move(self, direction):
        str = f"{direction}_to"
        new_room = getattr(self.current_room, str)
        if new_room:
            self.current_room = new_room
        else:
            print("You tried to move, but nothing happened. Try a different direction")