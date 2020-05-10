if __name__ == '__main__':
    def max2sqr(n1, n2, n3):
        if n1 >= n2 > n3:
            max1 = n1
            max2 = n2
        elif n1>= n2 < n3:
            max1 = n1
            max2 = n3
        else:
            max1 = n2
            max2 = n3
        return (max1 ** 2) + (max2 ** 2)
    
    
    print('輸入三個數，將找出最大兩個數的平方和。')
    a = int(input('The first number = '))
    b = int(input('The second number = '))
    c = int(input('The third number = '))
    print('The result is ' + str(max2sqr(a, b, c)))


'''
輸入三個數，將找出最大兩個數的平方和。
The first number = 25
The second number = 12
The third number = 33
The result is 1714
'''
