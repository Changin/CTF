from PIL import Image

f = open("flag.txt",'r')

#947
#474
#200
#632
y = 632
x = 121783/y

size = (y,x)
img = Image.new("RGB",size,(255,255,255))

for i in range(1,x):
	for j in range(1,y):
		
		line = f.readline()
		if not line: break
		img.putpixel((j,i),eval(line))

img.save("flag.bmp")
f.close()