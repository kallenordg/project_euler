def sum_multiples_3_and_5(under):
    count = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            count += i
        else:
            None
    return count

print(sum_multiples_3_and_5(1000))