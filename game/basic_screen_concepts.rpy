default variable = 0

screen basic_screen:
    add "#000"

screen not_to_do_screen:
    hbox:
        style_prefix "combo"
        $variable += 1
        text "Here is the variable [variable]"
