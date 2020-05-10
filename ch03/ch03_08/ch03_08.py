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
                    print('Cardano Triplet #' + str(num) + ' = ', end = '')
                    print(i, j, k)
                else:
                    continue
    Tend = time.time()
    totaltime = Tend - Tstart
    print('Completed!')
    print('CPU Time = ' + str(totaltime) + 'sec.')