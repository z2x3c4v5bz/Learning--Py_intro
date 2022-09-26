# ch04-15


def mystr(s):

    ws = ['e.x.', 'ex.', 'eg.', 'E.x.', 'Ex.', 'Eg.']
    cors = 'e.g.'
    wsexist = [w for w in ws if s.count(w) > 0]

    for w in wsexist:

        start = 0

        for _ in range(s.count(w)):

            if s.find(w) >= 0:

                start = s.find(w, start)

                if w.lower() == 'ex.' and len(s[start: ]) >= 5 and s[start + 4].isdecimal():

                    continue

                elif len(w) == 3:

                    scopy = list(s)
                    del scopy[start: start + 3]

                else:

                    scopy = list(s)
                    del scopy[start: start + 4]

                scopy.insert(start, cors)
                start += 1
                s = ''.join(scopy)

    return s


if __name__ == '__main__':

    s1 = 'I love animals, e.x., dogs, birds, and cats.'
    s2 = 'Please take a look at Ex. 1'
    s3 = 'I love animals, eg., dogs, birds, and cats.'
    s4 = 'Please take a look at Ex.'

    print('s1 = ' + s1)
    print('s1_new = ' + mystr(s1) + '\n')

    print('s2 = ' + s2)
    print('s2_new = ' + mystr(s2) + '\n')

    print('s3 = ' + s3)
    print('s3_new = ' + mystr(s3) + '\n')

    print('s4 = ' + s4)
    print('s4_new = ' + mystr(s4) + '\n')


''' Output

s1 = I love animals, e.x., dogs, birds, and cats.
s1_new = I love animals, e.g., dogs, birds, and cats.

s2 = Please take a look at Ex. 1
s2_new = Please take a look at Ex. 1

s3 = I love animals, eg., dogs, birds, and cats.
s3_new = I love animals, e.g., dogs, birds, and cats.

s4 = Please take a look at Ex.
s4_new = Please take a look at e.g.

'''
