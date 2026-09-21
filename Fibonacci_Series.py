# Problem : Fibonacci Series 

# Method - 1 : Basic Approach 

# n = 10 
# a = 0
# b = 1

# for i in range(n):
#     print(a, end = " ")
#     a,b = b,a+b

# Method - 2 : Funtional approach 

# def fibonacci_series(n,a,b):
#     for i in range(n):
#         print(a, end = " ")
#         a,b = b,a+b
# fibonacci_series(5,0,1)

# Method - 3 : oops

class Fibonacci_Series:
    def __init__(self,n,a,b):
        self.a = a
        self.b = b
        self.n = n
    def print_series(self):
        for i in range(self.n):
            print(self.a, end = " ")
            self.a,self.b = self.b,self.a+self.b
obj = Fibonacci_Series(int(input("Enter your Number :")),0,1)
obj.print_series()



