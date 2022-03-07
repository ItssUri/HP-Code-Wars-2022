n = int(input())
while n <= 0:
    n = int(input())

m = int(input())
while m <= 0:
    m = int(input())
o = int(input())
e = n/m
if n%m == o:
    print(f"CORRECT, the capacity of each box is", int(n/m))
else:
    print("INCORRECT")

    
    
