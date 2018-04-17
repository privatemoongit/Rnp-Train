screen bars:
    if total % 2 == 1 :
        add "trn_mgs/bg_background.jpg"
    elif total % 2 == 0:
        add "trn_mgs/bluescreen.jpg"
    bar:
        bar_vertical True
        value total
        range 10
        xysize(25,200)
        xalign 0.5
        yalign 0.5
    if total < 10:
        imagebutton auto "trn_mgs/button_%s.png":
            action Function(incrementTotal)
    else:
        imagebutton auto "trn_mgs/button_%s.png":
            action Null
