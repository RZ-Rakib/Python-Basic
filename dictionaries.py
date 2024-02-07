# Basic example of dictionaries
studentInformation = {
    'Rakib' : 22,
    'Riyad' : 23,
    'Niloy' : 21
}

# Accessing values using keys
print(studentInformation['Rakib'])
print(studentInformation['Riyad'])

# Modifying the values
studentInformation['Rakib'] = 25
print(studentInformation['Rakib'])

# updating new key-value pairs 
studentInformation['Sayeed'] = 26
print(studentInformation['Sayeed'])




# Professional example of dictionaries
students = {
    'Rakib' : {'Math': 90, 'English' : 87, 'Bangla' : 95},
    'Riyad' : {'Math' : 92, 'English' : 85, 'Bangla' : 90},
    'Niloy' : {'Math' : 91, 'English' : 86, 'Bangla' : 89} 
}
# Acessing nested values
print(students['Rakib']['Math'])
print(students['Niloy']['English'])

# Updating new subject and grade for a student
students['Rakib']['Science'] = 96
print(students['Rakib']['Science'])

# Iterating through students and their grades
for students, grades in students.items():
    print(f"{students}'s grades: {grades}")