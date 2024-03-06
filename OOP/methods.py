class Country:
    capitalCity = ""
    continent = ""
# methods
    def setValue(self, nCapitalCity, nContinent): # self is a convention used as the first parameter in the method of a class
        self.capitalCity = nCapitalCity
        self.continent = nContinent

    def displayMsg(self):
        print(f"Details:\n\tCapital city: {self.capitalCity}\n\tContinent: {self.continent}")

Bangladesh = Country()
print(isinstance(Bangladesh, Country)) # Check if Bangladesh is an instance of the Country class 
Bangladesh.setValue("Dhaka", "Asia")
Bangladesh.displayMsg()


Finland = Country()
print(isinstance(Finland, Country)) # Check if Finland is an instance of the Country class 
Finland.setValue("Helsinki", "Europe")
Finland.displayMsg()
