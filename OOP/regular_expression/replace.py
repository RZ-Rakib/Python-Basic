import re

pattern = r'\d+'
string = 'The price of the book is $20, the price of the pen is $5'
replace = "20"

modified_new_string = re.sub(pattern,replace, string)
print(f"Modified string is {modified_new_string}")

