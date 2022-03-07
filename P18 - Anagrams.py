def isanagram(a,b):
    if len(a)!=len(b):
            return False
    for l in a:
        if b.count(l)!=a.count(l):
            return False
    return True

sortida=""
aword=str(input())
if aword.isupper()==True:
    exit()

lwords=str(input())
ar=lwords.split(" ")
for paraula in ar:
    if isanagram(aword,paraula) and (aword!=paraula):        
        sortida = sortida + paraula + " "
        

print(sortida.rstrip())

      
