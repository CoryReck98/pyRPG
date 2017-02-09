# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import General
from items import t1_warrior

from objects.Player import player_flags
from objects import tutorial

def give_money(player):
    player.attributes["money"] += 50
    player_flags.set_flag(player, player_flags.TUT_MONEY_GIVEN, 1)

def generate():
    world.objects.clear()

    # Add merchants
    world.objects.append(General.merchant.merchant(6, 16, [t1_warrior.t1_warrior_hat(), t1_warrior.t1_warrior_pants(), t1_warrior.t1_warrior_ring(), t1_warrior.t1_warrior_shirt(), t1_warrior.t1_warrior_weapon()]))
    world.objects.append(General.merchant.merchant(43, 16, [t1_warrior.t1_warrior_hat(), t1_warrior.t1_warrior_pants(), t1_warrior.t1_warrior_ring(), t1_warrior.t1_warrior_shirt(), t1_warrior.t1_warrior_weapon()]))
    
    # Add portals
    world.objects.append(General.portal.portal(49, 9, "war_tut-1", 1, 10))
    world.objects.append(General.level_portal.level_portal(24, 19, "warrior_start", 24, 1, 5))

    # Add tutorial guy who gives you equip money.
    dialogue_tree = General.npc.dialogue_tree()
    dialogue_tree.add_node("start", General.npc.node("Welcome to Doobyville,\n the warrior town!", ("Bye", "exit")))
    dialogue_tree.add_exit("exit", 0)
    dialogue_tree.add_exit("money", 1, give_money)
    world.objects.append(tutorial.quest_giver.quest_giver(39, 4, dialogue_tree))

    world.map = [[ [display.GREEN, display.BLACK, ';', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
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
    world.map[4][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[26][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[6][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[7][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[8][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[9][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[10][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[11][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[16][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[17][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[18][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[19][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[20][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[21][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[22][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[23][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[24][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[25][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[26][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[27][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[28][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[29][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[30][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[31][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[32][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[33][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[34][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[35][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[40][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[41][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[42][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[43][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[44][3] =  [display.WHITE, display.BLACK, '.', True]
    world.map[45][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[6][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[7][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[8][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[9][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[10][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[11][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[16][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[17][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[18][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[19][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[20][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[21][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[22][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[23][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[24][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[25][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[26][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[27][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[28][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[29][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[30][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[31][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[32][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[33][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[34][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[35][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[40][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[41][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[42][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[43][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[44][4] =  [display.WHITE, display.BLACK, '.', True]
    world.map[45][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[8][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[16][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[17][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[18][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[19][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[20][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[21][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[22][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[23][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[24][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[25][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[26][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[27][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[28][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[29][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[30][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[31][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[32][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[33][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[34][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[35][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][5] =  [display.WHITE, display.BLACK, '.', True]
    world.map[43][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[16][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[17][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[18][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[19][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[20][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[21][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[22][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[23][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[24][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[25][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[26][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[27][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[28][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[29][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[30][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[31][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[32][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[33][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[34][6] =  [display.WHITE, display.BLACK, '.', True]
    world.map[35][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[16][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[17][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[18][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[19][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[20][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[21][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[22][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[23][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[24][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[25][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[26][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[27][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[28][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[29][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[30][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[31][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[32][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[33][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[34][7] =  [display.WHITE, display.BLACK, '.', True]
    world.map[35][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][8] =  [display.WHITE, display.BLACK, '.', True]
    world.map[24][8] =  [display.WHITE, display.BLACK, '.', True]
    world.map[25][8] =  [display.WHITE, display.BLACK, '.', True]
    world.map[26][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][9] =  [display.WHITE, display.BLACK, '#', False]
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
    world.map[3][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][15] =  [display.WHITE, display.BLACK, '.', True]
    world.map[7][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][15] =  [display.WHITE, display.BLACK, '.', True]
    world.map[44][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[5][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[6][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[8][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[9][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[42][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[43][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[45][16] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[46][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][17] =  [display.WHITE, display.BLACK, '#', False]
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