import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python fibonacci.py <n>")

def fibonacci(n):
    if n <= 1:
        print(1`)
        return (n, 0)
    else:
        (a, b) = fibonacci(n-1)
        print(a+b)
        return (a+b, a)
    
fibonacci(int(sys.argv[1]))