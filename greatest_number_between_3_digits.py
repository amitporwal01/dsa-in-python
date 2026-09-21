# Problem : greatest number between 3 digits

# Method-1 -> Basic Approach
# a,b,c = map(int,input().split(","))

# if a>=b and a>=c:
#     print(a,"a  the greatest")
# elif b>=a and b>=c:
#     print(b,"b  the greatest")
# else:
#     print(c,"c  the greatest")
    
# Method-2 -> Functions Approach

# def greatest(a,b,c):
#     if a>=b and a>=c:
#         return a 
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c 
# a,b,c = map(int, input().split(","))
# result = greatest(a,b,c)
# print(result)

# Method-3 -> oops Approach

class greatest:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def greater_number(self):
        if self.a >= self.b and self.a >= self.c:
            return self.a 
        elif self.b >= self.a and self.b >= self.c:
            return self.b 
        else:
            return self.c 
a,b,c = map(int,input().split(","))
obj = greatest(a,b,c)
result = obj.greater_number()
print(result)