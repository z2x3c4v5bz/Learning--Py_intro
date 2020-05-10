def newli2d(rows, cols, s):
    s = str(s)
    return [[s for i in range(cols)] for j in range(rows)]

if __name__ == '__main__':
    print(newli2d(2, 3, None))
    print(newli2d(4, 2, 2))