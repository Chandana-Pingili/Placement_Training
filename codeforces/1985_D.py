def print_coordinates(grid,r,c):
    min_i=r
    max_i=0
    min_j=c
    max_j=0
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='#':
                if i<min_i:
                    min_i=i
                if i>max_i:
                    max_i=i
                if j<min_j:
                    min_j=j
                if j>max_j:
                    max_j=j
    x_co=str((abs(max_i+min_i)//2)+1)
    y_co=str((abs(max_j+min_j)//2)+1)
    return " ".join((x_co,y_co))


n=int(input())
for i in range(n):
    r,c=map(int,input().split(" "))
    grid=[['-']*c]*r
    for i in range(r):
        for j in range(c):
            grid[i][j]=input()
    print(print_coordinates(grid,r,c))

