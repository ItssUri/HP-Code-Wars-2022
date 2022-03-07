sr = input()
ranks = ["Admiral", "Captain", "Commander", "Lieutenant", "Officer"]
if sr == "S":
    total = []
    for i in range(0, 6):
        total.append(input())
    if total[1] in ranks and total[3] in ranks:
        if ranks.index(total[1]) < ranks.index(total[3]):
            print("URGENT", end=",")
        for j in total:
            if total[-1] != j:
                print(j, end=",")
            else:
                print(j)
    else:
        print("Invalid input.")
elif sr == "R":
    total = input().split(",")
    if total[1] in ranks and total[3] in ranks:
        if ranks.index(total[1]) < ranks.index(total[3]):
            print("<<< URGENT >>>")
        print("From: " + total[0])
        print("From rank: " + total[1])
        print("To: " + total[2])
        print("To rank: " + total[3])
        print("Content: " + total[4])
        print("Timestamp: " + total[5])
    else:
        print("Invalid input.")
else:
    print("Invalid input.")
