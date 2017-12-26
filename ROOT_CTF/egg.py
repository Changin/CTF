arr = 'Mh;y;mR1@OijQhHW6Ah=hB'
result = ""


def sha(a):
	v2 = [8,9,0xF,5,0xB,1,3,5,0xD,1,0xE,3,4,0xE,7,4,0xC1,6,6,0xC,0xF,0xA,0xC,0xA,2,0xD,8,7,3,7,1,7,5,8,0xC,3,4,0xB,0xE,5,1,0xB,0,3,9,4,5,0,6,8,0xC,5,3,0xA,0xF,3,0xE,0xF,4,8,0xA,0xB,0xF,2]
	return v2[r(a)]

def r(a):
	y = 17
	m = 12
	d = 21

	v = a

	for i in range(17): #0~16
		v ^= y
		for j in range(12):
			v ^= m
			for k in range(21):
				v ^= d

	return v

print("FLAG={",end='')
for i in range(22): #0~21
	tmp = ord(arr[i])^int(str(sha(i+2)))
	print(chr(tmp),end='')

print("}")