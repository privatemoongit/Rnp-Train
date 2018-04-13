default variable = 0
default hovered = False
screen basic_screen:
    add "#000"
    hbox:
        style "centered_style"
        text "[variable]"
        text "[hovered]"
        textbutton "Increment variable" :
            action SetVariable("variable", variable + 1)
            hovered SetVariable("hovered", True)
            unhovered SetVariable("hovered", False)
            xalign 0.5
            yalign 0.5

screen not_to_do_screen:
    add "#000"
    $variable += 1
    text "[variable]"
