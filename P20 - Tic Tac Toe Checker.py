#llegir taluer
tauler = []
for x in range(3):
    tauler.append(list(input()))

def check(tauler):
    #comprova si és un resultat valid
    #numero X i O difereixen de mes d'1
    num = {'X': 0, 'O':0, '_':0 }

    for i in range(3):
        for j in range(3):
            num[tauler[i][j]] += 1
    
    if abs(num['X'] - num['O']) > 1:
        return 'NOT VALID'


    won = {'X': False, 'O': False}
    #comprova si hi ha algu que quanya
    for i in range(3):
        #comprovar horitzontal
         if all(tauler[i][0] == tauler[i][j] for j in range(3)):
             won[tauler[i][0]] = True
        #comprovar vertical
         if all(tauler[0][i] == tauler[j][i] for j in range(3)):
             won[tauler[0][i]] = True
             
    #comprovar diagonal 1
    if all(tauler[0][0] == tauler[i][i] for i in range(3)):
        won[tauler[0][0]] = True

    #comprovar diagonal 2
    if all(tauler[2][0] == tauler[2-i][i] for i in range(3)):
        won[tauler[2][0]] = True

    #determinar d'un guanyador
    #si mes d'un... resultat no valid
    if won['X'] and won['O']:
        return 'NOT VALID'
    elif won['X']:
        return 'X WON'
    elif won['O']:
        return 'O WON'
       
    #si totes les posicions estan plenes - empat
    if num['_'] == 0:
        return "IT'S A TIE"

    #si no
    return "PLAYING"
    
#escriu tauluer
print(check(tauler))


