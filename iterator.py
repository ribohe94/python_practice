#!/usr/bin/python3
import sys
list=[1,2,3,4]
it = iter(list)     #This builds an iterator object
print (next(it))    #Prints next available element in iterator
#Iterator object can be traversed using regular for statement

for x in it:
   print (x)

while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
