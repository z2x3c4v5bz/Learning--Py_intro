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


'''

Hamming Distance( 168 , 427 )= 3
Hamming Distance( 333 , 30 )= 5
Hamming Distance( 173 , 2 )= 6
Hamming Distance( 481 , 380 )= 5
Hamming Distance( 446 , 825 )= 5
Hamming Distance( 787 , 757 )= 6
Hamming Distance( 796 , 131 )= 8
Hamming Distance( 902 , 556 )= 5
Hamming Distance( 481 , 912 )= 5
Hamming Distance( 477 , 970 )= 5
Completed!

'''
