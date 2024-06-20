n=int(input())
event=list(map(int,input().split(" ")))
crime_count=0
police_count=0
 
for event in event:
    if event==-1:
        if police_count>0:
            police_count-=1
        else:
            crime_count+=1
    else:
        police_count+=event
print(crime_count)