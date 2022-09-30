# ch03-12


def exchangebit(n):

    m1 = 0b10101010101010101010101010101010
    m2 = ~m1

    return ((n << 1) & m1) | ((n >> 1) & m2)


if __name__ == '__main__':

    n1 = 0b10101010
    n2 = 0b01010101
    n3 = 0b11001100
    n4 = 0b10011001
    n5 = 0b01100110

    print('exchangebit({:032b}) = {:032b}'.format(n1, exchangebit(n1)))
    print('exchangebit({:032b}) = {:032b}'.format(n2, exchangebit(n2)))
    print('exchangebit({:032b}) = {:032b}'.format(n3, exchangebit(n3)))
    print('exchangebit({:032b}) = {:032b}'.format(n4, exchangebit(n4)))
    print('exchangebit({:032b}) = {:032b}'.format(n5, exchangebit(n5)))


''' Output



'''