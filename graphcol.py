m = int(input("enter the number of MAX colors: "))

g = {}
n = int(input("enter the number of Edges: "))

for i in range(n):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = []
    g[a].append(b)
    if b not in g:
        g[b] = []
    g[b].append(a)

print(g)

posCol = ["red", "orange", "violet", "indigo", "blue", "yellow", "green"]

def canColor(g, n, col, colList):
    for child in g[n]:
        if colList[child] == posCol[col]:
            return False
    return True

def graphColouring(g, m, v, n, colList):
    if n == v:
        return True
    
    for col in range(m):
        if canColor(g, n, col, colList):
            colList[n] = posCol[col]
            if graphColouring(g, m, v, n + 1, colList):
                return True
            colList[n] = -1  # Backtrack

    return False

# Initialize color list with -1 (meaning uncolored)
colList = {}
for i in g.keys():
    colList[i] = -1

if graphColouring(g, m, len(g.keys()), 0, colList):
    print(colList)
else:
    print(f"Can't color using {m} colors")




'''
ex. for printin graph

3
6
0 1
0 2 
0 3
1 2 
2 3 
3 4 

'''
