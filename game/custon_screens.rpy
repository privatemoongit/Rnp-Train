#styles stored in custom_style.rpy
screen hbox_screen:
    hbox:
        style "centered_style"
        textbutton "One"
        textbutton "Two"

screen hbox_screen_param(buttons):
    hbox:
        style "centered_style"
        for button in buttons:
            textbutton button

screen hbox_screen_param_with_default(buttons=["DefaultValue"]):
    hbox:
        style "centered_style"
        for button in buttons:
            textbutton button
