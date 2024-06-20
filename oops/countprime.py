class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class DLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def addBack(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail.next.previous=self.tail
            self.tail=self.tail.next
    def isprime(self,n,i=2):
        if n<2:
            return False
        if n==2 or n==3:
            return True
        if n%i==0:
            return False
        if i*i>n:
            return True
        return self.isprime(n,i+1)
        
    def countprime(self,head,c=0):
        if head is None:
            return c
        if self.isprime(head.data):
            c+=1
        return self.countprime(head.next,c)
s=list(map(int,input().split(",")))
d=DLL()
for num in s:
    d.addBack(num)
print(d.countprime(d.head))