import sys
a=sys.stdin.read()
b=a.split()

i=0
while i < len(b):
    c=int(b[i])+1
    i+=1
    print(str(c),end=' ')