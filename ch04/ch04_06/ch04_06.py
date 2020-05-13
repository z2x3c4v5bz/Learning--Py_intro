def cumulative_sum(li):
    r = []
    a = 1
    for x in li:
        a *= x
        r.append(a)
    return r

if __name__ == '__main__':
    li = [3, 2, 1, 4, 6, 5]

    print(cumulative_sum(li))


'''

[3, 6, 6, 24, 144, 720]

'''
