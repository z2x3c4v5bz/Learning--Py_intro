# ch04-16


def jpalin(s):

    s = s.lower()
    strnew = [letter for letter in s if 97 <= ord(letter) <= 122]

    for i in range(len(strnew) // 2 + 1):

        if strnew[i] != strnew[len(strnew) - i - 1]:

            return False

    return True


if __name__ == '__main__':

    s = ['race car', 'Amor, Roma', "No 'x' in Nixon", 'A man, a plan, a canal, Panama!', 'My mom.']

    for w in s:

        print('"' + w + '" a palindrome?')
        print(str(jpalin(w)) + '\n')


''' Output

"race car" a palindrome?
True

"Amor, Roma" a palindrome?
True

"No 'x' in Nixon" a palindrome?
True

"A man, a plan, a canal, Panama!" a palindrome?
True

"My mom." a palindrome?
False

'''
