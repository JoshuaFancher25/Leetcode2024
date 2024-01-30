# leetcode 202
# happy number
# getting the square of digits in the number

# modulus returns the remainder after a division operation

x = 123
print(x)
print(x%10)
print(x//10)

def get_next(n):
    computed_sum = 0
    while n > 0:
        rem = n%10
        n = n//10
        computed_sum += rem**2
    return computed_sum

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
print(is_happy(19))