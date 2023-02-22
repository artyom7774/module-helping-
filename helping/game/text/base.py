class Base(object):
    def __init__(self, blocks: list = []) -> None:
        self.blocks = blocks

    def add(self, block: dict) -> None:
        self.blocks.append(block)

        items = []

        for element in self.inventory:
            for i in range(len(items)):
                item = items[i]
                if item.get('name') == element.get('name'):
                    items[i] = {'name': item.get('name'),
                                'display_name': item.get('display_name'),
                                'count': item.get('count') + element.get('count')}
                    break
            else:
                items.append({'name': element.get('name'),
                              'display_name': element.get('display_name'),
                              'count': element.get('count')})

        self.inventory = items

    def get(self) -> list:
        return self.blocks
