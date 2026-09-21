# Problem : count the occurances of each character in a string

# Method - 1 : Basic Approach

# text = 'Hello'
# count = {}

# for char in text:
#     if char in count:
#         count[char] = count[char]+1
#     else:
#         count[char] = 1
# print(count)

# Method - 2 : Functional Approach

# def count_occurances(text):
#     count = {}
#     for char in text:
#         if char in count:
#             count[char] = count[char]+1
#         else:
#             count[char] = 1
#     return count 

# result = count_occurances(input("enter your text: "))
# print(result)

# Method - 3 : oops

class count_occurances:
    def __init__(self,text):
        self.text = text 
        
    def check_result(self):
        count = {}
        for char in self.text:
            if char in count:
                count[char] = count[char]+1
            else:
                count[char] = 1
        return count
obj = count_occurances(input("enter your text: "))
result = obj.check_result()
print(result)