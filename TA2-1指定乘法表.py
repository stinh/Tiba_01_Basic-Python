import sys
a=sys.stdin.read()

b=int(a.split()[0])
c=int(a.split()[1])

i=0
while i<b:
    j=0
    while j<c:    
        print(f'{i+1}x{j+1}={(i+1)*(j+1)}')
        j+=1
    i+=1