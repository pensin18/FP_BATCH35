import numpy as np

l1 = [1,2,3,4,5]
print(l1)
a1 =  np.array(l1,dtype = 'str')
print(a1)
print(type(a1))

l2 = np.ones(10,dtype = int)
print(l2)
l3 = np.zeros((3,4),dtype = float)
print(l3)
l4 = np.arange(1,20,2)
print(l4)

print(np.random.randint(1,100,10))

print(np.arange(1,10).reshape(3,3))
print(np.random.randint(1,50,25).reshape(5,5))
