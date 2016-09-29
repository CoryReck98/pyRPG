from random import randrange

import display
import world

from items import item
from objects.Player import attack
from objects.Loot import money
from objects import world_object
from objects import obj_maker
from spells import spell

def enemy_update(this, delta_time):
    if randrange(0, this.attributes["mov_spd"]) < delta_time:  
        newX = this.X + randrange(-1, 2)
        newY = this.Y + randrange(-1, 2)
        # If the new tile is walkable on and not out of bounds
        if (newX >= 0) and (newX < world.WORLD_X) and (newY >= 0) and (newY < world.WORLD_Y) and (world.map[newX][newY][3]):
            this.X = newX
            this.Y = newY
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
        moneydrop = this.attributes["money"] + randrange(0, this.attributes["money"])
        moneydrop += moneydrop*world.player.attributes["luck"]*.01
        moneydrop = max(1, int(moneydrop))
        world.objects.append(obj_maker.make(money, this.X, this.Y, {"value": moneydrop, "taken" : False}))
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give experience

def enemy_collide(this, obj):
    if obj.type == "player":
        obj.attributes["HP"] -= this.attributes["damage"]
        this.X += 1


def enemyColor(this):
  return display.CYAN

def enemyChar(this):
  return 'Q'

enemy_type = "enemy"

enemy_attributes =      \
    { "HP" : 10.0,      \
      "effects" : {},   \
      "mov_spd" : 350,  \
      "damage" : 5,     \
      "EXP" : 1,        \
      "money" : 3       \
    }