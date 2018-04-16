define j = 0
define x = 0
screen map_screen:
  modal True
  grid 16 9:
      style "centered_style"
      for j in range (0, 144):
        if j == 14:
            textbutton "[x]"
        elif j == 15:
            imagebutton auto "interactive_screen_componenets/concil_%s.jpg":
                action Return()
        elif j == 56:
            imagebutton auto "interactive_screen_componenets/printer_%s.jpg":
                action Null
        elif j == 129:
            imagebutton auto "interactive_screen_componenets/megaphone_%s.jpg":
                action Null
        else:
            textbutton "":
                action Null
