# ch02-05


def max2sqr(n1, n2, n3):

    if n1 >= n2 > n3:

        max1 = n1
        max2 = n2

    elif n1 >= n2 < n3:

        max1 = n1
        max2 = n3

    else:

        max1 = n2
        max2 = n3

    return (max1 ** 2) + (max2 ** 2)


if __name__ == '__main__':
    
    print('輸入三個數，將找出最大兩個數的平方和。')

    a = int(input('The 1st number = '))
    b = int(input('The 2nd number = '))
    c = int(input('The 3rd number = '))

    print('The result is {}.'.format(max2sqr(a, b, c)))


''' Output

輸入三個數，將找出最大兩個數的平方和。
The 1st number = 25
The 2nd number = 12
The 3rd number = 33
The result is 1714.

'''
