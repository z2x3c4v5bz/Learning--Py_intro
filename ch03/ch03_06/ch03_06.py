def is_1089(x):
    x = str(x)

    if abs(int(x[0]) - int(x[2])) < 2:
        return None
    
    x_inv = 0

    for i in range(3):
        x_inv += ((int(x[i])) * 10 ** i)
    
    y = abs(int(x) - x_inv)
    y = str(y)
    ans = 0
    y_inv = 0

    if len(y) == 3:
        for i in range(3):
            y_inv += ((int(y[i])) * 10 ** i)
    elif len(y) == 2:
        y_inv = int(y[0]) * 10 + int(y[1]) * 100
    else:
        y_inv = int(y[0]) * 100
    
    ans = int(y) + y_inv

    if ans == 1089:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(100, 1000):
        if is_1089(i) is None or is_1089(i):
            continue
        else:
            print('False!')
            break
    else:
        print('True!')


'''

True!

'''
