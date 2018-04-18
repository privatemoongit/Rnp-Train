init python:
    class Player:
        def __init__(self, hp, mp, attack, defense, mdef, level=1):
            self.hp = hp
            self.max_hp = hp
            self.mp = mp
            self.max_mp = mp
            self.attack = attack
            self.defense = defense
            self.mdef = mdef
            self.level = level
            self.weapon = None
            self.armor = {"head": None, "chest": None, "acc": None, "shield": None}

        def addHP(self, ammount):
            self.hp += ammount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

        def addMP(self, ammount):
            self.mp += ammount
            if self.mp > self.max_mp:
                self.mp = self.max_mp

        def equip_weapon(self, weapon):
            if self.weapon != None:
                self.unequip_weapon()

            self.weapon = weapon
            self.attack += weapon.attack

        def unequip_weapon(self, weapon):
            if self.weapon != None:
                self.attack -= weapon.attack
                self.weapon = None

        def equip_armour(self, armour, slot):
            if self.armour[slot] != None:
                self.unequip_armour(slot)

            self.armour[slot] = armour
            self.defense += armour.defense
            self.mdef += armour.mdef

        def unequip_armour(self, armour, slot):
            if self.armour[slot] != None:
                self.defense -= armour[slot].defense
                self.mdef -= armour[slot].mdef
                self.armour[slot] = None
