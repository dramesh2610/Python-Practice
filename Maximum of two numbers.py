# Python program to find the
# maximum of two numbers Method 1

def maximum (a,b):
    if a >= b:
        return a
    else:
        return b
# Driver code
a = 2
b = 4
print(maximum(a, b))

# maximum of two numbers Method 2
a = 2
b = 6
print(max(a,b))

# maximum of two numbers Method 3
a = 2
b = 7
# Use of ternary operator
print(a if a >= b else b)

# maximum of two numbers Method 4
a = 2
b = 10
maximum = lambda a,b: a if a>= b else b
print(f'{maximum(a,b)} is a maximum number')
