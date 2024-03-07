class Phone: # super class
    def __init__(self) -> None:
        print("I am from phone class.")

class Iphone(Phone): # inherited super class
    def __init__(self) -> None: # overriding the super class features
        super().__init__() # calling the super class
        print("I am from Iphone class.") # add new feature

i = Iphone()