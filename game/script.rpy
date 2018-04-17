    #jump old_tutorial_label
    #scene bg green
    #label map_label:
    #show screen map_screen
    #pause
    #jump map_label
    #pause

# The game starts here.


#"This is an imagemap tutorial."
#jump solar_system
default a = 0
label start:
scene bg green
call screen bars
"scene finished"
hide screen bars
"befor jump"
jump prolog_scene
"Placeholder for end and a pause"
label finito:
return
