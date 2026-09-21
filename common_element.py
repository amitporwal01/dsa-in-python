# Problem : Find the common elements in two lists 

# Method-1 : Basic Approach

# a = ['a','b','c',]
# b = ['d','a','b']
# result = []
# set1 = set(a)
# set2 = set(b)


# print(set1 & set2)

# for i in a:
#     if i in b:
#         result.append(i)
# print(result)

# Method - 2 Funtional approach

# def common_element(a,b):
#     result = []
#     for i in a:
#         if i in b:
#             result.append(i)
#     return result 

# a = ['a','b','c',]
# b = ['d','a','b']
# answer = common_element(a,b)
# print(answer)

# Method-3 oops 

class common_element:
    def __init__(self,a,b):
        self.a = a
        self.b = b 
    def intersection(self):
        result = []
        for i in self.a:
            if i in self.b:
                result.append(i)
        return result 
obj = common_element(['a','b','c'],['d','a','b'])
answer = obj.intersection()
print(answer)

