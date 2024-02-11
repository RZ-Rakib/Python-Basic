# Positional arguments
def showMessage(name, message):
    print(f'{name}, {message}.')

showMessage("Rakib", "Good affternoon")





# *Arbitrary positional arguments(args)
#           Example no 1
def student1(*details): # arbitrary returns output as a touple
        print(f'Here are the details: {", ".join(map(str,details))}') # for printing output in a single line,sperate elements and join with comma

student1('Rakib', 30, 'rakibzaman824@gmail.com')

#           Example no 2
def sum(*numbers):
    add = 0
    for number in numbers:
        add = add + number
    print(f'Sum is: {add}')
      
sum(12, 12, 12)




# **Arbitrary keyword argumenst(kwargs)
def student2(**details):
     print(details) # output as a touple

     for key, value in details.items():
        print(f'Here are the details: {key}: {value}')

student2(name = 'Rakib', age = 30, email = 'rakibzaman824"gmail.com')




# Combining Positional and Arbitrary Positional Arguments
def names(arg1, arg2, *extraArg):
    print(f'arg1: {arg1}')
    print(f'arg2: {arg2}')
    print(f'extra arg: ',extraArg) # output as touples

names(1, 'Apple', True, 'RZ')




# Combining Keyword and Arbitrary Keyword Arguments:
def colors(arg1, arg2, **extraArg):
    print(f'arg1: {arg1}')
    print(f'arg2: {arg2}')
    print(f'extra arg: ',extraArg) # output as touples

colors('Black', 'Olive', fvrt1 = 'Blue', fvrt2 = 'Green') #output as dictionaries



# Combining Positional, Arbitrary Positional, and Keyword Arguments
def colors(arg1, *addiArg, arg2 = 'default', **extraArg):
    print(f'arg1: {arg1}')
    print(f'Additional arg: {addiArg}')
    print(f'arg2: {arg2}') # default value will print due to not have a value in the function 
    print(f'extra arg: ',extraArg) # output as touples

colors('Black', True, 'Olive', fvrt1 = 'Blue', fvrt2 = 'Green') #output as dictionaries