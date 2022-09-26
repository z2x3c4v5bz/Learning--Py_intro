# ch05-08
from collections import defaultdict as ddict


def getanagram(strlist):

    d = ddict(list)

    for i in range(len(strlist)):
        d[''.join(sorted(strlist[i]))].append(strlist[i])

    return list(d.values())


if __name__ == '__main__':

    s = ['eat', 'ate', 'done', 'tea', 'opus', 'soup', 'node', 'quick']

    print(getanagram(s))


''' Output

[['eat', 'ate', 'tea'], ['done', 'node'], ['opus', 'soup'], ['quick']]

'''
