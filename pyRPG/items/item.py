import display
# Item class. Note that for all equipment, certain attribute modifiers will be displayed in the menu:
# maxHP = red
# maxMP = blue
# mov_spd = green
# atk_spd = white
# magic = cyan
# str = magenta
# luck = yellow
# To override this, add the attribute "disp_data".
class item:
    """Item class, all items in the game are part of this.
"""
    def __init__(this, item_name, type, sell_value, quantity = 1, attr = {}):
        """Parameters:
            item_name: The name of the item.
            type: What type it is. hat, pants, consumable...
            sell_value: How much it sells for. 0 if it is unsellable
            quantity: How many there are.
"""
        this.name = item_name
        this.amount = quantity
        this.value = sell_value
        this.attributes = attr
        this.type = type
        if "disp_data" not in this.attributes: # They gave no default display data. Make it.
            disp_str = "" # Go through all default modifiers and add them to the string.
            if this.type == "weapon":
                # It's a weapon, so we need to show range and damage
                disp_str += " Range " + str(this.attributes["range"]) + " " # Add range
                disp_str += "Damage " + str(this.attributes["damage"]) + " " # Add damage
            if "maxHP_mod" in this.attributes:
                disp_str += "\\fr("
                if this.attributes["maxHP_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["maxHP_mod"]) + ")"
            if "maxMP_mod" in this.attributes:
                disp_str += "\\fb("
                if this.attributes["maxMP_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["maxMP_mod"]) + ")"
            if "mov_spd_mod" in this.attributes:
                disp_str += "\\fg("
                if this.attributes["mov_spd_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["mov_spd_mod"]) + ")"
            if "atk_spd_mod" in this.attributes:
                disp_str += "\\fw("
                if this.attributes["atk_spd_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["atk_spd_mod"]) + ")"
            if "magic_mod" in this.attributes:
                disp_str += "\\fc("
                if this.attributes["magic_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["magic_mod"]) + ")"
            if "str_mod" in this.attributes:
                disp_str += "\\fm("
                if this.attributes["str_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["str_mod"]) + ")"
            if "luck_mod" in this.attributes:
                disp_str += "\\fy("
                if this.attributes["luck_mod"] >= 0:
                    disp_str += "+"
                disp_str += str(this.attributes["luck_mod"]) + ")"
            this.attributes["disp_data"] = disp_str # Add string to disp mod.

    def __lt__(self, other):
        return self.name < other
    
    def ___le__(self, other):
        return self.name <= other
    
    def __eq__(self, other):
        "For objects to be equal, they need same name, attributes, type, and value."
        return (self.name == other.name) and (self.attributes == other.attributes) and (self.type == other.type) and (self.value == other.value)
    
    def __ne__(self, other):
        return self.name != other
    
    def __gt__(self, other):
        return self.name > other
    
    def __ge__(self, other):
        return self.name >= other

    def draw(this):
        "Draws the consumable icon. Only needed if it's a consumable"
        display.printc(display.SPELL_BOX_START + 7, 1, this.attributes["icon"][0], this.attributes["color"])
        display.printc(display.SPELL_BOX_START + 7, 2, this.attributes["icon"][1], this.attributes["color"])
        display.printc(display.SPELL_BOX_START + 7, 3, this.attributes["icon"][2], this.attributes["color"])

    # Default equip and unequip functions. Use these when having normal enchantments.
    def equip(this, player):
        if "maxHP_mod" in this.attributes:
            player.attributes["maxHP"] += this.attributes["maxHP_mod"]
            player.attributes["HP"] += this.attributes["maxHP_mod"]
        if "maxMP_mod" in this.attributes:
            player.attributes["maxMP"] += this.attributes["maxMP_mod"]
            player.attributes["MP"] += this.attributes["maxMP_mod"]
        if "mov_spd_mod" in this.attributes:
            player.attributes["mov_spd"] += this.attributes["mov_spd_mod"]
        if "atk_spd_mod" in this.attributes:
            player.attributes["atk_spd"] += this.attributes["atk_spd_mod"]
        if "magic_mod" in this.attributes:
            player.attributes["magic"] += this.attributes["magic_mod"]
        if "str_mod" in this.attributes:
            player.attributes["strength"] += this.attributes["str_mod"]
        if "luck_mod" in this.attributes:
            player.attributes["luck"] += this.attributes["luck_mod"]
    def unequip(this, player):
        if "maxHP_mod" in this.attributes:
            player.attributes["maxHP"] -= this.attributes["maxHP_mod"]
            player.attributes["HP"] -= this.attributes["maxHP_mod"]
        if "maxMP_mod" in this.attributes:
            player.attributes["maxMP"] -= this.attributes["maxMP_mod"]
            player.attributes["MP"] -= this.attributes["maxMP_mod"]
        if "mov_spd_mod" in this.attributes:
            player.attributes["mov_spd"] -= this.attributes["mov_spd_mod"]
        if "atk_spd_mod" in this.attributes:
            player.attributes["atk_spd"] -= this.attributes["atk_spd_mod"]
        if "magic_mod" in this.attributes:
            player.attributes["magic"] -= this.attributes["magic_mod"]
        if "str_mod" in this.attributes:
            player.attributes["strength"] -= this.attributes["str_mod"]
        if "luck_mod" in this.attributes:
            player.attributes["luck"] -= this.attributes["luck_mod"]
