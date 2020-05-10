if __name__ == '__main__':
    import ch02_04_mod as mymod


    tpt = float(input('輸入攝氏溫度，轉華氏溫度: '))
    print('華氏溫度=' + str(mymod.ctof(tpt)))

    tpt = float(input('輸入華氏溫度，轉攝氏溫度: '))
    print('攝氏溫度=' + str(mymod.ftoc(tpt)))


'''
輸入攝氏溫度，轉華氏溫度: 33
華氏溫度=91.4
輸入華氏溫度，轉攝氏溫度: 91.4
攝氏溫度=33.0
'''
