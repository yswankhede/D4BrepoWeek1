num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# print results
print("Sum is:", num1 + num2)
# difference, product, etc.
dif= num1-num2
print("difference is:",dif)

product= num1 * num2
print("product is:", product)

if num2 != 0:
    print( "Quotient ", num1/num2)
else:
    print("can not devide by zero")