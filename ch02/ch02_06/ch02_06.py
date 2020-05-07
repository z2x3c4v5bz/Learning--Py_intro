if __name__ == '__main__':
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    

    def lcm(a, b):
        return int(a * b / gcd(a, b))
    
    
    print('Input two numbers to find the LCM.')
    a = int(input('The first number = '))
    b = int(input('The second number = '))
    print('The result = ', end = '')
    print(str(lcm(a, b)))