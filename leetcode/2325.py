def decodeMessage( key: str, message: str) -> str:
        ans=""
        d={}
        a=97
        
        for i in range(len(key)):
            if key[i] not in d.keys() and key[i]!=' ':
                d[key[i]]=chr(a)
                a+=1
        print(d)
        for char in message:
            if char!=" ":
                ans=ans+d[char]
            else:
                ans=ans+" "
        return ans
#key = "eljuxhpwnyrdgtqkviszcfmabo"
#message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(chr(97))
print(decodeMessage(key,message))