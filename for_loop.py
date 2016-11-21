#!/usr/bin/python3
#for loop

for var in list(range(5)):
	print (var)

for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

numbers=[11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num%2==0:
        print ('the list contains an even number')
        break	#If it gets here, it will not reach the else statement.
else:
    print ('the list doesnot contain even number')
