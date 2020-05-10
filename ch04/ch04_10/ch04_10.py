def is_validmat(mat):
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            return False
    return True

def flatten(list2d):
    result = []
    for x in list2d:
        result.extend(x)
    return result

def SUMPRODUCT(arr1, arr2):
    if len(arr1) == len(arr2):
        result = 0
        for i in range(len(arr1)):
            result += (arr1[i] * arr2[i])
        return result
    else:
        print('len(arr1) != len(arr2)')
        return None

def MMULT(A, B):
    print('A = ' + str(A))
    print('B = ' + str(B))
    if not (is_validmat(A) and is_validmat(B)):
        print('Invalid input!\n')
        return None
    elif len(A[0]) != len(B):
        print('Invalid input!\n')
        return None
    else:
        print('A * B = ', end='')
    
    b = flatten(B)
    result = []

    for i in range(len(A)):
        temp = []
        arr1 = A[i]
        for j in range(len(B[0])):
            arr2 = [b[x] for x in range(j, len(b), len(B[0]))]
            temp.append(SUMPRODUCT(arr1, arr2))
        result.append(temp)
    print(str(result) + '\n')
    return None

if __name__ == '__main__':
    mat0 = [[1, 3, -1], [3, 0, -2, 1], [1, 4, 2]]
    mat1 = [[1, 3, -1], [3, 0, -2], [1, 4, 2]]
    mat2 = [[2, 3], [1, 0], [5, 4]]
    mat3 = [[2, 1], [3, 4]]

    MMULT(mat0, mat1)
    MMULT(mat1, mat0)
    MMULT(mat2, mat1)
    MMULT(mat1, mat2)
    MMULT(mat3, mat3)