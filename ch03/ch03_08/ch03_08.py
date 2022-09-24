# ch03-08
import math
import time


def cardano(a, b, c):

    if a - b * math.sqrt(c) < 0:

        return pow(a + b * math.sqrt(c), 1 / 3) - pow(abs(a - b * math.sqrt(c)), 1 / 3)
    
    return pow(a + b * math.sqrt(c), 1 / 3) + pow(a - b * math.sqrt(c), 1 / 3)


if __name__ == '__main__':

    Tstart = time.time()
    lim = 1000
    diff = 0.000000001
    ite = range(1, lim)
    num = 0

    for i in ite:

        for j in ite:

            for k in ite:

                if i + j + k > lim:

                    break

                elif abs(cardano(i, j, k) - 1) < diff:

                    num += 1
                    print('Cardano Triplet #{:3d} -> {:3d}, {:3d}, {:3d}'.format(num, i, j, k))

                else:

                    continue
    
    Tend = time.time()
    totaltime = Tend - Tstart
    print('Completed!')
    print('CPU Time = {:.5f}sec.'.format(totaltime))


''' Output

Cardano Triplet #  1 ->   2,   1,   5
Cardano Triplet #  2 ->   5,   1,  52
...
Cardano Triplet #148 -> 395, 396, 117
Cardano Triplet #149 -> 422, 423, 125
Completed!
CPU Time = 87.11721sec.

'''
