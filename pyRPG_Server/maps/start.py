# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world
from objects import General
from items import bread

def to_warr(player):
    player.attributes["class"] = "warrior"
    player.X = 24  # Set start coords for new map
    player.Y = 13
    player.attributes["respawnX"] = 24  # Set respawn info
    player.attributes["respawnY"] = 13
    player.attributes["respawnMap"] = "warrior_start"
    world.to_del_plr.append(player) # Move player
    world.move_requests.append(("warrior_start", player))
 
def to_mage(player):
    player.attributes["class"] = "mage"
    player.X = 9
    player.Y = 9
    player.attributes["respawnX"] = 9
    player.attributes["respawnY"] = 9
    player.attributes["respawnMap"] = "mage_start"
    world.to_del_plr.append(player)
    world.move_requests.append(("mage_start", player))

def to_thief(player):
    player.attributes["class"] = "thief"
    player.X = 43
    player.Y = 12
    player.attributes["respawnX"] = 34
    player.attributes["respawnY"] = 12
    player.attributes["respawnMap"] = "thief_start"
    world.to_del_plr.append(player)
    world.move_requests.append(("thief_start", player))

def generate():
    world.objects.clear()

    dialogue_tree = General.npc.dialogue_tree()
    dialogue_tree.add_node("start", General.npc.node("Welcome to pyRPG Multiplayer!\nChoose a class:", ("Warrior!", "warr"), ("Mage!", "mage"), ("Thief!", "thief")))
    dialogue_tree.add_exit("warr", 0, to_warr)
    dialogue_tree.add_exit("mage", 1, to_mage)
    dialogue_tree.add_exit("thief",2, to_thief)
    world.objects.append(General.npc.npc(25, 4, dialogue_tree))


    world.map = [[ [display.WHITE, display.BLACK, ' ', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[0][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[12][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[13][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[26][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[37][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][18] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][18] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[12][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[13][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[26][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[37][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][19] =  [display.WHITE, display.BLACK, '#', False]
