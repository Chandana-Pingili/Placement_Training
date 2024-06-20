def dfs(graph,s):
    l.append(s)
    for i in graph[s]:
        if i not in l:
            dfs(graph,i)

def bfs(graph,s):
    visited=[]
    queue=[s]
    while queue:
        key=queue[0]
        for i in graph[key]:
            if i not in visited and i not in queue:
                queue.append(i)
        visited.append(key)
        queue.pop(0)
    return visited

def dijkstras(graph,s):
    visted=[]
    queue=[(0,s)]
    costfroms={k:float('inf') for k in graph.keys()}
    costfroms[s]=0
    while queue:
        c,cur=min(queue)
        for i in graph[cur]:
            if i[0] not in visted:
                cc=min(costfroms[i[0]],c+i[1])
                queue.append((cc,i[0]))
                if costfroms[i[0]]>cc:
                    costfroms[i[0]]=cc
        queue.remove((c,cur))
        visted.append(cur)
    print("costs to all vertices from ",s)
    print(costfroms)
            
def allPaths(graph,s,e,path):
    path=path+str(s)
    l.append(s)
    if s==e:
        print("->".join(path))
        l.pop()
        return 
    for i in graph[s]:
        if i[0] not in l:
            allPaths(graph,i[0],e,path)
    l.pop()

def costOfAllPaths(graph,s,e,path,c):
    path=path+str(s)
    l.append(s)
    if s==e:
        print("->".join(path),", cost : ",c)
        l.pop()
        return 
    for i in graph[s]:
        if i[0] not in l:
            costOfAllPaths(graph,i[0],e,path,c+i[1])
    l.pop()

def minCostPath(graph,s,e,path,c,min_c,min_path):
    path=path+str(s)
    l.append(s)
    if s==e:
        if c<min_c:
            min_c=c
            min_path=path
        l.pop()
        return (min_c,min_path)
    for i in graph[s]:
        if i[0] not in l:
            min_c,min_path=minCostPath(graph,i[0],e,path,c+i[1],min_c,min_path)
    l.pop()
    return (min_c,min_path)

def allPossiblePaths(graph,s):
    # path=path+str(s)
    # l.append(s)
    # for i in graph[s]:
    #     if i[0] not in l:
    #         allPossiblePaths(graph,i[0],path)
    # print(" ->".join(path))
    # l.pop()
    for node in graph.keys():
        min_c,min_path=minCostPath(graph,s,node,"",0,9999999,"")
        print(f"minimum cost path from {s} to {node} is {"->".join(min_path)} with minimum cost = {min_c}")

graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
# dfs(graph,5)
g={10:[(15,8),(5,2)],15:[(12,3),(10,8)],5:[(12,2),(10,2)],12:[(11,1),(9,2),(15,3),(5,2)],11:[(12,1)],9:[(12,2),(6,4)],6:[(9,4)]}
#print("DFS Traversal : ",l)
#print("BFS Traversal : ",bfs(graph``,6))
graph={5:[(7,2),(3,2)],7:[(5,2),(4,8),(3,3)],4:[(7,8),(8,4),(2,5)],8:[(3,1),(4,4),(2,4)],3:[(5,2),(7,3),(8,1)],2:[(4,5),(8,4)]}
dijkstras(g,10)
# l=[]
# allPaths(graph,5,2,"")
# l=[]
# costOfAllPaths(graph,5,2,"",0)
# l=[]
# min_c,min_path=minCostPath(graph,5,2,"",0,9999999,"")
# print(f"minimum cost path is {"->".join(min_path)} with minimum cost = {min_c}")
# allPossiblePaths(graph,5)