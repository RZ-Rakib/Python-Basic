names = ['Rakib', 'Riyad', 'Niloy', 'Sayeed', 'Sumon']

print(names) #print the list
print(names[0]) # print the first index
print(names[3: ]) # print the list from 4th-last
print(names[-1]) # reverse the list
print("Riyad" in names) # check the word in list 
print("Rafi" in names) # check the word in list
print(names + ["Rasel", "Ashik"]) # add two new items in the list

languages = ["python", "c++", "c", "java"]
print(f'Total length is {len(languages)}') # print the total length of list

languages.append("javascript") # append one new item and by default it will add end of the list
print(languages)

languages.insert(2, "ruby") # insert a new item in a specific place
print(languages)

languages.remove("python") # remove an item from the list
print(languages)

languages.sort() # sort the list as alphabetically
print(languages)

languages.reverse() # reverse the list as alphabetically
print(languages)

languages.pop() # pop the last item from the list
print(languages)

newLanguages = languages.copy() # copy the list
print(newLanguages)

position = languages.index("java") # check the index number of a word in list
print(position) 

total = languages.count("c++") # count a specific word in the list
print(total)