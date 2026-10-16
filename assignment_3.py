# write a program that takes two number and print:
# their sum diff and product
# whether the first no is greater than second

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))

sum=num1+num2
diff=num1-num2
product=num1/num2
print(sum,diff,product)

print("Is first number greater than second?", num1 > num2)