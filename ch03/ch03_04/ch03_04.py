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
    while x <= 10000:
        print('collatz(' + str(x) + ') = ' + str(collatz(x)))
        x += 1
    input('Press the Enter key to exit...')
