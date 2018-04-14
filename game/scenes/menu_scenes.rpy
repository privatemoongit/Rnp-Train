label prolog_scene:
     menu:
        "display characters":
            jump option_one_label
        "More options: if":
            jump option_tree_label
        "jump to screen tests":
            jump option_two_label
        "jump to screen_ tests and concept":
            jump option_screens_concepts_label

label option_two_label:
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


label option_screens_concepts_label:
    menu:
        "Basic concept":
            jump basic_screen_label
        "Basic not to do":
            jump not_to_do_screen_label
            
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

label ending:
    menu:
        "Go to the begin of the scene":
            jump start
        "End the game":
            jump finito