import display

class effect():
    """Base class of effects."""
    def __init__(this, owner, duration, name = None):
        this.time = duration
        this.owner = owner
        this.name = name

    def tick(this, delta_time):
        this.time -= delta_time
        if this.owner.type == "player" and this.name is not None and display.sidebar_line < 15: # Only show the first few effects.
            time_left = "Inf"
            if this.time < float("inf"):
                time_left = str(int(this.time/1000))
            display.printc(51, display.sidebar_line, this.name + '(' + time_left + ')')
            display.sidebar_line += 1

    def uneffect(this, owner):
        pass

