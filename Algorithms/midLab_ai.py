class Node:
    def __init__(self,node,cost,heur):
        self.node=node
        self.cost=cost
        self.heur=heur
#question 1
def aStar(graph, start, Cost, goal, heuristic):
    queue = [(heuristic[start] + Cost, Cost, start, [start])]
    while queue:
        queue.sort()
        heur, cost, node, path = queue.pop(0)
        if node == goal:
            print("Your cost from ", start, " to ", goal, " is", cost, "wih heuristic  ", heur, " with path ", path)
        for child, edgeCost in graph[node].items():
            hn = heuristic[child]
            gn = edgeCost + cost   
            queue.append((hn + gn, gn, child, path + [child]))

#question 2
def func(x):
    return -(x**4)/8 + (x**3)/2 + 2*(x**2) - 4*x + 5

def hillClimb(startVal=-2.0, step=0.1, minStep=0.0001):
    x = startVal
    fx = func(x)
    count = 0

    while step >= minStep:
        count += 1
        xImprove = x + step
        xWorsen = x - step

        fImprove = func(xImprove)
        fWorsen = func(xWorsen)

        if fImprove > fx or fWorsen > fx:
            
            if fImprove > fWorsen:
                x = xImprove
                fx = fImprove
                
            else:
                x = xWorsen
                fx = fWorsen
                
            step = step * (1+0.1)
        else:
            step = step * (1-0.2)

    print(f"\nFinal value for x = {x:.5f}")
    print(f"Final max value of f(x) = {fx:.5f}")
    print("No of iterations = ", count)

#mian part for Q1
graph = {
    'S':{'A':8,'H':4,'I':9},
    'A':{'B':5,'H':3},
    'B':{'C':6,'D':6,'H':9},
    'C':{'D':2,'F':7,'I':5,'H':1},
    'D':{'E':5,'F':2},
    'E':{'F':1,'G':4},
    'F':{'G':8},
    'G':{},
    'H':{'I':2},
    'I':{}
}
heurs={
    'S':10,
    'A':9,
    'B':7,
    'C':4,
    'D':3,
    'E':2,
    'F':4,
    'G':0,
    'H':6,
    'I':7
}


print("\nOutput for Q1 is as follows")
aStar(graph,'S',0,'G',heurs)  #Q1
print("\nOutput for Q2 is as follows")
hillClimb()                    #Q2