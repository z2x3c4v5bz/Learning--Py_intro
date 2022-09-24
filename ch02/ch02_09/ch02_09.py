# ch02-09


def fac(n):

    ans = 1

    for i in range(1, n + 1):
        ans *= i
    
    ans = str(ans)
    mysum = 0

    for i in ans:
        mysum += int(i)

    return [ans, mysum]


if __name__ == '__main__':


    n = int(input('Enter a number: '))
    li = fac(n)

    print('{}! = {}'.format(n, li[0]))

    for i in range(0, len(li[0])):

        if i != (len(li[0]) - 1):

            print('{} + '.format(li[0][i]), end='')

        else:

            print('{} = {}'.format(li[0][i], li[1]))


''' Output

Enter a number: 6
6! = 720
7 + 2 + 0 = 9

'''
