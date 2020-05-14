if __name__ == '__main__':
    stock = {
        'Apple': 655.95, 'IBM': 202.13, 'HP': 45.51, 'Facebook': 12.11,
        'Intel': 40.51, 'Atmel': 10.23, 'Amazon': 305.35, 'Google': 535.81
    }

    s_100 = {k: v for k, v in stock.items() if v > 100}

    print("s_100 = {}".format(s_100))


'''

s_100 = {'Apple': 655.95, 'IBM': 202.13, 'Amazon': 305.35, 'Google': 535.81}

'''
