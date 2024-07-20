def is_prime(number): # more efficient prime function checking up to square root
    if number == 1:
        return False  
    elif number == 2:
        return True
    else:
        for i in range(2, int(number ** 0.5) + 1): 
            if number % i == 0:
                return False
        return True

def primes_under_two_million():
    result = 2
    for i in range(3, 2000001, 2):
        print(i)
        if is_prime(i):
            result += i
    return result

print(primes_under_two_million())