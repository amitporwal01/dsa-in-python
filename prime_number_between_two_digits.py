# problem 2 : prime_number_between_two_digits

# Method 1 -> Basic Approach

# start, end = map(int, input("enter your number :").split(","))

# for num in range(start,end+1):
#     is_prime = True 
#     for i in range(2,num):
#         if num%i==0:
#             is_prime = False
#             break
#     if is_prime and num>1:
#         print(num)

# Method 2 -> Functions Approach


# def prime_number(start,end):
#     lst = []
#     for num in range(start,end+1):
        
#         is_prime =True 
#         for i in range(2,num):
#             if num%i==0:
#                 is_prime = False
#                 break
#         if is_prime:
#             lst.append(num)
#     return lst 
# print(prime_number(10,30))

# Method 3 -> oops

class PrimeNumber:
    def __init__(self,start,end):
        self.start = start 
        self.end = end 
    
    def find_primes(self):
        lst = []
        for num in range(self.start,self.end+1):
            is_prime = True 
            for i in range(2,num):
                if num%i==0:
                    is_prime = False 
                    break 
            if is_prime:
                lst.append(num)
        return lst 
obj = PrimeNumber(10,30)
answer = obj.find_primes()
print(answer)
