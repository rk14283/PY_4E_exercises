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
      
      
      
      
      
