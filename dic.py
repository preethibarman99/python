#dictionary
d=dict()
b="mysore is the beautiful city mysore"
l=b.split()
for i in l:
    if i not in d:
        d[i]=0
    d[i]+=1
print (d)
