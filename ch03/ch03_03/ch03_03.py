# ch03-03


def is_divby3(x):

    mysum = 0

    for i in range(len(x)):
        mysum += int(x[i])

    if mysum % 3 == 0:

        return True

    else:

        return False


if __name__ == '__main__':

    print('21 % 3 = 0? {}'.format(is_divby3(str(21))))
    print('32 % 3 = 0? {}'.format(is_divby3(str(32))))


''' Output

21 % 3 = 0? True
32 % 3 = 0? False

'''
