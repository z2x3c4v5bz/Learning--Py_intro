# ch02-08


# 用來確認是否為閏年
def is_leapYear(year):

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

        return True
        
    else:

        return False


# 用來確認某月份的天數
def hmDays(year, month):

    _31d = (1, 3, 5, 7, 8, 10, 12)

    if month == 2:

        if is_leapYear(year):

            return 29

        else:

            return 28
    
    else:

        for i in _31d:

            if month == i:

                return 31

    return 30


# 確認輸入的日期正不正確
def is_correct(date_a, date_b):

    if date_a[0] < 0 or date_b[0] < 0:

        print('Error(year)')

        return None

    if 0 >= date_a[1] or date_a[1] > 12 or 0 >= date_b[1] or date_b[1] > 12:

        print('Error(month)')

        return None

    day_a = hmDays(date_a[0], date_a[1])
    day_b = hmDays(date_b[0], date_b[1])

    if 0 >= date_a[2] or date_a[2] > day_a or 0 >= date_b[2] or date_b[2] > day_b:

        print('Error(day)')

        return None

    return True


# 檢查室否有日期需要進位
def is_overMD(date, arg_statu):

    if arg_statu == 1:

        lmtday = hmDays(date[0], date[1])

        if date[2] > lmtday:

            date[2] = 1
            date[1] += 1

    if date[1] > 12:

        date[1] = 1
        date[0] += 1
    
    return date
    

# 計算日期
def process_date(date_a, date_b):

    sum_d = 0

    if date_b[0] == date_a[0]:

        if date_b[1] == date_a[1]:

            return date_a[2] - date_b[2]

        else:

            sum_d = hmDays(date_b[0], date_b[1]) - date_b[2]
            date_b[2] = 32
            date_b = is_overMD(date_b, 1)

            while date_b[1] < date_a[1]:

                sum_d += hmDays(date_b[0], date_b[1])
                date_b[1] += 1

            return sum_d + date_a[2]

    else:

        sum_d = hmDays(date_b[0], date_b[1]) - date_b[2]
        date_b[2] = 32
        date_b = is_overMD(date_b, 1)

        while (date_b[0] != date_a[0]) or (date_b[1] < date_a[1]):

            sum_d += hmDays(date_b[0], date_b[1])
            date_b[1] += 1
            date_b = is_overMD(date_b, 0)

        return sum_d + date_a[2]


# 交換日期，方便後面運算
def exchange_date(date_a, date_b):

    i = 0
    
    while i < 3:

        if date_a[i] < date_b[i]:

            return [date_b, date_a]
        
        i += 1

    return [date_a, date_b]


# 呼叫其他函數
def calculDays(date_a, date_b):

    if not is_correct(date_a, date_b):

        print('日期有誤!')

        return None

    if date_a == date_b:

        return 0

    else:

        tmp = exchange_date(date_a, date_b)
        date_a = tmp[0]
        date_b = tmp[1]

    total_days = process_date(date_a, date_b)

    return total_days


# 顯示日期
def show_days(date_1, date_2):

    print('第一個日期是: {}'.format(date_1))
    print('第二個日期是: {}'.format(date_2))

    days = calculDays(date_1, date_2)

    if days:
        print('總共相差 {} 天。'.format(days))


# 輸入日期
def process_ipt(a):

    li_a = []
    li_a += [(a // 10000)]
    a -= ((a // 10000) * 10000)
    li_a += [(a // 100)]
    a -= ((a // 100) * 100)
    li_a += [a]

    return li_a


if __name__ == '__main__':

    ipt_a = int(input('輸入第一個日期 (yyyymmdd): '))
    ipt_b = int(input('輸入第二個日期 (yyyymmdd): '))

    date_a = []
    date_b = []

    date_a = process_ipt(ipt_a)
    date_b = process_ipt(ipt_b)

    show_days(date_a, date_b)


''' Output

輸入第一個日期 (yyyymmdd): 20131224
輸入第二個日期 (yyyymmdd): 20190304
第一個日期是: [2013, 12, 24]
第二個日期是: [2019, 3, 4]
總共相差 1896 天。

'''
