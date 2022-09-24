# ch02-01


if __name__ == '__main__':

    user_year = int(input('輸入一個年份以判別是否為閏年: '))
    
    if user_year % 400 == 0 or (user_year % 4 == 0 and user_year % 100 != 0):

        print('{} 是閏年。'.format(user_year))

    else:
        
        print('{} 不是閏年。'.format(user_year))

    input('輸入 Enter 鍵結束...')


''' Output

輸入一個年份以判別是否為閏年: 2020
2020 是閏年。
輸入 Enter 鍵結束...

'''
