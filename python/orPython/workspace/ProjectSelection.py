'''
    Project Selection
    - 현재 가지고 있는 정보를 바탕으로
      어떤 프로젝트에 어떤 리소스를 투입할 것인지를 결정하는 문제
    - 순현재가치(Net Present Value)를 활용하여 문제를 정의
    - 최초 투자 시기붙터 사업이 끝나는 시기까지의 이익을 환상하여 구함
'''
from gurobipy import *

investments_targets = ['i1', 'i2', 'i3', 'i4', 'i5']
expected_npv = [13,16, 16, 14, 39]

cash_outflow = [
                [11, 53, 5, 5, 29],
                [3, 6, 5, 1, 34]
                ]
cash_budget = [40, 20]

m = Model("project_selection")

invesestment_assignment = []
for i in range(len(investments_targets)):
    invesestment_assignment.append((m.addVar(vtype=GRB.CONTINUOUS, obj=expected_npv[i], name="(%s)" % (investments_targets[i]))))

m.modelSense = GRB.MAXIMIZE
m.update()

for time in range(len(cash_outflow)):
    m.addConstr(quicksum(cash_outflow[time][c] * invesestment_assignment[c] for c in range(len(investments_targets))) <= cash_budget[time], "day requirment %s" %investments_targets)

for index in range(len(investments_targets)):
    m.addConstr(invesestment_assignment[index] <= 1, "variable %s" %investments_targets[index])

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print(m.getObjective().getValue())
