# Let's create a list from the strings
def addNumbers(firstString, secondString):
    firstList = list(firstString.split(" "))
    secondList = list(secondString.split(" "))
    length = len(firstList)
    for i in range(length):
        print(float(firstList[i])+float(secondList[i]))


addNumbers("1234567.8901 2.345", "12.34 2345678901.2")
