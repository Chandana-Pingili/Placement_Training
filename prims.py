def prims(graph,s):
    queue=[]
    visited=[s]
    msp=[]
    for i in graph[s]:
        queue.append((s,i[0],i[1]))
    
    queue.sort(key=lambda x:x[2])
    while queue:
        strt,end,c=queue.pop(0)
        if end not in visited:
            visited.append(end)
            msp.append((strt,end,c))
            for vertex in graph[end]:
                if vertex[0] not in visited:
                    queue.append((end,vertex[0],vertex[1]))
        
        queue.sort(key=lambda x:x[2])
    print(msp)
       

graph={5:[(8,2),(2,2),(3,2)],
       2:[(5,2),(3,1)],
       3:[(2,1),(5,2),(8,3),(7,3)],
       8:[(3,3),(5,2),(6,4)],
       6:[(8,4),(9,2)],
       7:[(3,3),(9,1)],
       9:[(7,1),(6,2)],
       4:[(9,2)]}
prims(graph,5)

