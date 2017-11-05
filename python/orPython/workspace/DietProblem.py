'''
    최소의 비용으로 다이어트 음식 제공
    Min z = 50x1 + 20x2 + 30x3 + 80x4
    1. Calories 500 <= 400x1 + 200x2 +150x3 + 500x4
    2. C    6 <= 3x1 + 2x2
    3. S    10 <= 2x1 + 2x2 + 4x3 + 4x4
    4. Fat  8 <= 2x1 + 4x2 + x3 + 5x4
'''

from gurobipy import *
try :
    m = Model("diet_problem")

    x1 = m.addVar(name="brownie")
    x2 = m.addVar(name="icecream")
    x3 = m.addVar(name="cola")
    x4 = m.addVar(name="pineapple")

    m.update()

    m.setObjective(50 * x1 + 20 * x2 + 30 * x3 + 80 * x4, GRB.MINIMIZE)

    m.addConstr(400 * x1 + 200 * x2 + 150 * x3 + 500 * x4 >= 500, "c0")
    m.addConstr(3 * x1 + 2 * x2 >= 6, "c1")
    m.addConstr(2 * x1 + 2 * x2 + 4 * x3 + 4 * x4 >= 10, "c2")
    m.addConstr(2 * x1 + 4 * x2 + x3 + 5 * x4 >= 8, "c3")

    m.optimize()

    for v in m.getVars():
        print(v.varName, v.x)

    print("ObjVal : ", m.objVal)

except GurobiError:
    print("Error repoted")
