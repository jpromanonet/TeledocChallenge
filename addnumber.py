# Take Home Exercise:

'''Implement a function that adds any two strings that each represent N arbitrarily large non-
negative numbers.'''


# Let's create a list from the strings
def addNumbers(firstString, secondString):
    # Let's convert the string parameters into list so every number separated by spaces becomes an index
    firstList = list(firstString.split(" "))
    secondList = list(secondString.split(" "))
    # Now lest measure the first list to use the index as reference with the other list index when adding numbers later
    length = len(firstList)
    # Here we iterate over the two lists
    for i in range(length):
        lists = [firstList, secondList]
        # Converting the list into string to find if there is any negative sign and raise an error if so
        if str(lists).find("-") != -1:
            raise ValueError("You're using a negative number and it's not allowed")
        it = iter(lists)
        the_len = len(next(it))
        # Checking the length of both list by using the iter build-in function
        if not all(len(l) == the_len for l in it):
            raise ValueError('The list are not the same length')
        # If everything is fine (not negative numbers neither difference in lists lengths) we add the strings
        else:
            print(float(firstList[i]) + float(secondList[i]))


# Testing
# addNumbers("1234567.8901 2.345", "12.34 2345678901.2")
# addNumbers("123 456 789", "11 22 33")

print("You need to add two string with numbers separated by spaces (please don't use negatives) and the same length in block of numbers")
print("For example:'123 456 789', '11 22 33'")
