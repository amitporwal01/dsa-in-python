# Problem : Merge Two dictionaries 

# Method 1 : Basic Approach

# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40} 

# for key in dict2:
#     dict1[key] = dict2[key]
# print(dict1)

# Method 2 : Functional Approach

# def merged_dict(dict1,dict2):
#     for key in dict2:
#         dict1[key] = dict2[key]
#     return dict1 

# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40} 

# result = merged_dict(dict1,dict2)
# print(result)   

# Method 3 : oops

class merged_dict:
    def __init__(self,dict1,dict2):
        self.dict1 = dict1
        self.dict2 = dict2 
        
    def check_dict(self):
        for key in self.dict2:
            self.dict1[key] = self.dict2[key]
        return self.dict1 
    
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40} 

obj = merged_dict(dict1,dict2)
result = obj.check_dict()
print(result)

