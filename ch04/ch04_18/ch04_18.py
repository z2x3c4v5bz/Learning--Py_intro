# ch04-18


def myfunc(i):

    i = str(abs(i))

    for x in range(len(i) // 2 + 1):

        if i[x] != i[len(i) - x - 1]:

            return False

    return True


def myfunc2(i):

    i -= 1

    return [x for x in range(int('1' + ('0' * i)), int('9' + ('9' * i)) + 1) if myfunc(x)]


if __name__ == '__main__':

    li = [11, 101, 151, 484, 10201, 11201]

    for i in li:

        print('"' + str(i) + '" 是迴文數?', end=' ')
        print(str(myfunc(i)))

    print('\n')

    xx = myfunc2(2)
    print('{0}位數的迴文數有 {1} 個，分別是:\n{2}\n'.format(2, len(xx), xx))

    xx = myfunc2(3)
    print('{0}位數的迴文數有 {1} 個，分別是:\n{2}\n'.format(3, len(xx), xx))

    xx = myfunc2(4)
    print('{0}位數的迴文數有 {1} 個，分別是:\n{2}\n'.format(4, len(xx), xx))


''' Output

"11" 是迴文數? True
"101" 是迴文數? True
"151" 是迴文數? True
"484" 是迴文數? True
"10201" 是迴文數? True
"11201" 是迴文數? False


2位數的迴文數有 9 個，分別是:
[11, 22, 33, 44, 55, 66, 77, 88, 99]

3位數的迴文數有 90 個，分別是:
[101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 
555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]  

4位數的迴文數有 90 個，分別是:
[1001, 1111, 1221, 1331, 1441, 1551, 1661, 1771, 1881, 1991, 2002, 2112, 2222, 2332, 2442, 2552, 2662, 2772, 2882, 2992, 3003, 3113, 3223, 3333, 3443, 3553, 3663, 3773, 3883, 3993, 4004, 4114, 4224, 4334, 4444, 4554, 4664, 4774, 4884, 4994, 5005, 5115, 5225, 5335, 5445, 5555, 5665, 5775, 5885, 5995, 6006, 6116, 6226, 6336, 6446, 6556, 6666, 6776, 6886, 6996, 7007, 7117, 7227, 7337, 7447, 7557, 7667, 7777, 7887, 7997, 8008, 8118, 8228, 8338, 8448, 8558, 8668, 8778, 8888, 8998, 9009, 9119, 9229, 9339, 9449, 9559, 9669, 9779, 9889, 9999]

'''
