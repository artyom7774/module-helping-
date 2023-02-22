import helping
import random

copper = helping.Item(name='copper', display_name='медь', rare=1).get()

copper["count"] = 2

inventory = helping.Inventory()
inventory.add(copper)

print(inventory.inventory)

copper["count"] = random.randint(1, 7)
forest = helping.Place(inventory=inventory, speed = 0.3, size=30, text="Поход в лес...", get=[copper])

inventory = forest.run()
print(inventory.inventory)
