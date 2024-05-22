def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def under(number):
    for i in range(35):
        if fib(i) > number:
            return i-1
        
def sum_under_even(under_number):
    fib_number = under(under_number)
    sum = 0
    for i in range(1,fib_number+1):
        if fib(i) % 2 == 0:
            sum += fib(i)
    return sum
        
print(sum_under_even(4000000))