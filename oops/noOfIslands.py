def modify(grid,i,j,n,c=0):
    if i<0 or j<0 or i>=n or j>=n:
        return c
    c+=1
    if grid[i][j]==1:
        grid[i][j]=2
        c+=modify(grid,i,j-1,n)+modify(grid,i,j+1,n)+modify(grid,i-1,j,n)+modify(grid,i+1,j,n)
    return c
def noOfIslands(grid,n):
    c=0
    max_area=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                c+=1
                area=modify(grid,i,j,n)
                if area>max_area:
                    max_area=area
    return c,area

grid=[[0,1,0,0,1],
      [1,0,0,1,1],
      [0,0,0,0,0],
      [1,0,0,0,0],
      [1,0,0,0,1]]
n=5
print(noOfIslands(grid,n))