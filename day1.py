#program to print 'yes' if a number divisible by 3 or end with 3 and 'no' for the else condition

N=int(input(" enter a number : "))
if N%3==0 or N%10==3:
    print("YES")
else:
    print("NO")

#swapping of two numbers

a=10
b=11
a=a^b
b=a^b
a=a^b
print(a,b)

#Find the negative of given number

n=6
print(-(~n))

#even or odd using bitwise operator

n=int(input("number : "))

if n&1==0:
    print("Even")
else:
    print("Odd")

#leap year

n=int(input(" year : "))
if n%400==0 or  (n%100!=0 and n%4==0):
    print("leap year")
else:
    print("not leap year")
