#電腦出一1~100數字，給你猜，再從你猜的數字縮小範圍
import random
com = random.randint(1,100)
min = 1
max = 100
you = int(input(f'請輸入一個{min}到{max}間的數字:'))
print(com)
while True:
    if you == com:
        print('猜中囉')
        break
    else:
        if you < com:
            min = you
            you =int(input(f'請輸入一個{min}到{max}間的數字:'))
    
        else:
            max = you
            you = int(input(f'請輸入一個{min}到{max}間的數字:'))