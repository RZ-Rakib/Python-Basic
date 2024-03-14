import re

pattern = r'RZ' # Define a regular expression pattern to search for words
text= "My name is RZ Rakib, I am from Bangladesh." # Define a simple text string

match = re.match(pattern,text) # searching for matchthe pattern in text

if match:
    print(f"Found:", match.group())
else:
    print(f"Not found") # output should be not found bcz match function find letter from index 0