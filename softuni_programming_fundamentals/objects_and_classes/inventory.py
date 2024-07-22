class Inventory:
    items = []

    def __init__(self, __capacity: int):
        self.__capacity = __capacity

    def add_item(self, item: str):
        if self.__capacity > len(Inventory.items):
            Inventory.items.append(item)
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        capacity = self.get_capacity()
        returned_items = ", ".join(Inventory.items)
        left_capacity = self.__capacity - len(Inventory.items)
        return f"Items: {returned_items}.\nCapacity left: {left_capacity}"