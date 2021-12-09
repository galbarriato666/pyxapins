"""print("#" *10) 
print(("#" + 8 * " " + "#\n") * 5)"""

def Fib(n):
    a,b = 0,1
    c=','
    while(a<n):
       print(a, end='')   # Way to print in same line
       a,b = b, a+b
       if a<n:
         print(c, end=',') # Way to ensure keep printing in same line
Fib(1000)
