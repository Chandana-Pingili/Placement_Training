def isArrayGood(n,nums):
    c=0
    for i in range(n):
        j=0
        s=sum(nums[:i])
        while j<=i:
            print(s,nums[:i+1],c,i,j)
            if s-nums[j]==0:
                
                c+=1
               
                break
            j+=1
    print(c)
isArrayGood(5,[0,1,2,1,4])