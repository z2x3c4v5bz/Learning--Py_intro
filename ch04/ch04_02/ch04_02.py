# ch04-02


def mysplit(arr, n):

    return [arr[i: i+n] for i in range(0 ,len(arr), n)]


if __name__ == '__main__':

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 3

    print(mysplit(arr, n))


''' Output

[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

'''
