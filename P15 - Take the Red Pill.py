a = int(input())
grid = []
for h in range(a):
    a = input().split()
    for i in range(len(a)):
        a[i-1] = int(a[i-1])
    grid.append(a)
minimum_same = None
min_row_pos = []
for j in grid:
    minimum = None
    for k in range(len(j)):
        try:
            if j[k] <= minimum:
                if minimum != j[k]:
                    minimum = j[k]
                    minimum_pos = k
                else:
                    minimum_same = j[k]
        except:
            minimum = j[k]
            minimum_pos = k

    try:
        if minimum_same == minimum:
            continue
        if minimum_same != minimum:
            min_row_pos.append([minimum, minimum_pos])            
    except:
        min_row_pos.append([minimum, minimum_pos])


mentioned = False
saddle_points = 0
saddle_points_list = []
for m in min_row_pos:
    column_to_look = m[1]
    column = []
    for n in grid:
        column.append(n[column_to_look])
    maximum = None
    for o in column:
        try:
            if o > maximum:
                maximum = o
        except:
            maximum = o
    if maximum == m[0]:
        saddle_points += 1
        saddle_points_list.append(maximum)
if saddle_points != 1:
    print("No saddle point in the matrix")
if saddle_points == 1:
    print("The saddle point is "+str(saddle_points_list[0]))
