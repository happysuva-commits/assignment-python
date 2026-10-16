#program that takes total bill amount and number of friends as input calculate how much each person will pay 
#also print data type of each variable used


# Take bill amount and number of friends as input
bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

# Calculate each person's share
each_person = bill / friends

# Print the result
print("Each person will pay:", each_person)

# Print data types
print("Type of bill:", type(bill))
print("Type of friends:", type(friends))
print("Type of each_person:", type(each_person))
