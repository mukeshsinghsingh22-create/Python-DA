#lambda Functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# The syntax of a lambda function is: lambda arguments : expression

x = lambda a : a + 10
print(x(5))
y = lambda a, b : a * b
print(y(5, 6))
z = lambda a, b, c : a + b + c
print(z(5, 6, 2))