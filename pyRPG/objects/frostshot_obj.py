import display
import world
from effects import frozen
from objects import attack
from objects import world_object
update = attack.attk_update

def collide(this, other):
     if this.attributes["owner"].type != other.type:
        if "HP" in other.attributes: # Deal damage
            other.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
            if "effects" in other.attributes:
                other.attributes["effects"]["frozen"] = [frozen.frozen, frozen.unfreeze, 1000]
                other.attributes["stuckX"] = other.X
                other.attributes["stuckY"] = other.Y

def color(this):
    return display.CYAN

def char(this):
    return 'o'

type = 'damage'