team1 , team2 = input().split(" -")
team2 = team2[1::]
team1score = 0
team2score = 0
end = 0
while end != 3:
    result = input().split("-")
    if int(result[0]) > int(result[1]):
        team1score +=1
    elif int(result[0]) < int(result[1]):
        team2score +=1
    if end == 1 and team1score == team2score +2 or end == 1 and team2score == team1score +2:
        break
    else:
        end+=1
winner = ""
if team1score > team2score:
    winner = team1
else:
    winner = team2
print(f"{winner} won the match {team1score} - {team2score}.")
