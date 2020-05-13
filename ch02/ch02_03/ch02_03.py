if __name__ == '__main__':
    scores = [30, 99, 41, 55, 84]
    scores_new = []

    for x in scores:
        if x >= 90:
            scores_new += [x]
        else:
            x += 10
            if x >= 90:
                x = 90
            scores_new += [x]
    
    print(scores_new)


'''

[40, 99, 51, 65, 90]

'''
