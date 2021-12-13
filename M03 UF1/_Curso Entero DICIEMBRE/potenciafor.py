power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
"""
The expo variable is used as a control variable for the loop, and indicates the current value of the exponent. 
The exponentiation itself is replaced by multiplying by two. Since 20 is equal to 1, then 2 × 1 is equal to 21, 2 × 21 is equal to 22,
 and so on. What is the greatest exponent for which our program still prints the result?
"""

