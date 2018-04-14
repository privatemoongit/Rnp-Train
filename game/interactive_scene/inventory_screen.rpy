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
            #label "Level: [pc.Level]"
            label "HP: [pc.hp] / [pc.max_hp]"
            label "MP: [pc.mp] / [pc.max_mp]"
            label "Attack: [pc.attack]"
            label "Defense: [pc.defense]"


    #inventory grid

    #item details

    textbutton "Return":
        action Return()
        xalign 05
        yalign 0.95