'''
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
'''
patt1 = int(input("what is the limit for row printing? "))

for row in range(1, patt1 + 1):
    for column in range(row):
        print(row, end= ' ')
    print('')

'''
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9 
'''
for row in range(1, patt1 + 1):
    for column in range(row):
        print((row * 2) - 1, end= ' ')
    print('')
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

patt2 = int(input("what is the limit for column printing? "))

for row in range(1, patt2 + 1 ):
    for column in range(1, row + 1):
        print(column, end=' ')
    print('')

'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
for row in range(patt2, 0, -1):
    for column in range(1, row, 1):
        print(column, end=' ')
    
    print('')


