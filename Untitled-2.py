from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

player = FirstPersonController()
app = Ursina()

Ground = Entity(
    model="plane",
    color=color.white,
    scale=(100, 1, 100),
    collider="mesh"
)

def input(key):
    if key == "left mouse down":
        playerpos = player.position + player.forward * 2
        playerpos.y = 0.75
        Entity(
            model="cube",
            color=color.grey,  # replaced stone texture with grey color
            scale=(1.5, 1.5, 1.5),
            collider="box",
            position=playerpos
        )
    elif key == "escape":
        application.quit()

Sky()

def update():
    playerpos123 = player.position
    print("position:", playerpos123)

app.run()
