define tm = Character("refChar", color="c8ffc8")
image bg background = "bg_background.jpg"
image refChar var_one= "var_one.jpeg"
image refChar var_two= "var_two.jpg"

label start:

    default numbers = ["one","two","tree","four","five","six"]
    $ boolean = False
    define total = 0
    scene bg room

    menu:
        "display characters":
            jump option_one_label
        "jump to screen tests":
            jump option_two_label
        "More options: if":
            jump option_tree_label

    label option_one_label:
    "Option two was chosen"
    scene bg background
    show refChar var_two
    tm "Line of the test male"
    show refChar var_one
    jump ending

    label option_two_label:
    #screens stored in the custom screens.rpy
    menu:
        "vbox_screen_param":
            jump vbox_screen_param_label
        "hbox_screen_param":
            jump hbox_screen_param_label
        "hbox_screen_param_with_default":
            jump hbox_screen_param_with_default_label
        "grid_screen_param":
            jump grid_screen_param_label
        "combo_screen":
            jump combo_screen_label

    label vbox_screen_param_label:
    show screen vbox_screen_param(numbers)
    pause
    hide screen vbox_screen_param
    pause
    jump ending

    label hbox_screen_param_label:
    show screen hbox_screen_param(numbers)
    pause
    hide screen hbox_screen_param
    jump ending

    label hbox_screen_param_with_default_label:
    show screen hbox_screen_param_with_default
    pause
    hide screen hbox_screen_param_with_default
    jump ending

    label grid_screen_param_label:
    show screen grid_screen_param(numbers)
    pause
    jump ending

    label combo_screen_label:
    show screen combo_screen
    pause
    jump ending

    label option_tree_label:
    menu:
        "Set boolean true":
            $ boolean = True
            jump check_boolean_label
        "Set boolean false":
            $ boolean = False
            jump check_boolean_label

    label check_boolean_label:
    menu:
        "Check boolean value":
            jump boolean_label
        "Finish boolean testing":
            jump ending

    label boolean_label:
    if boolean:
        "boolean is true"
        jump option_tree_label
    else:
        "boolean is false"
        jump option_tree_label


    label ending:
    menu:
        "Go to the begin of the scene":
            jump start
        "End the game":
            "Ending the game"
    return
