def myfunc(i):
    i = str(abs(i))
    for x in range(len(i)//2+1):
        if i[x] != i[len(i)-x-1]:
            return False
    return True

def myfunc2(i):
    i -= 1
    return [x for x in range(int('1'+('0'*i)), int('9'+('9'*i))+1) if myfunc(x)]

if __name__ == '__main__':
    li = [11, 101, 151, 484, 10201, 11201]
    for i in li:
        print('"' + str(i) + '" 是迴文數?', end=' ')
        print(str(myfunc(i)))
    print('\n')
    xx = myfunc2(2)
    print('{0}位數的迴文數有 {1} 個，分別是:\n{2}\n'.format(2, len(xx), xx))
    xx = myfunc2(3)
    print('{0}位數的迴文數有 {1} 個，分別是:\n{2}\n'.format(3, len(xx), xx))
    xx = myfunc2(4)
    print('{0}位數的迴文數有 {1} 個，分別是:\n{2}\n'.format(4, len(xx), xx))