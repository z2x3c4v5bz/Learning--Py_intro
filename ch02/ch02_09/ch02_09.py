if __name__ == '__main__':
    def fac(n):
        ans = 1
        for i in range(1, n + 1):
            ans *= i
        ans = str(ans)
        mysum = 0
        for i in ans:
            mysum += int(i)
        return [ans, mysum]
    

    n = int(input('Enter a number: '))
    li = fac(n)

    print(str(n) + '! = ' + str(li[0]))

    for i in range(0, len(li[0])):
        if i != (len(li[0]) - 1):
            print(str(li[0][i]) + '+', end = '')
        else:
            print(str(li[0][i]) + '=' + str(li[1]))


'''

Enter a number: 6
6! = 720
7+2+0=9

'''
