


number = 3113

num = number
result = 0

while num > 0:
    digits = num % 10
    result = result * 10 + digits
    print("The digits in the number are:", digits)
    num = num // 10

if result == number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")