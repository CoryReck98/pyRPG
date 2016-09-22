import time

import display
import world

from items import item

from objects.Player import attack
from objects import world_object

from spells import fireball
from spells import first_aid
from spells import frostshot
from spells import lifesteal
from spells import spell

from items import bread

def play_attk_color(this):
    return display.BLUE

def player_update(this, delta_time):
    display.printc(8, 0, str(int(this.attributes["HP"])) + "/" + str(int(this.attributes["maxHP"])) + "  ")
    display.printc(8, 1, str(int(this.attributes["MP"])) + "/" + str(int(this.attributes["maxMP"])) + "  ")
    display.printc(10, 2, str(this.attributes["money"]) + "     ")
    display.printc(12, 3, str(this.attributes["level"]))
    display.printc(5, 4, str(int(0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4 - this.attributes["EXP"])) + " to level        ")
    if this.attributes["HP"] < this.attributes["lastHP"]:
        this.attributes["sincehit"] = 0
    else:
        this.attributes["sincehit"] += delta_time

    if display.keyDown(ord('W')) and (not "del_up" in this.attributes["effects"]):
        if (this.Y > 0) and world.map[this.X][this.Y - 1][3]:
            this.Y -= 1
        this.attributes["effects"]["del_up"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["mov_spd"]))]
    if display.keyDown(ord('S')) and (not "del_down" in this.attributes["effects"]):
        if (this.Y < world.WORLD_Y - 1) and world.map[this.X][this.Y + 1][3]:
            this.Y += 1
        this.attributes["effects"]["del_down"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["mov_spd"]))]
    if display.keyDown(ord('A')) and (not "del_left" in this.attributes["effects"]):
        if (this.X > 0) and world.map[this.X - 1][this.Y][3]:
            this.X -= 1
        this.attributes["effects"]["del_left"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["mov_spd"]))]
    if display.keyDown(ord('D')) and (not "del_right" in this.attributes["effects"]):
        if (this.X < world.WORLD_X - 1) and world.map[this.X + 1][this.Y][3]:
            this.X += 1
        this.attributes["effects"]["del_right"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["mov_spd"]))]
    if display.keyDown(ord(' ')) and this.attributes["can_cast"]:
        this.attributes["spell"].cast(this)
        this.attributes["can_cast"] = False
    if not display.keyDown(ord(' ')):
        this.attributes["can_cast"] = True
    # Attacks!
    if (display.keyDown(ord('I'))) and (this.Y != 0) and (world.map[this.X][this.Y - 1][3]) and (not "del_atk" in this.attributes["effects"]):
        world.objects.append(world_object.world_object(attack.update, attack.collide, attack.char, play_attk_color, attack.type, this.X, this.Y - 1, \
            {"movex" : 0, "movey": -1, "range" : this.attributes["weapon"].attributes["range"], "damage" : (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), "speed" : 100, "to_move" : 0, "owner" : this}\
        ))
        this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["atk_spd"]))]

    if (display.keyDown(ord('J'))) and (this.X != 0) and (world.map[this.X - 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
        world.objects.append(world_object.world_object(attack.update, attack.collide, attack.char, play_attk_color, attack.type, this.X - 1, this.Y, \
            {"movex" : -1, "movey": 0, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["strength"]*this.attributes["weapon"].attributes["damage"]//2, "speed" : 100, "to_move" : 0, "owner" : this}\
        ))
        this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["atk_spd"]))]

    if (display.keyDown(ord('K'))) and (this.Y != 19) and (world.map[this.X][this.Y + 1][3]) and (not "del_atk" in this.attributes["effects"]):
        world.objects.append(world_object.world_object(attack.update, attack.collide, attack.char, play_attk_color, attack.type, this.X, this.Y + 1, \
            {"movex" : 0, "movey": 1, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["strength"]*this.attributes["weapon"].attributes["damage"]//2, "speed" : 100, "to_move" : 0, "owner" : this}\
        ))                                                                                                                                                                  
        this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["atk_spd"]))]

    if (display.keyDown(ord('L'))) and (this.X != 49) and (world.map[this.X + 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
        world.objects.append(world_object.world_object(attack.update, attack.collide, attack.char, play_attk_color, attack.type, this.X + 1, this.Y, \
            {"movex" : 1, "movey": 0, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["strength"]*this.attributes["weapon"].attributes["damage"]//2, "speed" : 100, "to_move" : 0, "owner" : this}\
        ))
        this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, 500/(1+2.718**(.01*this.attributes["atk_spd"]))]
        # Or with our constants in python, time = 500/(1+2.718^(.01x)), which is a nice logistic formula.

    if display.keyDown(display.CONST.VK_LSHIFT) and this.attributes["can_item"]:
        this.attributes["consumable"].attributes["use"](this)
        this.attributes["can_item"] = False
        this.attributes["consumable"].amount -= 1
        if this.attributes["consumable"].amount == 0:
            this.attributes["consumable"] = item.item("Nothing", "consumable", world_object.no_func, world_object.no_func, 1, {"icon" : ["   ", "   ", "   "], "color" : 0, "use" : world_object.no_func})
            this.attributes["consumable"].draw()
    if not display.keyDown(display.CONST.VK_SHIFT):
        this.attributes["can_item"] = True

    
    eff_del_list = []
    # Update all effects.
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
        display.printc(33, 9,  "+++++++++++++", display.RED)
        display.printc(33, 10, "+ You DIED! +", display.RED)
        display.printc(33, 11, "+++++++++++++", display.RED)
        display.refresh()
        time.sleep(1)
        display.flushinp()
        key = -1
        while key == -1:
            key = display.getch()

        display.end()
    # Finally, update lastHP. Done after effects because we don't want effects to make you constantly red
    this.attributes["lastHP"] = this.attributes["HP"]

def collide(this, oth):
    if oth.type == "money":
        this.attributes["money"] += oth.attributes["value"];
        # Now to delete it
        world.to_del.append(oth)

def player_char(this):
    return 'P'

def player_color(this):
    if this.attributes["sincehit"] < 75:
        return display.RED
    elif this.attributes["sincehit"] < 150:
        return display.WHITE
    elif this.attributes["sincehit"] < 225:
        return display.RED
    return display.WHITE

player_type = "player"

def gain_exp(this, amount):
    this.attributes["EXP"] += amount
    # Takes 0.5L^2 + .5L + 4
    while this.attributes["EXP"] >= (0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4): # They levelled up!
        this.attributes["EXP"] -= (0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4) # Remove EXP required for level
        this.attributes["level"] += 1 # Duh.
        if this.attributes["level"] == 2:
            if this.attributes["class"] == "mage":
                this.attributes["items"].append(spell.spell(fireball.manaCost, fireball.fireball, fireball.name, fireball.icon, fireball.color))
            if this.attributes["class"] == "warrior":
                this.attributes["items"].append(spell.spell(first_aid.manaCost, first_aid.FirstAid, first_aid.name, first_aid.icon, first_aid.color))
            if this.attributes["class"] == "thief":
                this.attributes["items"].append(spell.spell(lifesteal.manaCost, lifesteal.lifesteal, lifesteal.name, lifesteal.icon, lifesteal.color))
        if this.attributes["level"] == 4:
            if this.attributes["class"] == "mage":
                this.attributes["items"].append(spell.spell(frostshot.manaCost, frostshot.frostshot, frostshot.name, frostshot.icon, frostshot.color))
        if this.attributes["class"] == "warrior":
            this.attributes["maxHP"] += 15 # Give stats. TODO: Give them based on class
            this.attributes["maxMP"] += 5
            this.attributes["mov_spd"] -= 1
            this.attributes["atk_spd"] -= 2
            this.attributes["magic"] += 1
            this.attributes["strength"] += 4
        if this.attributes["class"] == "mage":
            this.attributes["maxHP"] += 5 # Give stats. TODO: Give them based on class
            this.attributes["maxMP"] += 10
            this.attributes["mov_spd"] -= 2
            this.attributes["atk_spd"] -= 2
            this.attributes["magic"] += 4
            this.attributes["strength"] += 2
        if this.attributes["class"] == "thief":
            this.attributes["maxHP"] += 10  # Give stats. TODO: Give them based on class
            this.attributes["maxMP"] += 10
            this.attributes["mov_spd"] -= 4
            this.attributes["atk_spd"] -= 3
            this.attributes["magic"] += 2
            this.attributes["strength"] += 3

        this.attributes["HP"] = this.attributes["maxHP"] # HP restore on level
        this.attributes["MP"] = this.attributes["maxMP"] # MP restore on level
# effects is a dictionary of (string) effect name to [(func) tick(player, delta_time), (func) on_remove(player), time_left]
# items is a list of ITEMs or to SPELLs
player_attributes =                     \
    { "maxHP" : 100.0,                  \
      "HP" : 100.0,                     \
      "maxMP" : 50,                     \
      "MP" : 50,                        \
      "money" : 0,                      \
      "effects" : {},                   \
      "EXP" : 0,                        \
      "level" : 1,                      \
      "items" : [],                     \
      "class" : "newb",                 \
      "spell" : spell.spell(0, world_object.no_func, ["   ", "   ", "   "], display.WHITE), \
      "weapon" : item.item("", "weapon", world_object.no_func, world_object.no_func, 1, {"damage" : 1, "range" : 1}),       \
      "hat" : item.item("", "hat", world_object.no_func, world_object.no_func),             \
      "shirt" : item.item("", "shirt", world_object.no_func, world_object.no_func),         \
      "pants" : item.item("", "pants", world_object.no_func, world_object.no_func),         \
      "ring" : item.item("", "ring", world_object.no_func, world_object.no_func),           \
      "consumable" : item.item("", "consumable", world_object.no_func, world_object.no_func, 1, {"icon" : ["   ", "   ", "   "], "color" : 0, "use" : world_object.no_func}), \
      "mov_spd" : 0,                    # How quickly they move\
      "atk_spd" : 0,                    # How quickly they attack\
      "can_cast" : True,                 \
      "can_item" : True,                 \
      "magic" : 5,                      # How good spells are \
      "strength" : 5,                   # How much damage regular attacks do. \
      "luck" : 0,                       # Luck will change item and money drops\
      "gainexp" : gain_exp,              \
      "lastHP" : 100.0,                 # What was their HP last frame?\
      "sincehit" : 300                  # How long since they were hit\
    }


def set_active(type):
    options = [] # All options to go in the menu.
    items = [] # The item corresponding to the option
    for opt in world.player.attributes["items"]:
        if opt.type == type:
            if opt.type == "spell":
                options.append([opt.name + "(" + str(opt.amount) + ")", world_object.no_func])
            else:
                options.append([opt.name +"(" + str(opt.amount) + ")" + opt.attributes["disp_data"], world_object.no_func])
            items.append(opt)

    empty_lists = [[] for x in range(len(options) + 1)]
    choice = display.menu("Set to what?", empty_lists, ["Back", world_object.no_func],  *options)
    if choice == 0: # They chose back
        return

    if type != "spell": # Spells don't have equip and unequip functions.
        world.player.attributes[type].unequip(world.player.attributes[type], world.player) # Unequip the old item.
        world.player.attributes[type] = items[choice - 1] # Find the new item
        world.player.attributes[type].equip(world.player.attributes[type], world.player) # Equip new item
    else:
        world.player.attributes[type] = items[choice - 1]

    
def inventory_menu():
    while display.menu("Inventory\nMax HP: Red\nMax MP: Blue\nMovement Speed: Green\nAttack Speed: White\nMagic Power: Cyan\nStrength: Magenta\nLuck: Yellow", [[], ["consumable"], ["weapon"], ["hat"], ["shirt"], ["pants"], ["ring"]], ["Back", world_object.no_func], ["Set Consumable", set_active], ["Set Weapon", set_active], ["Set Hat", set_active], ["Set Shirt", set_active], ["Set Pants", set_active], ["Set Ring", set_active]):
        # Redraw equip names.
        display.printc(display.WEAPON_X, display.WEAPON_Y, ' ' * 33)
        display.printc(display.WEAPON_X, display.WEAPON_Y, world.player.attributes["weapon"].name[:33])
        display.printc(display.HAT_X, display.HAT_Y, ' ' * 36)
        display.printc(display.HAT_X, display.HAT_Y, world.player.attributes["hat"].name[:36])
        display.printc(display.SHIRT_X, display.SHIRT_Y, ' ' * 34)
        display.printc(display.SHIRT_X, display.SHIRT_Y, world.player.attributes["shirt"].name[:34]) 
        display.printc(display.PANTS_X, display.PANTS_Y, ' ' * 34)
        display.printc(display.PANTS_X, display.PANTS_Y, world.player.attributes["pants"].name[:34])
        display.printc(display.RING_X, display.RING_Y, ' ' * 35)
        display.printc(display.RING_X, display.RING_Y, world.player.attributes["ring"].name[:35])
 
