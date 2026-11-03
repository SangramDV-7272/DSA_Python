

# extract digits from a string using a loop
y = 3110
x = y
print("The digits in the number are:")
while x > 0:
    d = x % 10
    print(d)
    x = x // 10

