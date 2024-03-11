# inheritance is a method to use features from parent/super class to child/sub class

# parent / super class
class Phone:
    def call(self):
        print(f"You can call")

    def message(self):
        print(f"You can message")

# child / sub class
class Iphone(Phone): # it will provide inherited features from super class.
    def photo(self):
        print(f"You can capture photos")

i = Iphone()
i.call()
i.message()
i.photo()

print(issubclass(Iphone, Phone)) # to check is Iphone is a sub class of Phone or not?