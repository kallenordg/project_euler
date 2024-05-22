def sum_square_hundred():
    number = 0
    for i in range(1,101):
        number += pow(i,2)
    return number

def square_sum_hundred():
    number = 0
    for i in range(1,101):
        number += i
    return pow(number,2)

print(square_sum_hundred()-sum_square_hundred())
