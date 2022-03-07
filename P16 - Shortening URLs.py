#llegir paraula
number = int(input())

#defincio de l'alfabet
alfabet = [chr(ord('a')+i) for i in range(26)] + [chr(ord('A')+i) for i in range(26)] + [chr(ord('0')+i) for i in range(10)]

#anar treient caràcters base 62
result = ''
while number > 0 or len(result)==0:
    r, number = number % 62, number // 62
    result = alfabet[r] + result    

#escriure reslutat
print(result)
