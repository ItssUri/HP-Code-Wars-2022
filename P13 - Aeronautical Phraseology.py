ll = []
while True:
	a = input()
	if a == "#":
		break
	ll.append(a)
	
"""
A123BC
D119 left Y right H
Delta Echo Golf cleared for take-off
F456 altimeter 30.05 maintain 13000
#
"""

def convertible(word):
	lower_cases = False
	for x in word:
		if x.islower() and "." not in x:
			lower_cases = True
	return not lower_cases
	
alphabet = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliett", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"X-ray", "Y":"Yankee", "Z":"Zulu", "1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine", "0":"Zero", ".":"Decimal"}


new_ll = []
for x in ll:
	word_list = x.split()
	new_ll.append([])
	
	for y in range(len(word_list)):
		
		if convertible(word_list[y]):
		
			for z in range(len(word_list[y])):
				new_ll[-1].append(alphabet[word_list[y][z]])
				
		else:
			new_ll[-1].append(word_list[y])

for x in new_ll:
	print(" ".join(x))
			
