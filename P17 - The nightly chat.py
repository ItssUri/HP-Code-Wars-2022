def pasGMT(h, dif):
    o = h-dif
    if o<0:
        o = o+24
    return o%24

    
#Entrada
e=input().split(":")
he=int(e[0])
me=int(e[1])

#Sortida
s=input().split(":")
hs=int(s[0])
ms=int(s[1])

#Hora Madrid
heMadrid=pasGMT(he,1)
hsMadrid=pasGMT(hs,1)
if hsMadrid < heMadrid:
   hsMadrid += 24

print(f'He madrid;{heMadrid}: {me}')
print(f'Hs madrid;{hsMadrid}: {ms}')
   

#Hora Moscu
heMoscu=pasGMT(he,3)
hsMoscu=pasGMT(hs,3)
if hsMoscu < heMoscu:
   hsMoscu += 24 
print(f'He Moscu;{heMoscu}: {me}')
print(f'Hs Moscu;{hsMoscu}: {ms}')



#Hora Tokio
heTokio=pasGMT(he,9)
hsTokio=pasGMT(hs,9)
if hsTokio < heTokio:
   hsTokio += 24

print(f'He Tokio;{heTokio}: {me}')
print(f'Hs Tokio;{hsTokio}: {ms}')


horaFinalEntrada = max(heMadrid,heMoscu,heTokio)
horaFinalSortida = min(hsMadrid,hsMoscu,hsTokio)

print(f'horaFinalEntrada: {horaFinalEntrada}')
print(f'horaFinalSortida: {horaFinalSortida}')

if horaFinalEntrada*60+me < horaFinalSortida*60+ms:
    print(f'{horaFinalEntrada%24:02d}:{me:02d} to {horaFinalSortida%24:02d}:{ms:02d} GMT')
else:
    print('CANNOT FIND A SLOT')
   




