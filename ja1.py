x = 10
divisorsum = 0
for i in range(1, x+1):
    if x % i == 0:
        divisorsum += i
        
# ans = 0
# if divisorsum >= 0:
#  while ans*ans < divisorsum:
#     ans = ans + 1
# print ('ans ='), ans
# if ans*ans != divisorsum:
#     print x, 'is not a perfect square'
# else: print ans
#     else: print x, 'is a negative number'
print("Sum of divisors of", x, ":", divisorsum)  