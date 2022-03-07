n = int(input())
t = int(input())
suma = n
a = ""
b=0
x = 0
for i in range(t):
    x=0
    for y in range(len(str(suma))):
        a=str(suma)
        b+=int(a[x])
        x+=1
    suma+=b
    b = 0
print(suma)
    
