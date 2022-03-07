# IMG_20170103_124522.jpg IMG_20170104_113321.jpg IMG_20170107_223749.jpg
# P020117_203138.jpg P030117_052636.jpg

place = input()
img = input()
p = input()

imgs = img.split(" ")
ps = p.split(" ")


def img_to_date(img):
	return img[4:12]+img[13:-4]

def p_to_date(p):
	return "20"+p[5:7]+p[3:5]+p[1:3]+p[8:-4]

total = imgs+ps
 
def resoldre(photos):
	n = len(photos)
	"""
	Bubble sort -> ordenar fotos
	corre la array tantes vegades com elements hi ha.
	per cada bucle corre la array pero cada vegada un element menys.
	i per cada iteració si j > j+1 fa un canvi de posicions.
	tots els elements que queden per la dreta sera la part ordenada.
	
	les imprimeix ordenades
	"""
	for i in range(n-1):
		for j in range(0, n-i-1):
			img_a = photos[j]
			img_b = photos[j + 1]
            
			if img_a[:3] == "IMG":
				img_a_num = img_to_date(img_a)
			elif img_a[0] == "P":
				img_a_num = p_to_date(img_a)
            
			if img_b[:3] == "IMG":
				img_b_num = img_to_date(img_b)
			elif img_b[0] == "P":
				img_b_num = p_to_date(img_b)
			
			
			if int(img_a_num) > int(img_b_num):
				tmp = photos[j]
				photos[j] = photos[j + 1]
				photos[j + 1] = tmp
				
	for x in range(len (total)):
		print("mv", total[x], place+"_"+f"{x:03}"+".jpg")
				
				
resoldre(total)
