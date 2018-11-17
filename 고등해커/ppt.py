# -*- coding: utf-8 -*-
import string
from itertools import product

def Sub(inputString):
	flg = inputString #input String

	bt = [[0]*100 for i in range(10)] #bool

	for i in range(8):	#0~7
		for j in range(len(flg)): 0~31
			bt[i][j] = (((ord(flg[j])) & (2**i)) == 0)

	fla = [[0]*100 for i in range(12)] #bool

	fla[0][0] = False
	fla[0][1] = False
	fla[0][2] = True
	fla[0][3] = True
	fla[0][4] = False
	fla[0][5] = True
	fla[0][6] = False
	fla[0][7] = True
	fla[0][8] = False
	fla[0][9] = True
	fla[0][10] = False
	fla[0][11] = True
	fla[0][12] = False
	fla[0][13] = False
	fla[0][14] = True
	fla[0][15] = True
	fla[0][16] = True
	fla[0][17] = True
	fla[0][18] = False
	fla[0][19] = False
	fla[0][20] = True
	fla[0][21] = False
	fla[0][22] = True
	fla[0][23] = False
	fla[0][24] = False
	fla[0][25] = True
	fla[0][26] = True
	fla[0][27] = False
	fla[0][28] = False
	fla[0][29] = False
	fla[0][30] = False
	fla[1][0] = False
	fla[1][1] = True
	fla[1][2] = False
	fla[1][3] = False
	fla[1][4] = True
	fla[1][5] = False
	fla[1][6] = False
	fla[1][7] = True
	fla[1][8] = False
	fla[1][9] = False
	fla[1][10] = True
	fla[1][11] = False
	fla[1][12] = False
	fla[1][13] = False
	fla[1][14] = True
	fla[1][15] = True
	fla[1][16] = True
	fla[1][17] = False
	fla[1][18] = False
	fla[1][19] = False
	fla[1][20] = False
	fla[1][21] = True
	fla[1][22] = False
	fla[1][23] = False
	fla[1][24] = False
	fla[1][25] = False
	fla[1][26] = True
	fla[1][27] = True
	fla[1][28] = False
	fla[1][29] = True
	fla[1][30] = True
	fla[2][0] = True
	fla[2][1] = False
	fla[2][2] = False
	fla[2][3] = True
	fla[2][4] = True
	fla[2][5] = False
	fla[2][6] = True
	fla[2][7] = True
	fla[2][8] = False
	fla[2][9] = False
	fla[2][10] = True
	fla[2][11] = False
	fla[2][12] = False
	fla[2][13] = False
	fla[2][14] = True
	fla[2][15] = True
	fla[2][16] = False
	fla[2][17] = False
	fla[2][18] = False
	fla[2][19] = False
	fla[2][20] = False
	fla[2][21] = True	
	fla[2][22] = False
	fla[2][23] = False
	fla[2][24] = False
	fla[2][25] = False
	fla[2][26] = False
	fla[2][27] = True
	fla[2][28] = False
	fla[2][29] = True
	fla[2][30] = False
	fla[3][0] = True
	fla[3][1] = True
	fla[3][2] = False
	fla[3][3] = True
	fla[3][4] = False
	fla[3][5] = False
	fla[3][6] = False
	fla[3][7] = True
	fla[3][8] = True
	fla[3][9] = False
	fla[3][10] = False
	fla[3][11] = False
	fla[3][12] = True
	fla[3][13] = False
	fla[3][14] = True
	fla[3][15] = True
	fla[3][16] = True
	fla[3][17] = True
	fla[3][18] = False
	fla[3][19] = True
	fla[3][20] = False
	fla[3][21] = False
	fla[3][22] = False
	fla[3][23] = True
	fla[3][24] = False
	fla[3][25] = True
	fla[3][26] = False
	fla[3][27] = True
	fla[3][28] = True
	fla[3][29] = True
	fla[3][30] = False
	fla[4][0] = False
	fla[4][1] = False
	fla[4][2] = True
	fla[4][3] = False
	fla[4][4] = True
	fla[4][5] = True
	fla[4][6] = False
	fla[4][7] = False
	fla[4][8] = False
	fla[4][9] = True
	fla[4][10] = True
	fla[4][11] = True
	fla[4][12] = True
	fla[4][13] = False
	fla[4][14] = False
	fla[4][15] = False
	fla[4][16] = False
	fla[4][17] = True
	fla[4][18] = True
	fla[4][19] = False
	fla[4][20] = True
	fla[4][21] = True
	fla[4][22] = True	
	fla[4][23] = True
	fla[4][24] = False
	fla[4][25] = True	
	fla[4][26] = True
	fla[4][27] = True
	fla[4][28] = True
	fla[4][29] = True
	fla[4][30] = False
	fla[5][0] = True
	fla[5][1] = False
	fla[5][2] = False
	fla[5][3] = False
	fla[5][4] = False
	fla[5][5] = False
	fla[5][6] = False
	fla[5][7] = False
	fla[5][8] = False
	fla[5][9] = False
	fla[5][10] = False
	fla[5][11] = False
	fla[5][12] = False
	fla[5][13] = True
	fla[5][14] = True
	fla[5][15] = True
	fla[5][16] = True
	fla[5][17] = False
	fla[5][18] = False
	fla[5][19] = False
	fla[5][20] = False
	fla[5][21] = False
	fla[5][22] = False
	fla[5][23] = False
	fla[5][24] = True
	fla[5][25] = False
	fla[5][26] = False
	fla[5][27] = False
	fla[5][28] = False
	fla[5][29] = False
	fla[5][30] = False
	fla[6][0] = False
	fla[6][1] = False
	fla[6][2] = False
	fla[6][3] = False
	fla[6][4] = False
	fla[6][5] = False
	fla[6][6] = False
	fla[6][7] = False
	fla[6][8] = False
	fla[6][9] = False
	fla[6][10] = False
	fla[6][11] = False
	fla[6][12] = False
	fla[6][13] = False
	fla[6][14] = False
	fla[6][15] = False
	fla[6][16] = False
	fla[6][17] = True
	fla[6][18] = False
	fla[6][19] = False
	fla[6][20] = False
	fla[6][21] = False
	fla[6][22] = False
	fla[6][23] = False
	fla[6][24] = False
	fla[6][25] = False
	fla[6][26] = False
	fla[6][27] = False
	fla[6][28] = False
	fla[6][29] = True
	fla[6][30] = False
	fla[7][0] = True
	fla[7][1] = True
	fla[7][2] = True
	fla[7][3] = True
	fla[7][4] = True
	fla[7][5] = True
	fla[7][6] = True
	fla[7][7] = True
	fla[7][8] = True
	fla[7][9] = True
	fla[7][10] = True
	fla[7][11] = True
	fla[7][12] = True
	fla[7][13] = True
	fla[7][14] = True
	fla[7][15] = True
	fla[7][16] = True
	fla[7][17] = True
	fla[7][18] = True
	fla[7][19] = True
	fla[7][20] = True
	fla[7][21] = True
	fla[7][22] = True
	fla[7][23] = True
	fla[7][24] = True
	fla[7][25] = True
	fla[7][26] = True
	fla[7][27] = True
	fla[7][28] = True
	fla[7][29] = True
	fla[7][30] = True

	flagage = True

	for i in range(8): #0~7
		for j in range(len(flg)): #0~31
			flagage = flagage and (fla[i][j] == bt[i][j])

	if flagage and len(flg) == 31:
		print(flg) #Success
		return 1
	else:
		print("Nope")
		return 0

chars = string.printable
to_attempt = product(chars, repeat=31)
for attempt in to_attempt:
	brute = ''.join(attempt)
	print(brute)
	if(Sub(brute) == 1):
		break