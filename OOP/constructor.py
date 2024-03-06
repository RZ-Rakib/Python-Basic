class Country:
    countryName = ""
    capitalCity = ""
    continent = ""
# methods
    def __init__(self, nCountryName, nCapitalCity, nContinent): # self is a convention used as the first parameter in the method of a class
        self.countryName = nCountryName
        self.capitalCity = nCapitalCity
        self.continent = nContinent

    def displayMsg(self):
        print(f"Details of {self.countryName}:\n\tCapital city: {self.capitalCity}\n\tContinent: {self.continent}")

Bangladesh = Country("Bangladesh", "Dhaka", "Asia")
print(isinstance(Bangladesh, Country)) # Check if Bangladesh is an instance of the Country class 
Bangladesh.displayMsg()


Finland = Country("Finland", "Helsinki", "Europe")
print(isinstance(Finland, Country)) # Check if Finland is an instance of the Country class 
Finland.displayMsg()