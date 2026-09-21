# Problem : Length of list without using the len() fn 

# Method - 1 : Basic Approach

# lst = [2,5,6,3,2,5,2]
# count = 0

# for num in lst:
#     count+=1
# print(count)

# Method - 2 : Functional Approach

# def length(lst):
#     count = 0 
#     for num in lst:
#         count+=1
#     return count
# lst = [2,5,6,3,2,5,2]
# result = length(lst)
# print(result)

# Method - 3 : oops

class length:
    def __init__(self,lst):
        self.lst = lst 
    def check(self):
        count = 0
        for num in self.lst:
            count +=1
        return count 
    
lst = [2,5,6,3,2,5,2]
obj = length(lst)
result = obj.check()
print(result)