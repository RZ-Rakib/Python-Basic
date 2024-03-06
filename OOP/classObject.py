class Country:
    capitalCity = ""
    continent = ""

Bangladesh = Country()
print(isinstance(Bangladesh, Country)) # Check if Bangladesh is an instance of the Country class 
Bangladesh.capitalCity = "Dhaka"
Bangladesh.continent = "Asia"
print(f"Details of Bangladesh\n\tCapital city: {Bangladesh.capitalCity}\n\tContinent: {Bangladesh.continent}")

Finland = Country()
print(isinstance(Finland, Country)) # Check if Finland is an instance of the Country class 
Finland.capitalCity = "Helsinki"
Finland.continent = "Europe"
print(f"Details of BangladesFinland\n\tCapital city: {Finland.capitalCity}\n\tContinent: {Finland.continent}")
