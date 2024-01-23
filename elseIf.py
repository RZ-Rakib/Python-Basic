mark = float(input("What is your mark? "))

if mark > 100:
    print("Undefined.")
elif mark >= 80 and mark <= 100:
    print("Your grade is A+.")
elif mark >= 70 and mark <= 79:
    print("Your grade is A.")
elif mark >= 60 and mark <= 69:
    print("Your grade is A-.")
elif mark >= 50 and mark <= 59:
    print("Your grade is B.")
elif mark >= 40 and mark <= 49:
    print("Your grade is B-.")
elif mark >= 33 and mark <= 39:
    print("Your grade is C.")
else:
    print("Your grade is fail.")
