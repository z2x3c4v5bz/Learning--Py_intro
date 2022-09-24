# ch02-06


def gcd(a, b):
    
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    
    print('Input two numbers to find the LCM.')

    a = int(input('The 1st number = '))
    b = int(input('The 2nd number = '))

    print('The result = {}'.format(lcm(a, b)))


''' Output

Input two numbers to find the LCM.
The 1st number = 21
The 2nd number = 6
The result = 42

'''
