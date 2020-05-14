if __name__ == "__main__":
    s = [('Amy', 70), ('Bob', 50), ('Cathy', 30), ('David', 50)]
    d = dict()
    for i in s:
        if i[1] in d.keys():
            d[i[1]].append(i[0])
        else:
            d[i[1]] = [i[0]]
    print(d)

    r = 'banana'
    d2 = dict()
    for l in r:
        if l in d2.keys():
            d2[l] += 1
        else:
            d2[l] = 1
    print(d2)


'''

{70: ['Amy'], 50: ['Bob', 'David'], 30: ['Cathy']}
{'b': 1, 'a': 3, 'n': 2}

'''
