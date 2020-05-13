if __name__ == '__main__':
    arr = [9, 5, 5, -4, 7, 6, 4, 1, -2, 0, 10, 9, 7]
    
    onlyone = [num for num in arr if arr.count(num) == 1]
    print(onlyone)


'''

[-4, 6, 4, 1, -2, 0, 10]

'''
