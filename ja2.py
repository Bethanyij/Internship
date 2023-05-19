print 
x= (input("Input value :"))
# The value we want to find the sum of their divisors is now bound to the variable "x"
x=int(x)
# when the value was inputed it came as a string and we want to act on that value as an integer hence the conversion
divisorsum=0
divisor=1

while divisor <= x:
    if x % divisor == 0:
        divisorsum += divisor

    divisor += 1
        
print ("The sum of the divisors of", x,"is:", divisorsum)