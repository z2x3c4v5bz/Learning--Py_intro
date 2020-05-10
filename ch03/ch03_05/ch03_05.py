import math


def is_prime(x):
    i = 2
    if x <= 1:
        return None
    while i <= int(math.sqrt(x)):
        if not (x % i):
            return False
        i += 1
    return True


if __name__ == '__main__':
    print('The prime number between 1 and 100.')
    for i in range(1, 101):
        if is_prime(i):
            print(i)


'''
The prime number between 1 and 100.
2
3
...
89
97
'''
