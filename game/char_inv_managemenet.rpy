label ci_label:
default inventory = []
default selected_item = None
default pc = Player(7, 5, 5, 3, 2, 1)

$ sword_item = Weapon("sword", 10, 5, "sword")
$ pie_item = Consumable("pie", 50, 100, 0)
$ cauldron_item = KeyItem("cauldron")
$ shield_item = Armour("armour shield", 15, 5, 4, "shield")

$inventory.append(sword_item)
$inventory.append(shield_item)
$inventory.append(pie_item)
$inventory.append(cauldron_item)

call screen inventory_screen
