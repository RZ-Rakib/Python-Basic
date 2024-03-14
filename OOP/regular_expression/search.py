import re

pattern = r'RZ' # Define a regular expression pattern to search for words
text= "My name is RZ Rakib, I am from Bangladesh." # Define a simple text string

match = re.search(pattern,text) # searching for the pattern in text

if match:
    print(f"Found:", match.group())
else:
    print(f"Not found")