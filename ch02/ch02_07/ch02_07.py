# ch02-07


def find_most(li):

    a = li[0]
    li_new = []
    li_temp = []

    for i in li:

        if a is i:

            li_temp += [a]

        else:

            li_new += [li_temp]
            del li_temp
            li_temp = []
            a = i
            li_temp += [a]
    
    li_new += [li_temp]
    maxi = []

    for i in li_new:

        if len(i) > len(maxi):
            maxi = i

    return maxi[0]


if __name__ == '__main__':
    
    li = [0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 23, 25, 25, 25]

    print('li = {}'.format(li))
    print('li 出現最多次且最小的數: {}'.format(find_most(li)))


''' Output

li = [0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 23, 25, 25, 25]
li 出現最多次且最小的數: 9

'''
