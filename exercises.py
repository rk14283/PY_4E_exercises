

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
