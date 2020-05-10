def under60_A(li):
    result = []
    for student in li:
        if student[1] < 60:
            result.append(student)
    return result

def under60_B(li):
    return [student for student in li if student[1] < 60]

if __name__ == '__main__':
    li = [('Jhon', 33), ('Elsa', 63), ('Amy', 60), ('Bill', 73), ('Mary', 59), ('Zachary', 93)]
    print(under60_A(li))
    print(under60_B(li))