#!/usr/bin/python3
#while loop

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

var = 1
while var == 1 :  # This constructs an infinite loop
   num = int(input("Enter a number (0 is for exit) :"))
   if num == 0 : break
   print ("You entered: ", num)


#If the else statement is used with a while loop, the else statement is executed when the condition becomes false.
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
