from collections import defaultdict as ddict

def getanagram(strlist):
    d = ddict(list)
    for i in range(len(strlist)):
        d[''.join(sorted(strlist[i]))].append(strlist[i])
    return list(d.values())

s = ['eat', 'ate', 'done', 'tea', 'opus', 'soup', 'node', 'quick']
print(getanagram(s))


'''

[['eat', 'ate', 'tea'], ['done', 'node'], ['opus', 'soup'], ['quick']]

'''
