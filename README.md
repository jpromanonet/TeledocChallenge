# TeledocChallenge
Teledoc Challenge in python

I use python to solve the take-home exercise which has the followings requirements:

1. The function should be called addNumbers
2. The function should accept 2 string params
3. Each string param contains M numbers, separated by spaces
4. The function must add the numbers in pairs by "blocks" meaning the first numbers of the first string should add to the first number of the second string
5. The output should be the sums of the pairs, separated by spaces
6. The strings have the same count of numbers
7. The numbers may include decimal places
8. The numbers can be super long like more than 1000+ digits

---

### How do I solve it?

1. I just call the function addNumbers in python
2. Define two params called firstString and secondString to be clear
3. Make an input to ask for the strings
4. Here is where the good stuff starts, I took both strings and then use the split build-in function to make both strings list so every number becomes an element into a list, after that I took the firstString that now is firstList and take the len so I can loop over every element and add every element with the same element position in secondString which now is called secondList but before that I have to do some validations.
5. The output on the bash shell is spaces so I don't look that much into this point right now.
6. As I did in point four, I took both list and put them into another list which I call lists and then using the build-in iter function over the new list called lists I check that both list has the same number of elements if not it will raise an error and stop execution.
7. After passing validation, I took both lists and convert them to float and print the sum of the elements by their index as float numbers, it works just fine.
8. Test it with super long numbers and it works OK
9. Also the assigment said that the numbers can't be negative so before the first validation, the one about the length of the strings, I transform the list called "lists" into a string for a bit to use the find built-in function and look for any negative sign(-) if there is one an error would be raised and execution stopped and if not it will continue on the next validation until we add the numbers.

### What was my thought process to solve it?

I took the whole problem and separated into little ones (one problem for each point or so) and I went to solve the main one about taking two strings of numbers and add each one with their correlative and after that I added features until every point was complete.

I won't lie and say I didn't use google so I let the links of where I look up for help to solve it:

https://www.geeksforgeeks.org/iterate-over-a-list-in-python/

https://stackoverflow.com/questions/10613131/how-to-access-list-elements

https://www.geeksforgeeks.org/python-program-convert-string-list/

https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/

https://www.w3schools.com/python/python_user_input.asp 

---
Also I added some super basic user interface on the terminal to make it easier to test if it works.