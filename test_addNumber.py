import addnumbers

firstTest = addnumbers.addNumbers("123 456 789", "11 22 33")
print(firstTest) # Should return 134 478822

def secondTest():
    assert addnumbers.addNumbers(["1234567.8901 2.345", "12.34 2345678901.2"]) == ["1234580.2301", "2345678903.545"], "Should be 1234580.2301 2345678903.545"

if __name__ == "__main__":
    secondTest()
    print("Everything passed")
