# lambda parameter : expression
#1
print(f'Result of (A + b)^2 : {(lambda a, b : a**2 + 2*a*b + b**2) (2,3)}')

#2
a = (lambda a, b : a**2 + 2*a*b + b**2) (5,6)
print(f'Result of (A + b)^2 : {a}')

#3
anotherWay = lambda a, b : a**2 + 2*a*b + b**2

anotherResult = anotherWay(4,5)
print(f'Result of (A + b)^2 : {anotherResult}')
