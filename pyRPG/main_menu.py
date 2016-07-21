import display
import world
from items import item

# Warrior equipment
from items import clothhat
from items import clothPants
from items import clothShirt
from items import okaySword
from items import UselessRingg
# Mage equipment

from objects import player
from objects import world_object
def load_game():
    pass

   
def new_game():
    # Get their save name
    display.clear()
    display.flushinp()
    inpt = display.getch()
    curs_loc = 0
    file_name = ""

    display.printc(30, 9, "Enter your name:")
    while inpt != 10: # Until ENTER pressed
        if inpt == 8: # Backspace
            if curs_loc != 0:
                curs_loc -= 1
                file_name = file_name[:-1] # Remove last character
            display.printc(curs_loc + 30, 10, ' ')
        elif inpt != -1:
            display.printc(curs_loc + 30, 10, chr(inpt))
            file_name += chr(inpt)
            curs_loc += 1
        display.refresh()
        inpt = display.getch()
    # Wait for release
    while display.keyDown(display.CONST.VK_RETURN):
        pass
    world.save_name = file_name
    # Class select!
    # What color each class should be
    color_list = [display.RED, display.BLUE, display.YELLOW]
    # What the middle text is for each class
    text_list = ["+  Warrior   +", "+    Mage    +", "+   Thief    +"]
    # The box of '+'s top and bottom
    box = '+' * 14

    # Number of rows each box takes up. 3 for the box + 2 for the space below
    box_size = 5
    # Where the boxes start display on y-axis
    box_start = 4
    # Left side of boxes
    box_left = 32
    # Clear screen and set up menu.
    display.clear()
    for i in range(len(text_list)):
        display.printc(box_left, box_start + i * box_size, box)
        display.printc(box_left, box_start + i * box_size + 1, text_list[i])
        display.printc(box_left, box_start + i * box_size + 2, box)

    # Draw first box in color
    display.printc(box_left, box_start, box, color_list[0])
    display.printc(box_left, box_start + 1, text_list[0], color_list[0])
    display.printc(box_left, box_start + 2, box, color_list[0])

    choice = 0;
    
    
    display.refresh()
    while True:
        # Check for choice down/up
        if display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
            # Redraw current box in white
            display.printc(box_left, box_start + choice * box_size, box)
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box)
            # If decrementing choice would bring it below zero, set it to one past last
            if choice == 0:
                choice = len(text_list)
            # And decrement it.
            choice -= 1

            # Redraw new box in correct color.
            display.printc(box_left, box_start + choice * box_size, box, color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice], color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box, color_list[choice])
            # Refresh display
            display.refresh()
            # Wait for release
            while display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
                pass
        if display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
            # Redraw current box in white
            display.printc(box_left, box_start + choice * box_size, box)
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box)
            # Go down
            choice += 1
            # Wrap options
            if choice == len(text_list):
                choice = 0
            # Redraw new box in correct color.
            display.printc(box_left, box_start + choice * box_size, box, color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice], color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box, color_list[choice])
            # Refresh display
            display.refresh()
            # Wait for release
            while display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
                pass

        # Check if they chose an option
        if display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
            # Basic player. Choice will modify it's attributes.
            world.player = world_object.world_object(player.player_update, player.collide, player.player_char, player.player_color, "player", 0, 0, player.player_attributes)
            hat = shirt = pants = ring = weapon = None
            spell = None
            if not choice: # Choice was 0, so warrior
                # Create player as warrior character
                # Their equipment
                hat = item.item(clothhat.name, clothhat.type, clothhat.on_equip, clothhat.on_unequip, 1, clothhat.attributes)
                shirt = item.item(clothShirt.name, clothShirt.type, clothShirt.on_equip, clothShirt.on_unequip, 1, clothShirt.attributes)
                pants = item.item(clothPants.name, clothPants.type, clothPants.on_equip, clothPants.on_unequip, 1, clothPants.attributes)
                ring = item.item(UselessRingg.name, UselessRingg.type, UselessRingg.on_equip, UselessRingg.on_unequip, 1, UselessRingg.attributes)
                weapon = item.item(okaySword.name, okaySword.type, okaySword.on_equip, okaySword.on_unequip, 1, okaySword.attributes)
            if choice == 1: # Choice was Mage
                # Create player as mage.
                pass
            if choice == 2: # Choice was Thief
                pass

            world.player.attributes["items"] = [hat, shirt, pants, ring, weapon, spell] # Give them their equips
            world.player.attributes["hat"] = hat                                        # Equip everything!
            hat.equip(hat, world.player)
            world.player.attributes["shirt"] = shirt
            shirt.equip(shirt, world.player)
            world.player.attributes["pants"] = pants
            pants.equip(pants, world.player)
            world.player.attributes["ring"] = ring
            ring.equip(ring, world.player)
            world.player.attributes["weapon"] = weapon
            weapon.equip(weapon, world.player)
            world.player.attributes["spell"] = spell
                
            # Load starting world
            world.load("start")
            return

def start():
    """Gives the main menu option to load a file, create a new file, or exit"""
    display.printc(28, 10, "Welcome to pyRPG!")
    display.printc(30, 11, ">Load a file")
    display.printc(31, 12, "New game")
    display.printc(31, 13, "Exit game")
    display.refresh()
    opt = 0
    while True:

        # Move cursor up if w or up key pressed
        if display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
            # Clear old cursor
            display.printc(30, opt + 11, ' ')
            opt -= 1
            if opt < 0:
                opt = 2
            # Redraw for good menu
            display.printc(30, opt + 11, '>')
            display.refresh()      
            # Wait for release
            while display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
                pass

        # Move cursor down if s or down key pressed
        if display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
            # Clear old cursor
            display.printc(30, opt + 11, ' ')
            opt += 1
            if opt > 2:
                opt = 0
            # Redraw for good menu
            display.printc(30, opt + 11, '>')
            display.refresh()      
            # Wait for release
            while display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
                pass

        # If they have e or enter pressed, they chose an option.
        if display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
            # Wait for key release
            while display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
                pass
            if opt == 0:
                load_game()
                display.clear()
                return
            if opt == 1:
                new_game()
                world.save_player()
                display.clear()
                return
            if opt == 2:
                display.end() # They chose exit

