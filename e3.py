def is_prime(number):
    if number == 1:
        return True
    else:
        for i in range(2, number//2+1):
            if number % i == 0:
                return False
        return True
    
def highest_prime_factor(number):
    new_number = number
    highest_prime = 0
    while (not(is_prime(new_number))):
        for i in range(2, new_number//2+1):
            if is_prime(i) and (new_number % i == 0):
                new_number = new_number//i
                highest_prime = new_number
                break
    return highest_prime

print(highest_prime_factor(600851475143))