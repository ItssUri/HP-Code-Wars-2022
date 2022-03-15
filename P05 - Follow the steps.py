coord=[]
x=0
y=0
n=int(input())
for i in range(n):
    ent=input().split(" ")
    coord.append(ent)
    
for e in coord:
    e[1]=int(e[1])
    e[0]=int(e[0])
    if e[1]>y:
        print("Walk",e[1]-y,"steps north")
    elif e[1]<y:
        print("Walk",y-e[1],"steps south")
    if e[0]>x:
        print("Walk",e[0]-x,"steps east")
    elif e[0]<x:
        print("Walk",x-e[0],"steps west")
    x=e[0]
    y=e[1]

