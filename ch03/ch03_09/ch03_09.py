def jajb(ans, gus):
    a = 0
    b = 0
    for i in range(4):
        if ans[i] == gus[i]:
            a += 1
        else:
            for j in range(4):
                if gus[i] == ans[j]:
                    b += 1
    return (a, b)


if __name__ == '__main__':
    tu0 = jajb('4321', '4321')
    tu1 = jajb('9487', '0587')
    tu2 = jajb('9527', '2901')
    tu3 = jajb('0521', '1205')
    print('ans = 4321, gus = 4321, result = ' + str(tu0))
    print('ans = 9487, gus = 0587, result = ' + str(tu1))
    print('ans = 9527, gus = 2901, result = ' + str(tu2))
    print('ans = 0521, gus = 1205, result = ' + str(tu3))