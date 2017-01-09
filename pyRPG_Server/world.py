import pickle


# World tile. Form of [foreground color, background color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING = [0, 1, ' ', True]     # Nothing there

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size

map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]
players = []

objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.
to_del_plr = []

move_requests = [] # Requests to move players

def out_of_bounds(x, y):
    return (y < 0) or (y >= WORLD_Y) or (x < 0) or (x >= WORLD_X)

world_name = "default"

def load(name):
    global map, objects, world_name, to_del
    try:
        with open("res/maps/" + name + ".wrld", "rb") as handle:
            map = pickle.load(handle)
            objects = pickle.load(handle)
            to_del = []
            world_name = name
    except Exception as ex:
        map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]
        objects = []
        world_name = "default"
        print("Error loading map " + name)
        print(ex)

def save_player(index):
    try:
        with open("res/saves/" + world_name + ".plr", "wb") as handle:
            pickle.dump(players[index], handle)
            pickle.dump(world_name, handle)
    except Exception as ex:
        print("Could not save player in map " + world_name)

def save(name):
    try:
        with open("res/maps/" + name + ".wrld", "wb") as handle:
            pickle.dump(map, handle)
            pickle.dump(objects, handle)
    except Exception as ex:
        print( "Could not save.")

