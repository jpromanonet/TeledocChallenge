firstString = "1111 5555"
secondString = "2222 4444"


# Let's create a list from the strings
def addNumbers(firstString, secondString):
    firstList = list(firstString.split(" "))
    secondList = list(secondString.split(" "))
    for i in firstList:
        print(firstList[i]+secondList[i])


addNumbers(firstString, secondString)
