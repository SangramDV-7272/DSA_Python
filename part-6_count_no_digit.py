

# part 1

x = 3110
y = x
count = 0
while y > 0:
    y = y // 10
    count += 1
print("The number of digits in the number are:", count, "\n")

# part 2
import math
print("The number of digits in the number are using log10:", int(math.log10(x)+1))

