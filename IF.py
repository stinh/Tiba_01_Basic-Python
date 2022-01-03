# age=int(input("你幾歲?"))
# money=int(input("你有多少錢?"))
customer=input("你幾歲? 有多少錢?")
# age,money = int(customer.split())
age,money = map(int, customer.split())
print(str(age+money))

age,money = customer.split()
age=int(age)
money=int(money)
if age >= 18:
    print("歡迎光臨")
elif money>=20000:
    print("歡迎光臨")
else:
    print("謝謝惠顧")




#================================
import random

key_word = ['剪刀', '石頭', '布']

user = int(input('[0]剪刀, [1]石頭, [2]布:'))

rand_num = random.randint(0, 2)

print('你出了: ', key_word[user])
print('電腦出了: ', key_word[rand_num])

while x in range(10):
    if user is rand_num:
        print("平手")
    elif user == (rand_num+1)%3:
        print("你贏了")
    else:
        print("電腦贏了")