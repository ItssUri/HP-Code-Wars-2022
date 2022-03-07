num = int(input())
result = 0
for i in range(num+1):
    for char in str(num):
        if char == "5":
            result+=1
    num-=1
print(result)
