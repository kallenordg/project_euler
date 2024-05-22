def number_divisible_twenty(number):
    for i in range(2,21):
        if number % i != 0:
            return False
    return True

def smallest_twenty():
    number = 20
    while(not(number_divisible_twenty(number))):
        if number_divisible_twenty(number) == False:
            number += 20
    return number

print(smallest_twenty())
