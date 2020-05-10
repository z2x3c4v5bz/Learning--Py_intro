def x(li):
    return li[1]

if __name__ == '__main__':
    data = [('John', 40, 174, 65), ('Amy', 28, 165, 44), ('Jessie', 32, 158, 45)]

    print(sorted(data, key=x))


'''
[('Amy', 28, 165, 44), ('Jessie', 32, 158, 45), ('John', 40, 174, 65)]
'''
