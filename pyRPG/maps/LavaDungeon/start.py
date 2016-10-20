# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import copy

import display
import world

from objects import LavaDungeon
from objects.General import portal
from objects.General import npc

def generate():
    world.objects.clear()
    world.map = [[ [display.WHITE, display.BLACK, '.', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    world.objects.append(LavaDungeon.lava.lava())
    world.objects.append(portal.portal(0, 10, "town", 25, 10))
    world.objects.append(portal.portal(25, 10, "lavadungeon.1", 25, 10))
    world.objects.append(LavaDungeon.enemy.generic_enemy(15, 7))
    world.objects.append(LavaDungeon.enemy.generic_enemy(43, 5))
    world.objects.append(LavaDungeon.enemy.generic_enemy(35, 15))
    npc_text = "Hello, adventurer.\nA warning before you enter\n the volcano:\nIt contains an\n ancient deadly beast.\nThere is no escape\n from the volcano before\n the beast is slain."
    world.objects.append(npc.npc(23, 9, npc_text))

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
    world.map[27][2] =  [display.RED, display.BLACK, '.', True]
    world.map[28][2] =  [display.RED, display.BLACK, '.', True]
    world.map[29][2] =  [display.RED, display.BLACK, '.', True]
    world.map[49][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][3] =  [display.RED, display.BLACK, '.', True]
    world.map[6][3] =  [display.RED, display.BLACK, '.', True]
    world.map[7][3] =  [display.RED, display.BLACK, '.', True]
    world.map[8][3] =  [display.RED, display.BLACK, '.', True]
    world.map[9][3] =  [display.RED, display.BLACK, '.', True]
    world.map[25][3] =  [display.RED, display.BLACK, '.', True]
    world.map[26][3] =  [display.RED, display.BLACK, '.', True]
    world.map[27][3] =  [display.RED, display.BLACK, '.', True]
    world.map[28][3] =  [display.RED, display.RED, '#', True]
    world.map[29][3] =  [display.RED, display.BLACK, '.', True]
    world.map[49][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][4] =  [display.RED, display.BLACK, '.', True]
    world.map[6][4] =  [display.RED, display.RED, '#', True]
    world.map[7][4] =  [display.RED, display.RED, '#', True]
    world.map[8][4] =  [display.RED, display.RED, '#', True]
    world.map[9][4] =  [display.RED, display.BLACK, '.', True]
    world.map[24][4] =  [display.RED, display.BLACK, '.', True]
    world.map[25][4] =  [display.RED, display.BLACK, '.', True]
    world.map[26][4] =  [display.RED, display.RED, '#', True]
    world.map[27][4] =  [display.RED, display.RED, '#', True]
    world.map[28][4] =  [display.RED, display.RED, '#', True]
    world.map[29][4] =  [display.RED, display.BLACK, '.', True]
    world.map[30][4] =  [display.RED, display.BLACK, '.', True]
    world.map[49][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][5] =  [display.RED, display.BLACK, '.', True]
    world.map[6][5] =  [display.RED, display.BLACK, '.', True]
    world.map[7][5] =  [display.RED, display.RED, '#', True]
    world.map[8][5] =  [display.RED, display.BLACK, '.', True]
    world.map[9][5] =  [display.RED, display.BLACK, '.', True]
    world.map[24][5] =  [display.RED, display.BLACK, '.', True]
    world.map[25][5] =  [display.RED, display.RED, '#', True]
    world.map[26][5] =  [display.RED, display.RED, '#', True]
    world.map[27][5] =  [display.RED, display.RED, '#', True]
    world.map[28][5] =  [display.RED, display.RED, '#', True]
    world.map[29][5] =  [display.RED, display.RED, '#', True]
    world.map[30][5] =  [display.RED, display.BLACK, '.', True]
    world.map[31][5] =  [display.RED, display.BLACK, '.', True]
    world.map[49][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][6] =  [display.RED, display.BLACK, '.', True]
    world.map[7][6] =  [display.RED, display.BLACK, '.', True]
    world.map[8][6] =  [display.RED, display.BLACK, '.', True]
    world.map[24][6] =  [display.RED, display.BLACK, '.', True]
    world.map[25][6] =  [display.RED, display.RED, '#', True]
    world.map[26][6] =  [display.RED, display.RED, '#', True]
    world.map[27][6] =  [display.RED, display.BLACK, '.', True]
    world.map[28][6] =  [display.RED, display.RED, '#', True]
    world.map[29][6] =  [display.RED, display.RED, '#', True]
    world.map[30][6] =  [display.RED, display.RED, '#', True]
    world.map[31][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][7] =  [display.RED, display.RED, '#', True]
    world.map[26][7] =  [display.RED, display.BLACK, '.', True]
    world.map[27][7] =  [display.RED, display.BLACK, '.', True]
    world.map[28][7] =  [display.RED, display.BLACK, '.', True]
    world.map[29][7] =  [display.RED, display.RED, '#', True]
    world.map[30][7] =  [display.RED, display.BLACK, '.', True]
    world.map[31][7] =  [display.RED, display.BLACK, '.', True]
    world.map[32][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][7] =  [display.RED, display.BLACK, '.', True]
    world.map[35][7] =  [display.RED, display.BLACK, '.', True]
    world.map[36][7] =  [display.RED, display.BLACK, '.', True]
    world.map[37][7] =  [display.RED, display.BLACK, '.', True]
    world.map[38][7] =  [display.RED, display.BLACK, '.', True]
    world.map[39][7] =  [display.RED, display.BLACK, '.', True]
    world.map[49][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][8] =  [display.RED, display.BLACK, '.', True]
    world.map[26][8] =  [display.RED, display.BLACK, '.', True]
    world.map[28][8] =  [display.RED, display.BLACK, '.', True]
    world.map[29][8] =  [display.RED, display.BLACK, '.', True]
    world.map[30][8] =  [display.RED, display.BLACK, '.', True]
    world.map[34][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][8] =  [display.RED, display.RED, '#', True]
    world.map[36][8] =  [display.RED, display.RED, '#', True]
    world.map[37][8] =  [display.RED, display.BLACK, '.', True]
    world.map[38][8] =  [display.RED, display.RED, '#', True]
    world.map[39][8] =  [display.RED, display.BLACK, '.', True]
    world.map[40][8] =  [display.RED, display.BLACK, '.', True]
    world.map[49][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][9] =  [display.RED, display.BLACK, '.', True]
    world.map[17][9] =  [display.RED, display.BLACK, '.', True]
    world.map[18][9] =  [display.RED, display.BLACK, '.', True]
    world.map[19][9] =  [display.RED, display.BLACK, '.', True]
    world.map[21][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][9] =  [display.RED, display.BLACK, '.', True]
    world.map[35][9] =  [display.RED, display.RED, '#', True]
    world.map[36][9] =  [display.RED, display.RED, '#', True]
    world.map[37][9] =  [display.RED, display.RED, '#', True]
    world.map[38][9] =  [display.RED, display.RED, '#', True]
    world.map[39][9] =  [display.RED, display.RED, '#', True]
    world.map[40][9] =  [display.RED, display.BLACK, '.', True]
    world.map[49][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][10] =  [display.WHITE, display.BLACK, '.', True]
    world.map[15][10] =  [display.RED, display.BLACK, '.', True]
    world.map[16][10] =  [display.RED, display.BLACK, '.', True]
    world.map[17][10] =  [display.RED, display.RED, '#', True]
    world.map[18][10] =  [display.RED, display.RED, '#', True]
    world.map[19][10] =  [display.RED, display.BLACK, '.', True]
    world.map[20][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][10] =  [display.RED, display.RED, '#', True]
    world.map[36][10] =  [display.RED, display.RED, '#', True]
    world.map[37][10] =  [display.RED, display.RED, '#', True]
    world.map[38][10] =  [display.RED, display.BLACK, '.', True]
    world.map[39][10] =  [display.RED, display.BLACK, '.', True]
    world.map[40][10] =  [display.RED, display.BLACK, '.', True]
    world.map[49][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][11] =  [display.RED, display.BLACK, '.', True]
    world.map[16][11] =  [display.RED, display.RED, '#', True]
    world.map[17][11] =  [display.RED, display.RED, '#', True]
    world.map[18][11] =  [display.RED, display.RED, '#', True]
    world.map[19][11] =  [display.RED, display.RED, '#', True]
    world.map[20][11] =  [display.RED, display.BLACK, '.', True]
    world.map[32][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][11] =  [display.RED, display.BLACK, '.', True]
    world.map[35][11] =  [display.RED, display.BLACK, '.', True]
    world.map[36][11] =  [display.RED, display.RED, '#', True]
    world.map[37][11] =  [display.RED, display.BLACK, '.', True]
    world.map[38][11] =  [display.RED, display.BLACK, '.', True]
    world.map[49][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][12] =  [display.RED, display.BLACK, '.', True]
    world.map[16][12] =  [display.RED, display.RED, '#', True]
    world.map[17][12] =  [display.RED, display.RED, '#', True]
    world.map[18][12] =  [display.RED, display.RED, '#', True]
    world.map[19][12] =  [display.RED, display.BLACK, '.', True]
    world.map[20][12] =  [display.RED, display.BLACK, '.', True]
    world.map[32][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][12] =  [display.RED, display.BLACK, '.', True]
    world.map[36][12] =  [display.RED, display.BLACK, '.', True]
    world.map[37][12] =  [display.RED, display.BLACK, '.', True]
    world.map[49][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][13] =  [display.RED, display.BLACK, '.', True]
    world.map[16][13] =  [display.RED, display.BLACK, '.', True]
    world.map[17][13] =  [display.RED, display.RED, '#', True]
    world.map[18][13] =  [display.RED, display.RED, '#', True]
    world.map[19][13] =  [display.RED, display.BLACK, '.', True]
    world.map[20][13] =  [display.RED, display.BLACK, '.', True]
    world.map[30][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][14] =  [display.RED, display.BLACK, '.', True]
    world.map[17][14] =  [display.RED, display.BLACK, '.', True]
    world.map[18][14] =  [display.RED, display.RED, '#', True]
    world.map[19][14] =  [display.RED, display.RED, '#', True]
    world.map[20][14] =  [display.RED, display.BLACK, '.', True]
    world.map[21][14] =  [display.RED, display.BLACK, '.', True]
    world.map[27][14] =  [display.RED, display.BLACK, '.', True]
    world.map[28][14] =  [display.RED, display.BLACK, '.', True]
    world.map[29][14] =  [display.RED, display.BLACK, '.', True]
    world.map[30][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][15] =  [display.RED, display.BLACK, '.', True]
    world.map[18][15] =  [display.RED, display.RED, '#', True]
    world.map[19][15] =  [display.RED, display.RED, '#', True]
    world.map[20][15] =  [display.RED, display.RED, '#', True]
    world.map[21][15] =  [display.RED, display.BLACK, '.', True]
    world.map[27][15] =  [display.RED, display.BLACK, '.', True]
    world.map[28][15] =  [display.RED, display.RED, '#', True]
    world.map[29][15] =  [display.RED, display.RED, '#', True]
    world.map[30][15] =  [display.RED, display.BLACK, '.', True]
    world.map[31][15] =  [display.RED, display.BLACK, '.', True]
    world.map[49][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][16] =  [display.RED, display.BLACK, '.', True]
    world.map[17][16] =  [display.RED, display.BLACK, '.', True]
    world.map[18][16] =  [display.RED, display.BLACK, '.', True]
    world.map[19][16] =  [display.RED, display.RED, '#', True]
    world.map[20][16] =  [display.RED, display.RED, '#', True]
    world.map[21][16] =  [display.RED, display.BLACK, '.', True]
    world.map[27][16] =  [display.RED, display.BLACK, '.', True]
    world.map[28][16] =  [display.RED, display.BLACK, '.', True]
    world.map[29][16] =  [display.RED, display.BLACK, '.', True]
    world.map[30][16] =  [display.RED, display.RED, '#', True]
    world.map[31][16] =  [display.RED, display.BLACK, '.', True]
    world.map[49][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][17] =  [display.RED, display.BLACK, '.', True]
    world.map[17][17] =  [display.RED, display.RED, '#', True]
    world.map[18][17] =  [display.RED, display.RED, '#', True]
    world.map[19][17] =  [display.RED, display.RED, '#', True]
    world.map[20][17] =  [display.RED, display.BLACK, '.', True]
    world.map[21][17] =  [display.RED, display.BLACK, '.', True]
    world.map[29][17] =  [display.RED, display.BLACK, '.', True]
    world.map[30][17] =  [display.RED, display.BLACK, '.', True]
    world.map[31][17] =  [display.RED, display.BLACK, '.', True]
    world.map[49][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][18] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][18] =  [display.RED, display.BLACK, '.', True]
    world.map[17][18] =  [display.RED, display.BLACK, '.', True]
    world.map[18][18] =  [display.RED, display.RED, '#', True]
    world.map[19][18] =  [display.RED, display.RED, '#', True]
    world.map[20][18] =  [display.RED, display.BLACK, '.', True]
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
