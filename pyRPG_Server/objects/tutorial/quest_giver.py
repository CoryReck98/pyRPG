import copy

import world

from objects import General
from objects.Player import player_flags

class quest_giver(General.npc.npc):
    """Talks to the player.""" #TODO: add a good interface for complex dialog trees.

    def update(this, delta_time):
        "Talks to player if they're standing next to it."
        for plr in world.players:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                if plr not in this.attributes["talking_players"]: # Not talking to them already
                    diag = copy.deepcopy(this.attributes["dialogue"])
                    diag.linked_player = plr
                    if not player_flags.get_flag(plr, player_flags.TUT_MONEY_GIVEN): # Don't have tut money, so give it
                        diag.nodes["start"].text += "\nYou're new. Take this money.\nUse it to buy some gear\n at the (\\fyM\\fw) Merchant"
                        print(diag.nodes["start"].options)
                        diag.nodes["start"].options = [("Thanks!", "money")]
                    this.attributes["talking_players"][plr] = diag

        left_players = []
        for plr, diag in this.attributes["talking_players"].items(): 
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                diag.run()
            else:
                left_players.append(plr)
            if plr not in world.players:
                left_players.append(plr)

        for gone in left_players:
            del this.attributes["talking_players"][gone]
            gone.attributes["current_menu"] = None

        if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
            world.to_del.append(this)
    
    

