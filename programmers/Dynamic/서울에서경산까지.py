travel=[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]
K=1650
time = 0
costs = []


#########최대로 표현 ##################
for i in range(len(travel)):
    cost = max(travel[i][1], travel[i][3])
    costs.append(cost)
    time += travel[i][travel[i].index(cost)- 1]


