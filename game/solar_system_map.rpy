default earth_destroyed = False

screen planets: #Preparing the imagemap
    imagemap:
        ground "/interactive_screen_componenets/planet_map.jpg"
        hover "/interactive_screen_componenets/planet_map_hover.png"

        hotspot (62, 399, 90, 91) clicked Jump("mercury")
        hotspot (227, 302, 141, 137) clicked Jump("venus")
        if not earth_destroyed:
            hotspot (405, 218, 164, 118) clicked Jump("earth")
        hotspot (591, 78, 123, 111) clicked Jump("mars")

label solar_system:
call screen planets #Displaying the imagemap

label mercury:
    "It is Mercury."
    jump solar_system

label venus:
    "It is Venus."
    jump solar_system

label earth:
    "It is Earth."
    "As soon as you quit it, it is destroyed!"
    $ earth_destroyed = True
    jump solar_system

label mars:
    "It is Mars."
    jump solar_system
