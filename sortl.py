#sort the list of strings based on their length
a=["school",'car','apple','hi']
a.sort(key=lambda x:len(x))
print(a)