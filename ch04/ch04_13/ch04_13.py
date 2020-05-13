import decimal

if __name__ == '__main__':
    pi = '3.14'
    r = '0.1'
    print('{0} * {1} * {1} = {2}'.format(decimal.Decimal(pi), decimal.Decimal(r), decimal.Decimal(pi) * decimal.Decimal(r) ** 2))


'''

3.14 * 0.1 * 0.1 = 0.0314

'''
