def change_data(x):
    if x < 0 or x >255:
        return None
    elif 200 <= x <=255:
        return int(round((x - 200) * 3 / 11.0 + 85, 0))
    elif 0 <= x <=130:
        return int(round(x * 6 / 13.0, 0))
    else:
        return int(round((x - 131) * 23 / 68.0 + 61, 0))


if __name__ == '__main__':
    print('-1 => ' + str(change_data(-1)))
    print('0 => ' + str(change_data(0)))
    print('55 => ' + str(change_data(55)))
    print('131 => ' + str(change_data(131)))
    print('255 => ' + str(change_data(255)))


'''
-1 => None
0 => 0
55 => 25
131 => 61
255 => 100
'''
