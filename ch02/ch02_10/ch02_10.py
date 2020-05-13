if __name__ == '__main__':
    import random


    def search_db(num, db):
        for i in db:
            if i == num:
                return True
            else:
                return False
    

    def inters(a, b):
        db = []
        for i in a:
            if not search_db(i, db):
                for j in b:
                    if i == j:
                        db += [j]
                        break
            else:
                continue
        return db
    

    li0 = []
    li1 = []

    for i in range(0, 10):
        li0 += [random.randint(1, 100)]
        li1 += [random.randint(1, 100)]
    
    print('li0 = ' + str(li0))
    print('li1 = ' + str(li1))

    myinters = inters(li0, li1)
    print('inters = ' + str(myinters))


'''

li0 = [2, 56, 95, 28, 72, 66, 25, 19, 4, 81]
li1 = [58, 38, 39, 30, 92, 62, 29, 51, 34, 40]
inters = []

li0 = [100, 67, 36, 39, 44, 22, 32, 100, 52, 65]
li1 = [60, 76, 54, 17, 11, 60, 58, 100, 6, 99]
inters = [100]

'''
