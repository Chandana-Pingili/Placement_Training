def numberOfSpecialChars(self, word: str) -> int:
    count=0
    s=[]
    for char in word:
        if char.isupper() and char.lower() in word and char not in s:
            s.extend([char,char.upper()])
            count+=1
         
         
                
            