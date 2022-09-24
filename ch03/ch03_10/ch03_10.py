# ch03-10
from random import randint


if __name__ == '__main__':

    upper = 100
    lower = 1
    ans = randint(lower, upper)
    cont = 0

    print('_____________________終極密碼_____________________')
    print('從 0～100 中猜一個數字，看你要猜幾次才能猜中。\n')

    while True:

        cont += 1

        print('_____________________Round {}_____________________'.format(cont))
        print('Scope: {}～{}'.format(lower, upper))
        user_k = int(input('Guess a number: '))

        if user_k == 999999:
            print('The answer is {}'.format(ans))

        while user_k <= lower or user_k >= upper:
            user_k = int(input('Guess a number between {} and {}: '.format(lower, upper)))

        print('')

        if user_k == ans:

            print('_________________Congratulations!_________________')
            print('總共試了 {} 次。'.format(cont))
            break

        elif ans < user_k:

            upper = user_k

        else:

            lower = user_k

    input('Game Over~')


''' Output

_____________________終極密碼_____________________
從 0～100 中猜一個數字，看你要猜幾次才能猜中。

_____________________Round 1_____________________
Scope: 1～100
Guess a number: 50

_____________________Round 2_____________________
Scope: 50～100
Guess a number: 75

_____________________Round 3_____________________
Scope: 50～75
Guess a number: 62

_____________________Round 4_____________________
Scope: 50～62
Guess a number: 56

_____________________Round 5_____________________
Scope: 50～56
Guess a number: 53

_____________________Round 6_____________________
Scope: 50～53
Guess a number: 52

_________________Congratulations!_________________
總共試了 6 次。
Game Over~

'''
