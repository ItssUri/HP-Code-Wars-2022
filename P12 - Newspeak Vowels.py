#llegir paraula
word = input()

#diu si es vocal
def esVocal(pos,paraula):
    if pos < 0 or pos >= len(paraula):
        return False
    return paraula[pos].upper() in 'AEIOU'

def gira(pos, paraula):
    return paraula[:i]+paraula[i+1]+paraula[i]+paraula[i+2:]

#busquem la psocio de dues vocals seguides
for i in range(len(word)):
    if not esVocal(i-1,word) and esVocal(i,word) and esVocal(i+1,word) and not esVocal(i+2,word):
       word = gira(i,word) 
        
#escriu resultat
print(word)

