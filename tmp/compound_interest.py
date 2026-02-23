"""
Formula for Compound Interest - 
a = p(1 + r/100)**t OR a = p * pow((1 + r/100), t)
ci = a - p
Where -
a = Amount
p = Principal
r = Rate of Interest
t = Time in Years
si = Simple Interest
ci = Compound Interest
"""

p = float(input("Enter the pricipal amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time in years: "))

# a = p(1 + r/100)**t OR a = p * pow((1 + r/100), t)
a = p * pow((1 + r/100), t)
print ("The amount is: ",round(a, 2)) # round function to round off the value till 2 digits
ci = a - p
print ("The compound interest is: ",ci)