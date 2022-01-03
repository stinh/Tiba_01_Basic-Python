import sys
a=sys.stdin.read()
time=0
sum=0
while time <=int(a):
    sum=sum+time
    time+=1
print(sum)