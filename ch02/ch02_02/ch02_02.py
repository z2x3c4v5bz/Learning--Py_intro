if __name__ == '__main__':
    print('by for loop: ')
    for i in range(1, 10):
        for j in range(1, 10):
            print(str(j) + '*' + str(i) + '=' + str(i * j), end = ' ')
            if j == 9:
                print()
    print()

    print('by while loop: ')
    i, j = 1, 1
    while i <= 9:
        while j <= 9:
            print(str(j) + '*' + str(i) + '=' + str(i * j), end = ' ')
            if j == 9:
                print()
            j += 1
        j = 1
        i += 1