class calculator:
    def __init__(self,*args):
        self.numbers = args 
        
    def add(self):
        result = 0
        for num in self.numbers:
            result+=num
        return result
    
    def subtract(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = result - num 
        return result
    
    def multiple(self):
        result = 1
        for num in self.numbers:
            result = result * num 
        return result
    
    def division(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = result/num
        return result 
    
    def floor_division(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = result // num
        return result
    
    def exponential(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = result ** num 
        return result 

obj = calculator(2,3,3)
exponential = obj.exponential()
print(exponential)