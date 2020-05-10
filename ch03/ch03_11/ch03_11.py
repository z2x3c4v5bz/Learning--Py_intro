from random import randint


def hamming(a, b):
    cont = 0
    compr = a ^ b
    for i in range(32):
        if (compr >> i) & 0b1:
            cont += 1
    return cont


if __name__ == '__main__':
    for i in range(10):
        a = randint(1, 1000)
        b = randint(1, 1000)
        print('Hamming Distance( ' + str(a) + ' , ' + str(b) + ' )= ' + str(hamming(a, b)))
    print('Completed!')