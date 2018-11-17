# simple list of numbers

list_of_numbers = [2,4,6,8,10,12]

print("this is our list of numbers: " + str(list_of_numbers))
print("and the 3rd number is: " + str(list_of_numbers[2]))

# alter the number inside the list

list_of_numbers[2] = 66
print("this is our new list of numbers (6 modified to 66): " + str(list_of_numbers))


# add items to the list

list_of_numbers = list_of_numbers + [14,16]
list_of_numbers.append(18)

print("this is our new list of numbers (items added): " + str(list_of_numbers))

# a trick to remove items

list_of_numbers[1:3] = []

print("this is our new list of numbers (items removed): " + str(list_of_numbers))
