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
    while (num != 10002):
        if(is_prime(prime)==True):
            prime += 1
            num += 1
        prime += 1
    return prime

print(get_prime())
