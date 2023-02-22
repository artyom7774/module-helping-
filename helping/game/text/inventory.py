class Inventory(object):
    def __init__(self, max_item: int = 10, inventory: list = []) -> None:
        self.max = max_item
        self.inventory = inventory

    def add(self, item) -> None:
        self.inventory.append(item)

        items = []

        for element in self.inventory:
            for i in range(len(items)):
                item = items[i]
                if item.get('name') == element.get('name'):
                    items[i] = {'name': item.get('name'),
                                'display_name': item.get('display_name'),
                                'rare': item.get('rare'),
                                'count': item.get('count') + element.get('count')}
                    break
            else:
                items.append({'name': element.get('name'),
                              'display_name': element.get('display_name'),
                              'rare': element.get('rare'),
                              'count': element.get('count')})

        self.inventory = items

    def get(self) -> list:
        return self.inventory
