# ch03-04


def collatz(x):

    numarr = []
    numarr += [x]

    while x:

        if x == 1:
            break

        if x % 2:

            x = 3 * x + 1

        else:

            x //= 2

        numarr += [x]

    return numarr


if __name__ == '__main__':

    x = 1
    flag = True

    while x <= 10000:

        re = collatz(x)

        if re[-1] != 1:
            flag = False
        
        print('collatz({:5d}) = {}\n'.format(x, re))
        x += 1
    
    print(flag)
    input('輸入 Enter 鍵結束...')


''' Output

collatz(1) = [1]
...
collatz(10000) = [10000, 5000, 2500, 1250, 625, 1876, 938, 469, 1408, 704, 352, 176, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
True
輸入 Enter 鍵結束...

'''
