# ch03-07
import math


def stirling(n):

    ans = math.sqrt(2 * math.pi * n) * pow((n / math.e), n)

    return round(ans, 4)


if __name__ == '__main__':

    print('10! ~ {}'.format(stirling(10)))


''' Output

10! ~ 3598695.6187

'''
