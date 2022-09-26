# ch04-03


def arrplus(arr):

    return [arr[i] + i for i in range(len(arr))]


if __name__ == '__main__':

    arr = [8, 4, 1, 7]

    print(arrplus(arr))


''' Output

[8, 5, 3, 10]

'''
