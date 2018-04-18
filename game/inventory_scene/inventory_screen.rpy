style inventory_label:
    xalign 0.2

style slot:
    background Frame("square", 0, 0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

screen inventory_screen:
    style_prefix "inventory"

    add "white"
    hbox:
    #character details
        vbox:
            xmaximum 300
            spacing 2
            label "Character Details" xalign 0.5
            label "Level: [pc.level]"
            label "HP: [pc.hp] / [pc.max_hp]"
            label "MP: [pc.mp] / [pc.max_mp]"
            label "Attack: [pc.attack]"
            label "Defense: [pc.defense]"

            frame:
                style "slot"
                if pc.weapon != None:
                    add pc.weapon.img
                else:
                    label "weapon" xalign 0.5 yalign 0.5 text_size 15

            frame:
                style "slot"
                if pc.armor["head"] != None:
                    add pc.armor["head"].img
                else:
                    label "head" xalign 0.5 yalign 0.5 text_size 15
            frame:
                style "slot"
                if pc.armor["chest"] != None:
                    add pc.armor["chest"].img
                else:
                    label "chest" xalign 0.5 yalign 0.5 text_size 15

    #inventory grid
        grid 10 7:
            yalign 0.2
            spaceing 5
            for item in inventory:
                frame:
                    style "slot"
                    imagebutton idle item.img action SetVariable("selected_item", item)
            for i in range(len(inventory), 70):
                frame:
                    style "slot"

    #item details
    vbox:
        spaceing 10
        label "Current Item" xalign 0.5

        if selected_item != None:
            frame :
                style "slot"
                if isinstance(selected_item, KeyItem):
                    add "bg_keyitem"
                add selected_item.img

                label "value: [selected_item.value]"

                if isinstance(selected_item, Consumable):
                    textbutton "Use" action Function(selected_item.use, pc )
                if isinstance(selected_item, Equipable):
                    if selected_item.is_equipped:
                        textbutton "unequip" action Function(selected_item.unequip)
                    else
                        textbutton "equip" action Function(selected_item.equip, pc)
                if not isinstance(selected_item, KeyItem):
                    textbutton "Discard" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None)]































    textbutton "Return":
        action Return()
        xalign 05
        yalign 0.95
