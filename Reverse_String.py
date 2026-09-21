# Problem: Reverse a String 

# Method-1 : Basic Approach

# n = input("Enter your String :")

# reverse_string = n[::-1]
# print(reverse_string)

# Method-2 : functional approach 

# def reverse_string(n):
#     reverse = n[::-1]
#     return reverse
# result = reverse_string(input("Enter your String :"))
# print(result)

# Method - 3 : oops

class reverse_string:
    def __init__(self,n):
        self.n = n 
        
    def reversed(self): 
        output = self.n[::-1]
        return output

obj = reverse_string(input("Enter your String : "))
result = obj.reversed()
print(result)