'''
    주어진 일에 최적의 비용으로 값을 찾는 것
'''
from gurobipy import *

days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', "Sun"]

assignment_FTE = [
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1, 1],
                    [1, 1, 1, 0, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1],
                ]
required_FTR = [17, 13, 15, 19, 14, 16, 11]

m = Model("post_office_problem")

day_assignment = []
for i in range(len(days)):
    # obj = 1 계수값을 의미 2x 
    day_assignment.append(m.addVar(obj=1, vtype=GRB.INTEGER, name="(%s)" %(days[i])))

m.modelSense = GRB.MINIMIZE
m.update()

for i in range(len(days)):
    m.addConstr(quicksum(assignment_FTE[i][c] * day_assignment[c] for c in range(len(days))) >= required_FTR[i], "day requirement %s" % days[i])

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print(m.getObjective().getValue())
