def is_prime(number):
    if number == 1:
        return True
    else:
        for i in range(2, number//2+1):
            if number % i == 0:
                return False
        return True

def get_prime():
    num = 0
    prime = 2
    while (num != 10001):
        if(is_prime(prime)==True):
            num += 1
        if num == 10001:
            return prime
        prime += 1

print(get_prime())
