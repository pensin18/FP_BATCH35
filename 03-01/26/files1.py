# data = 'goog=100'

# file1 = open('data.txt','w')
# file1.write(data)
# file1.close()

# f2 = open(r'C:\Users\75PEN\FP_BATCH35\28-12\25\data2.txt','r')
# d = f2.read()
# print(d)
# f2.close()

# f3 = open(r'C:\Users\75PEN\FP_BATCH35\28-12\25\data2.txt','a')
# f3.write('\nmsft=200')
# f3.close()

try:
    print('this is algo trading')
    num1 = int(input('enter num1: '))
    num2 = int(input('enter num2: '))
    res = num1 / num2   
    print('result is:', res)
except:
     
    print('denominator cant be zero')


print('end of the program')    

try:
    print('this is algo trading')
    num1 = int(input('enter num1: '))
    num2 = int(input('enter num2: '))
    res = num1 / num2   
    print('result is:', res)
except Exception as e:
    print(e)
     
    print('denominator cant be zero')


print('end of the program') 