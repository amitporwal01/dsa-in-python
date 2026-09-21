# Problem : Count the total number of vowels (a, e, i, o, u) 
# present in a given input string .

# Method -1 : Basic Approach 

# counter = 0 
# text = input("Enter your string :")

# for char in text:
#     if char.lower() in "aeiou":
#         counter+=1
# print(counter)

# Method-2 -> Functional Approach 

# def vowel_counter(n):
#     counter = 0 
#     for char in n:
#         if char.lower() in "aeiou":
#             counter+=1
#     return counter
# result = vowel_counter(input("Enter your String : ")) 
# print(result)

# Method-3 -> oops

class vowel:
    def __init__(self,n):
        self.n = n 
        
    def vowel_counter(self):
        counter = 0 
        for char in self.n:
            if char.lower() in "aeiou":
                counter +=1
        return counter 
obj = vowel(input("Enter your String: ")) 
result = obj.vowel_counter()
print(result)

