# Problem : count of number of digits from a number

# Method-1: Basic Approach

num = 2345124
count = 0
# Approach-1
# while num>0:
#     num = num  // 10 # this will do floor division / provide quotient
#     count = count+1
# print(count)

# Approach-2
# for i in str(num):
#     count = count+1
# print(count)

# Method-2: Functional Approach

# def count_digits(n):
#     count = 0
#     for i in str(n):
#         count+=1
#     return count

# result = count_digits(5563827543)
# print(result)

# Method-3: oops Approach 

class count_digits:
    def __init__(self,n):
        self.n = n 
    
    def total_count(self):
        count = 0 
        num = self.n
        while num > 0:
            num = num // 10 
            count+=1
        return count 

try:                                                   # Try to execute risky code
    obj = count_digits(int(input("Enter your number: ")))  # Convert user input to integer
    answer = obj.total_count()                         # Count the digits
    print(answer)                                      # Print the result
except ValueError:                                    # Runs when input cannot become an integer
    print("Invalid input! Please enter numbers only.") # Friendly error message
        
    