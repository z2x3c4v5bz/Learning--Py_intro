def myfunc(coes, x):
    result = 0
    for i in range(len(coes)):
        result += (coes[i] * x ** (len(coes) - i - 1))
    return result

if __name__ == '__main__':
    li = [4, 3, 6, 1]
    x = 3
    print(myfunc(li, x))