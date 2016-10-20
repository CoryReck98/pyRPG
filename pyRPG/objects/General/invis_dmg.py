from effects import fire
from objects import world_object

class lavatile(world_object.world_object):
    """ Does damage to whatever it collides with."""
    def __init__(this, locX, locY):
        super().__init__(locX, locY, "damage")
        this.attributes.update({"timers" : {}})

    def update(this, delta_time):
        "Decrements timers for damaging things"
        to_del = []
        for index in this.attributes["timers"]:
            this.attributes["timers"][index] -= delta_time
            if this.attributes["timers"][index] <= 0:
                to_del.append(index)
        for index in to_del:
            del this.attributes["timers"][index]
    
    # Since various sources of damage may do different effects, we need a new collide for each effect       
    def collide(this, oth):
        "Does damage to stuff."
        if not (oth in this.attributes["timers"]):
            if "HP" in oth.attributes:
                oth.attributes["HP"] -= 10              # Hurt it
                this.attributes["timers"][oth] = 100    # Give invincibility
                if "effects" in oth.attributes:
                    oth.attributes["effects"]["fire"] = [fire.fire, lambda x: 0, 1000] # Start fire damage
    
    