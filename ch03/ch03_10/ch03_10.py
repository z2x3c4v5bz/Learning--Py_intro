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