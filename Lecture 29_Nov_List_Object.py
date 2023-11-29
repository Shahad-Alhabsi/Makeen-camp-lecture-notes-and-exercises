class Numbers:
    def __init__(self):
        self.numbers = []
        
    def add_number(self, num):
        self.numbers.append(num)
    
    def remove_number(self, num):
        self.numbers.remove(num)
        
    def sum_numbers(self):
        sum_ = 0
        for i in self.numbers:
            sum_ += i
        return sum_
                     
                     
obj1 = Numbers()
obj1.add_number(1)
obj1.add_number(3)
obj1.add_number(5)
print(obj1.sum_numbers())