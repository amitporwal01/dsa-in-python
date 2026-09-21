# problem 1 : sum of two numbers

# Method 1 -> Basic Approach

# a = 10
# b = 20

# result = a+b
# print(result)

# Method 2 -> Functions Approach

# def add(a,b):
#     return a+b 

# result = add(10,200)
# print(result)

# Method 3 -> oops

class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b 

obj1 = calculator(5,6)
result1 = obj1.add()
print('result1:', result1)


obj2 = calculator(50,60)
result2 = obj2.add()
print('result2:',result2)
    