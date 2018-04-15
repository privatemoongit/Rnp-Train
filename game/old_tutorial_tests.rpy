label old_tutorial_label:
define tm = Character("refChar", color="c8ffc8")
image bg background = "trn_mgs/bg_background.jpg"
image refChar var_one= "trn_mgs/var_one.jpeg"
image refChar var_two= "trn_mgs/var_two.jpg"
default numbers = ["one","two","tree","four","five","six"]
$ boolean = False
define total = 0

jump interactive_screen_label

jump prolog_scene

pause

label option_one_label:
"Option two was chosen"
scene bg background
show refChar var_two
tm "Line of the test male"
show refChar var_one
jump ending

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
hide screen combo_screen
jump ending

label basic_screen_label:
show screen basic_screen
pause
hide screen basic_screen
jump ending

label not_to_do_screen_label:
show screen not_to_do_screen
pause
hide screen not_to_do_screen
jump ending

label boolean_label:
if boolean:
    "boolean is true"
    jump option_tree_label
else:
    "boolean is false"
    jump option_tree_label

"Ending incoming after click"
