# problem 2 : Factorial

# Method 1 -> Basic Approach

# n = int(input()) # factorial needed at what number

# factorial = 1 # default factorial will be 1, we will calculate & store factorial of a number

# if n == 0:
#     print(1)
# else:
#     for num in range(1,n+1):
#         factorial = factorial * num
#     print(factorial)

# Method 2 -> Functions Approach

# def factorial(n):
#     result = 1
#     if n==0:
#         return 1
#     else:
#         for num in range(1,n+1):
#             result = result * num
#         return result 
   
# answer = factorial(int(input()) )
# print(answer)

# Method 3 -> oops

class factorial:
    def __init__(self,n):
        self.n = n 
        
    def calculate(self):
        result = 1 
        if self.n == 0:
            return 1
        else:
            for num in range(1,self.n+1):
                result = result * num
            return result
obj1 = factorial(int(input()))
answer = obj1.calculate()
print(answer)
    