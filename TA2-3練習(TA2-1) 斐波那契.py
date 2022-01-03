# 起始條件，第一個數字為0，第二個數字為1，後面的數字為前面兩個數字的相加
# 輸入唯一個數字i，請試試看印出指定數字的(以人類的索引直)第i個數字是多少
import sys
a = int(sys.stdin.read())
# a 代表人判讀位數
# a = int(input("請輸入一個數字:"))-1
n1 = 0
n2 = 1

if a-1==0: #a-1代表電腦判讀位數
    print(0)

elif a-1==1:
    print(1)

else:
    i = 0

    while i < a-1: 
        n1=n1, n2=n2, n1+n2
        i+=1

    print(n1)