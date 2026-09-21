# Problem : Palindrome Check 

# Method -1 : Basic Approach

# n = input("Enter your String : ")

# if n == n[::-1]:
#     print("it is Palindrome")
# else:
#     print("its not a Palindrome")

# Method - 2 : Functional approach 

# def check_Palindrome(n):
    # if n == n[::-1]:
    #     return "it is Palindrome"
    # else:
    #     return "its not a Palindrome" 
# result = check_Palindrome(input("Enter your String :"))
# print(result)

# Method - 3 : oops

class check_palindrome:
    def __init__(self,n):
        self.n = n
    def checked_array(self):
        if self.n == self.n[::-1]:
            return "it is Palindrome"
        else:
            return "its not a Palindrome" 
obj = check_palindrome(input("Enter your String :"))
result = obj.checked_array()
print(result)        

        