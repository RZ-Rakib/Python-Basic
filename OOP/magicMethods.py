# __init__() is a common magic methods in python, there are several magic methods. check it

#super class
class Car:
    def __init__(self, model, year, color) -> None: # __init__() is a magic method
        self.model = model
        self.color= color
        self.year = year
    
    def __eq__(self, others: object) -> bool: # create compareing method useing __eq__() magic method to check the values of different objects
        return self.model == others.model and self.color == others.color and self.year == others.year
    
    def __str__(self) -> str: # this magic method will provide the values of a object without calling different methods
        return f"Model name: {self.model}\nModel year: {self.year}\nColor: {self.color}"
    
    def display(self):
        return(f"Model name: {self.model}\nModel year: {self.year}\nColor: {self.color}")
    
# Create instance of super class (object)
car1_instance = Car("Volvo", "2020", "White")
car2_instance = Car("BMW", "2021", "Black")

# comparing the values of two objects
print(car1_instance == car2_instance) # false

# call the object without mentioning method
print(car1_instance) # 

# normal call to the object with method
print(car2_instance.display())