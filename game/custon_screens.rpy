#styles stored in custom_style.rpy
screen hbox_screen:
    hbox:
        style "centered_style"
        textbutton "One"
        textbutton "Two"

screen hbox_screen_param(buttons, size_text=50):
    hbox:
        style "centered_param_style"
        for button in buttons:
            textbutton button:
                action Null
                text_size size_text

screen hbox_screen_param_with_default(buttons=["DefaultValue"], size_text=30):
    hbox:
        style "centered_style"
        for button in buttons:
            textbutton button

screen vbox_screen_param(buttons, size_text=50):
    vbox:
        style "vbox_style"
        for button in buttons:
            textbutton button:
                action Null
                text_size size_text

screen grid_screen_param(buttons=["Default_one", "Default_two"], text_size=45):
    grid 2 len(buttons)/2+1:
        style "grid_screen_param_style"
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size
        for i in range (0, len(buttons)/2 + 1)*2 - len(buttons)):
            null
