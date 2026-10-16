its just a basic to scratch python program beginner to pro

**print
print() is used to show output on the screen.

**variable
A variable is like a box that stores a value.

**input
input() allows the user to enter information.
Important: input() returns text (str), even if the user enters a number.

** comments
Comments are notes for humans. Python ignores them when running the program.

***** Basic data types
Type	Meaning	Example
-str	Text	"Happy"
-int	Whole number	25
-float	Decimal number	99.5
-bool	True or False	True
-list	Collection of values	[10, 20, 30]
-tuple	Fixed collection	(10, 20, 30)
-dict	Key-value pairs	{"name": "Happy"}
-set	Unique values	{1, 2, 3}
-You can check a variable's type using type():

**Arithmetic operators
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 floor division
print(a % b)   # 1 reminder
print(a ** b)  # 1000 power

**Comparison operators
a = 10
b = 5

print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a != b)  # True
print(a >= b)  # True
print(a <= b)  # False
Remember: = assigns a value, but == compares two values.

**Logical operators
age = 25

print(age > 18 and age < 30)  # True
print(age < 18 or age > 20)   # True
print(not age > 18)           # False

and: Both conditions must be true.
or: At least one condition must be true.
not: Reverses True/False.

**Assignment operators
score = 10
score += 5
print(score)  # 15

score *= 2
print(score)  # 30


** if / elif / else su chhe?
- if — jo condition True hoy to code run kare.
- elif — pehli condition False hoy to biji condition check kare.
- else — badhi conditions False hoy to run kare.

  
** Comparison operators
Operator	Meaning	Example
>	Greater than	80 > 35 → True
<	Less than	20 < 35 → True
>=	Greater than or equal	35 >= 35 → True
==	Equal to	50 == 50 → True
!=	Not equal	40 != 50 → True


** Logical operators
- and — banne conditions True hovi joie.
- or — koi ek condition True hoy to chale.
- not — True ne False ane False ne True kare.

**Build a Marks Pass/Fail Program
Rules:
- Marks 0 thi 100 vachche hova joie.
- Marks 35 ke vadhu hoy to Pass.
- 35 karta ochha hoy to Fail.
- Invalid marks hoy to Invalid input.


marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 35:
    print("Pass")

else:
    print("Fail")
