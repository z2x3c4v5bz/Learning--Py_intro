import math


def stirling(n):
    ans = math.sqrt(2 * math.pi * n) * pow((n / math.e), n)
    return round(ans, 4)


if __name__ == '__main__':
    print('10! ~ ' + str(stirling(10)))