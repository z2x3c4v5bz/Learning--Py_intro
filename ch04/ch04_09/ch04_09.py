# ch04-09


def rangeStr(char, lastchar='', jump=1):

    letters = 'abcdefghijklmnopqrstuvwxyz'
    result =[]

    if (len(char) == 1 and char.isalpha()) and lastchar == '':

        lastchar = letters.find(char.lower())
        char = 0

    elif (len(char) == 1 and char.isalpha()) and (len(lastchar) == 1 and lastchar.isalpha()):

        char = letters.find(char.lower())
        lastchar = letters.find(lastchar.lower())

    else:

        print('Invalid input!')

        return None

    for letterindex in range(char, lastchar, jump):
        result.append(letters[letterindex])

    print(result)

    return None


if __name__ == '__main__':

    print("Input ('aa'): ", end='')
    rangeStr('aa')

    print("Input ('a', 'cc'): ", end='')
    rangeStr('a', 'cc')

    print("Input ('1'): ", end='')
    rangeStr('1')

    print("Input ('a', '1'): ", end='')
    rangeStr('a', '1')

    print("Input ('f'): ", end='')
    rangeStr('f')

    print("Input ('i', 'l'): ", end='')
    rangeStr('i', 'l')

    print("Input ('a', 'f', 2): ", end='')
    rangeStr('a', 'f', 2)


''' Output

Input ('aa'): Invalid input!
Input ('a', 'cc'): Invalid input!
Input ('1'): Invalid input!
Input ('a', '1'): Invalid input!
Input ('f'): ['a', 'b', 'c', 'd', 'e']
Input ('i', 'l'): ['i', 'j', 'k']
Input ('a', 'f', 2): ['a', 'c', 'e']

'''
