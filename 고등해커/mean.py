# -*- coding: utf-8 -*-
str = ['01010011', '01110101', '01101110', '01110010', '01101001', '01101110', '01111011', '01000100', '00110000', '01011111', '01111001', '00110000', '01110101', '01011111', '01101011', '01101110', '00110000', '01110111', '01011111', '01100010', '00110001', '01101110', '00110100', '01110010', '01111001', '00111111', '01111101']

for i in str:
	print(chr(int(i,2)),end='')
print()