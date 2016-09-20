from random import randrange

import display
import world

from objects.Player import attack
from objects.Loot import money
from objects import world_object
from objects import obj_maker

def update(this, delta_time):
    # Move
    if randrange(0, this.attributes["mov_spd"]) < delta_time:
        newX = this.X + randrange(-1, 2)
        newY = this.Y + randrange(-1, 2)
        # If the new tile is in bounds and walkable on... Note: Can't walk on the very edge of the world
        
        if (newX > 0) and (newX < world.WORLD_X - 1) and (newY > 0) and (newY < world.WORLD_Y - 1) and (world.map[newX][newY][3]):
            this.X = newX
            this.Y = newY
    # Attack
    if randrange(0, this.attributes["atk_spd"]) < delta_time:
        newX = randrange(0, 2) * 2 - 1 # This makes it so that it has an X velocity
        newY = randrange(0, 2) * 2 - 1 # Also a Y velocity guarenteed
        if randrange(0, 2): # Possibly give a zero velocity
            if randrange(0, 2): # Zero X velocity
                newX = 0
            else:
                newY = 0 # Zero Y.
        # Add the projectile
        world.objects.append(obj_maker.make(attack, this.X + newX, this.Y + newY, \
                {"movex" : newX, "movey": newY, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
    eff_del_list = []
    for eff in this.attributes["effects"]:
        this.attributes["effects"][eff][0](this, delta_time)       # Tick code
        this.attributes["effects"][eff][2] -= delta_time           # Lower time
        if this.attributes["effects"][eff][2] <= 0:                # Remove effect
            eff_del_list.append(eff)
    for to_del in eff_del_list:
        this.attributes["effects"][to_del][1](this)
        del this.attributes["effects"][to_del]
    del eff_del_list
    if this.attributes["HP"] <= 0:
        world.to_del.append(this)
        world.objects.append(world_object.world_object(money.money_update, money.money_collide, money.money_char, money.money_color, money.money_type, this.X, this.Y, {"value": this.attributes["money"]}))
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give experience

def collide(this, obj):
    if obj.type == "player":
        obj.attributes["HP"] -= this.attributes["damage"]
        this.X += 1


def color(this):
    return display.CYAN

def char(this):
    return 'S'

type = "enemy"

attributes = {          \
    "HP" : 50.0,        \
    "effects" : {},     \
    "mov_spd" : 300,    \
    "atk_spd" : 400,    \
    "range" : 5,        \
    "damage" : 10,      \
    "EXP" : 3,          \
    "money" : 10        \
  }