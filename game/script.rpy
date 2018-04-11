#RenpyNotes 07
define tm = Character("refChar", color="c8ffc8")
#RenpyNotes 12
image bg background = "bg_background.jpg"
#RenpyNotes 17
image refChar var_one= "var_one.jpeg"
#RenpyNotes 18
image refChar var_two= "var_two.jpg"

label start:
    #RenpyNotes 14
    scene bg background
    #RenpyNotes 24
    show refChar var_two

    #RenpyNotes 08
    tm "Line of the test male"
    #RenpyNotes 20
    show refChar var_one
    #RenpyNotes 53
    default boolean = False
    #RenpyNotes 44
    menu:
        "Option one":
            #RenpyNotes 46
            jump option_one
        "Option two":
            #RenpyNotes 48
            jump option_two
        "Option tree":
            #RenpyNotes 54
            $ boolean = True
            #RenpyNotes 50
            jump option_tree
    #RenpyNotes 32
    label option_one:
    "Chosed option one jumping to option tree"
    #RenpyNotes 50
    jump option_tree
    #RenpyNotes 32
    label option_two:
    "Option two was chosen"
    #RenpyNotes 33
    label option_tree:
    "The third option"
    #RenpyNotes 55
    if boolean:
        "boolean is true"
    else:
        "boolean is false"
    "Placeholder line befor the game ends"
    return
