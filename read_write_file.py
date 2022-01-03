# f = open('file.txt' , 'r')

# print(f.read())

# f.close()

# =================================

# with open('file.txt' , 'r') as f:
#    print(f.read())



# =================================

with open('file.txt' , 'w', encoding='utf-8') as f:
   #print(f.read())
   f.write('Today is a good day')