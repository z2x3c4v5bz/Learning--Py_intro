# ch03-11
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

        print('Hamming Distance ({:4d}, {:4d}) = {}'.format(a, b, hamming(a, b)))

    print('Completed!')


''' Output

Hamming Distance ( 568,  744) = 3
Hamming Distance ( 637,  607) = 2
Hamming Distance (  55,  263) = 3
Hamming Distance ( 632,  354) = 5
Hamming Distance ( 418,  705) = 6
Hamming Distance ( 211,  439) = 4
Hamming Distance ( 940,  327) = 7
Hamming Distance ( 669,  682) = 5
Hamming Distance ( 327,  492) = 5
Hamming Distance ( 977,  152) = 5
Completed!

'''
