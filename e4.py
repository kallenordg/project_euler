def is_palindrome(num):
    reverse = int(str(num)[::-1])
    if num == reverse:
        return True
    else:
        return False

def largest_palindrome_three():
    large_palindrome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if (is_palindrome(i*j) and (i*j > large_palindrome)):
                large_palindrome = i*j
    return large_palindrome

print(largest_palindrome_three())