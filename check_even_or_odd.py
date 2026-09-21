# Problem : check_even_or_odd 

# Method - 1 : Basic Approach

# n = int(input("Enter your Number: ")) 

# if n%2 == 0 : # % gives remainder & 0 means completely divided 
#     print("Even") 
# else:
#     print("Odd")

# Method - 2 : Functional Approach 

# def check_even_or_odd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
# result = check_even_or_odd(int(input("Enter your Number : ")))
# print(result)

# Method - 3 : oops 

class check_even_or_odd:
    def __init__(self,n):
        self.n = n 
    def checking_digits(self):
        if self.n % 2 == 0:
            return "Even"
        else:
            return "Odd"
        
obj = check_even_or_odd(int(input())) 
result = obj.checking_digits()
print(result)