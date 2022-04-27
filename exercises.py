# Exercise 2.3 

# This first line is provided for you

hrs = float (input("Enter Hours:"))
rate =float (input("Enter Rate per Hour:"))

pay = float (hrs*rate)

print("Pay: "+ str(pay)) 


#Exercise 3.1 
#You get the correct answer with 0.5 not 1.5 

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("input rate:")
r = float(rate) 

if h>40:
    reg_pay = h*r
    ot= (h-40.0)*(r*0.5)
    pay =  ot + reg_pay
else:
    pay = h*r 
    
print(pay)

#Exercise 4.6 

h = float (input("Enter Hours:"))
r = float(input("Enter rate"))

def computepay(h, r):
    if h>40:
        reg_pay =h*r
        ot= (h-40.0)*(r*0.5)
        pay = ot + reg_pay
    else:
        pay = h*r 
    return pay

p = computepay(h, r)
print("Pay", float(p)
 
#A simple loop 
 for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')     
      
"""   lazy code that assumed all numbers are positive, it would not have worked if all numbers were negative    
   """   
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num> largest_so_far:
        largest_so_far = the_num 
    print(largest_so_far,the_num)
print('After', largest_so_far)


"""
print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')        
"""
    

"""
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
"""      

#loop patterns       
      
      
#Counting in a loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork - zork+1
    print(zork, thing)
print('After', zork)


print
print

#Summing in a loop 
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork= zork+thing 
    print(zork,thing)
print('After', zork)


print 
print 

#Average 
"""The proces is similar to above but we divide those"""

count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count+1
    sum = sum + value 
    print(count, sum, value)
print('After', count, sum, sum/count)


#pattern of something in the begining, something in middle, something in end 


print 
print

"""Filtering in a loop, here we are looking for something
this may be important for some search algorithm 
"""

""" we use if statment in the loop to catch/filter the
values we are looking for 
"""

print('Before')
for value in [9,41,12,3,74,15]:
    if value>20:
        print('Large number', value)
print('After')

#this is cool use for try 
try: 
    prin #this code will blow up 
except:
    print
    print 

#Search using Boolean variable 
"""
If we just want to search and know if a vlaue was found, we 
use a variable that starts at False and is set to True as
soon as we fund what we are looking for. 
"""

found = False 
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value==3:
        found = True 
    print(found, value)
print 


"""how might we make the loop more efficient 
so that when it found the 3 it stops 
"""


#smallest number 
#first value as hypothesis for smallest so far
"""
This technique of using None can also be used for largest 
"""
print 
print 

smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value 
    elif value<smallest:
        smallest = value 
    print(smallest, value)
print('After', smallest )

      
#Bear in mind these codes are complicated      

#is and is not, same result as abvoe  

smallest = None
print('Before')
for value in [3,41,12,9,74,15]:
    if smallest is None:
        smallest = value 
    elif value<smallest:
        smallest = value 
    print smallest, value 
    
    
print ('After', smallest)      
      
 #the output is 5     
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot= tot + 1
print(tot)

#basically in the above i switches from 0 to 5
      
