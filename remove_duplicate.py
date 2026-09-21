# Problem : Remove Duplicate from a list 

# Method - 1 : Basic Approach

# numbers = [10,20,40,10,10,20,70,60,20,30,40,50]
# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(sorted(unique))
# print(unique)

# Method - 2 : Functional Approach

# def remove_duplicate(numbers):
#     unique = []
#     for num in numbers:
#         if num not in unique:
#             unique.append(num)
#             unique.sort()
#     return unique

# numbers = [10,20,40,10,10,20,70,60,20,30,40,50]
# result = remove_duplicate(numbers)
# print(result)

# Method - 3 : oops
class remove_duplicate:
    def __init__(self,numbers):
        self.numbers = numbers 
    def check_list(self):
        unique = []
        for num in self.numbers:
            if num not in unique:
                unique.append(num)
                unique.sort()
        return unique 
numbers = [10,20,40,10,10,20,70,60,20,30,40,50]
obj = remove_duplicate(numbers)
result = obj.check_list()
print(result)    
    
