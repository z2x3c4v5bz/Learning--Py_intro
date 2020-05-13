from random import randint


if __name__ == '__main__':
    upper = 100
    lower = 1
    ans = randint(1, upper)
    cont = 0
    print('_____________________終極密碼_____________________')
    print('從0 ~ 100中猜一個數字，看你要猜幾次才能猜中。')
    while True:
        cont += 1
        print('_____________________Round ' + str(cont) + '_____________________')
        print('Scope: ' + str(upper) + ' ~ ' + str(lower))
        user_k = int(input('Guess a number: '))
        if user_k == 840521:
            print('The answer is ' + str(ans))
        while user_k <= lower or user_k >= upper:
            user_k = int(input('Guess a number between ' + str(lower) + ' and ' + str(upper) + ': '))
        print('')
        if user_k == ans:
            print('_________________Congratulations!_________________')
            print('總共試了 ' + str(cont) + ' 次。')
            break
        elif ans < user_k:
            upper = user_k
        else:
            lower = user_k
    input('Game Over~')


'''

_____________________終極密碼_____________________
從0 ~ 100中猜一個數字，看你要猜幾次才能猜中。
_____________________Round 1_____________________
Scope: 100 ~ 1
Guess a number: 50

_____________________Round 2_____________________
Scope: 100 ~ 50
Guess a number: 75

_____________________Round 3_____________________
Scope: 100 ~ 75
Guess a number: 90

_____________________Round 4_____________________
Scope: 90 ~ 75
Guess a number: 80

_____________________Round 5_____________________
Scope: 90 ~ 80
Guess a number: 85

_____________________Round 6_____________________
Scope: 90 ~ 85
Guess a number: 88

_____________________Round 7_____________________
Scope: 90 ~ 88
Guess a number: 89

_________________Congratulations!_________________
總共試了 7 次。
Game Over~

'''
