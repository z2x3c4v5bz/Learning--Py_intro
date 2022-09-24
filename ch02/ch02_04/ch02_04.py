# ch02-04


def ctof(number):

    return number * (9 / 5) + 32


def ftoc(number):
    
    return (number - 32) * 5 / 9


if __name__ == '__main__':

    tpt = float(input('輸入攝氏溫度，轉華氏溫度: '))
    print('華氏溫度 = {:.2f}'.format(ctof(tpt)))

    tpt = float(input('輸入華氏溫度，轉攝氏溫度: '))
    print('攝氏溫度 = {:.2f}'.format(ftoc(tpt)))


''' Output

輸入攝氏溫度，轉華氏溫度: 33
華氏溫度 = 91.40
輸入華氏溫度，轉攝氏溫度: 91.4
攝氏溫度 = 33.00

'''
