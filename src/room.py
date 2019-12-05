# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''
    Room class stores name, description, and direction
    '''
    def __init__(self, name, description, *item_list):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = []
        if len(item_list) > 0:
            for item in item_list:
                self.list.append(item)

    def add_item(self, item):
        self.list.append(item)

    def delete_item(self, item):
        self.list.remove(item)

    def item_locate(self, item_name):
        for item in self.list:
            if item.name.lower() == item_name.lower():
                return item
            else:
                return None

    def items_avail(self):
        if self.list == []:
            print("You look around and see no items here.\n")
        else:
            for item in self.list:
                print(f"You look around and find: {item.name}\n")

    def __str__(self):
        return f"{self.name} >> {self.description}\n"