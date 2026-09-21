# Problem : Right-Angled Triangle Pattern in Python

# Method 1 : Basic Approach
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# n = int(input("Enter your number: ")) 

# for i in range(1,n+1):
#     print("*" *i , end = " ")
#     print()

# Method 2 : Functional Approach
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# def print_triange(n): 
#     for num in range(1,n+1,1):
#         print("*" *num , end = " ")
#         print()
        
# print_triange(10)


# Method 3 : oops
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

class triange:
    def __init__(self,n):
        self.n = n 
    def right_angled_triangle(self):
        for num in range(1,self.n+1,1):
            print("*" * num , sep = "")
            print()
obj = triange(int(input("Enter your digit: ")))
obj.right_angled_triangle()

        
        
    
