s="dog"
l=[]
for i in range(len(s)):
    for j in range(len(s)):
        r=s[i:j+1]
        if r=='':
            pass
        else:
            l.append(s[i:j+1])
        
print(l)