# take input in celsius and print its equivalent in 
#fahrenheit and kelvin (explict type conversion and arithmetic oprators)
# f=(c*9/5)+32
#kelvin=c+273.15


# Take temperature in Celsius
c = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
f = (c * 9 / 5) + 32

# Convert Celsius to Kelvin
kelvin = c + 273.15

# Print results
print("Temperature in Fahrenheit:", f)
print("Temperature in Kelvin:", kelvin)

# Print data types
print("Type of c:", type(c))
print("Type of f:", type(f))
print("Type of kelvin:", type(kelvin))
