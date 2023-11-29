"""
Q1. Create a BankAccount class with private attributes for balance and account number.
    Include methods for deposit, withdrawal, and displaying the account information.
"""

class BankAccoun:
    def __init__(self, balance, account_n):
        self.__balance = balance
        self.__account_n = account_n
    
    def get_balance(self):
        return self.__balance
    
    def get_account_n(self):
        return self.__account_n    

    def set_balance(self, new_balance):
        self.__balance= new_balance
    
    def set_account_n(self, new_acc_n):
        self.__account_n = new_acc_n

    def withdrawal(self, amount):
        self.__balance = (self.__balance - amount)
        print(f"{amount} OR withdrawen saccesfully")
        
    def diposit(self, amount):
        self.__balance = (self.__balance + amount)
        print(f"{amount} OR diposited saccesfully")
    
    def display(self):
        print(f"Account number : {self.__account_n} || Balance = {self.__balance}\n")
        
print("Q1: before error handling:")        
o = BankAccoun(1000, 12966005)
o.display()
o.withdrawal(60000)
o.withdrawal(60)
o.display()
o.diposit(1000)
o.display()



"""
Q2. Modify one of the previous classes to include proper error handling.
    For example, handle cases where a negative value is passed as an argument
    or when trying to withdraw more money than the balance in a bank account
"""
class BankAccoun:
    def __init__(self, balance, account_n):
        self.__balance = balance
        self.__account_n = account_n
    
    def get_balance(self):
        return self.__balance
    
    def get_account_n(self):
        return self.__account_n    

    def set_balance(self, new_balance):
        self.__balance= new_balance
    
    def set_account_n(self, new_acc_n):
        self.__account_n = new_acc_n

    def withdrawal(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                  if self.__balance > amount:
                      self.__balance = (self.__balance - amount)
                      print(f"\n{amount} OR withdrawen saccesfully")
                      
                  else:
                      print("\nInsufficient balance")
            else:
                print("\nAmount cannot be < 0")
              
        except:
            print("/nInvalid input")
        
        
    def diposit(self, amount):
        try:
            amount = float(amount)
            if amount < 0:
                print("\nAmount cannot be < 0 ")
            else:
                self.__balance = (self.__balance + amount)
                print(f"\n{amount} OR diposited saccesfully") 
        except:
            print("\nInvalid input")
            
        
    
    def display(self):
        print(f"\nAccount number : {self.__account_n} || Balance = {self.__balance}\n")
        
print("____________________________")
print("Q1: after error handling:")        
o = BankAccoun(1000, 12966005)
o.display()
o.withdrawal(60000)
o.withdrawal(-6)
o.withdrawal(60)
o.display()
o.diposit(1000)
o.diposit(-100)
o.diposit("kk")
o.display()


"""
Q3. Create a Library class that contains a list of Book objects.
Include methods to add a book, display all books, and search for a book by title.
"""

class Library:
    
    def __init__(self):
        self.library = []
    
    def __str__(self):
        return self.library
    
    def add_book(self, title, author, copies):
        new_book = {}
        new_book["Title"] = title
        new_book["Author"] = author
        new_book["Copies"] = copies
        self.library.append(new_book)
        
    def remove_book(self, book_name):
        found = False
        for book_index in range(len(self.library)):
            remove_book = self.library[book_index]
            if book_name == remove_book["Title"]:
                found = True
                break
            
        if found:
            self.library.remove(remove_book)
            print(book_name, " was successfully removed")
        else:
            print("This book i not in the library")
         
        
    def display_books(self):
        print("\nThis library contins:")
        for book in self.library:
            print(f"{book['Title']} by {book['Author']} in {book['Copies']} copies")
        print()
          
    def search_for(self, book_title):
        found = False
        for book_index in range(len(self.library)):
            book = self.library[book_index]
            if book_title == book["Title"]:
                found = True
                break
            
        if found:    
            print(f"{book['Title']} Details\n--> Autor: {book['Author']}\n--> book: {book['Copies']}")
        else:
            print("This book is not in the library")
            
print("____________________________")
print("Q3: Library class")          
obj1 = Library()
print("CREATE A")
obj1.add_book("A", "shahad", 9)
print("CREATE B")
obj1.add_book("B", "Hajer", 4)
print("DISPLAY")
obj1.display_books()
print()
print("SEARCH FOR A")
obj1.search_for("A")
print("SEARCH FOR G")
obj1.search_for("G")
print()
print("REMOVE g")
obj1.remove_book("G")
print("REMOVE A")
obj1.remove_book("A")
print("DISPLAY")

obj1.display_books()




    
    



