'''find kth largest factor of given input n'''
def kthLargestFactor(num,k):
    factor=num
    for i in range(num,0,-1):
        if num%i==0:
            factor=i
            k-=1
            if k==0:
                return factor

print(kthLargestFactor(1,1))


    
