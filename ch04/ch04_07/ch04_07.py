def group(iterable, size):
    result = []
    li = list(iterable)
    length = len(li)
    for i in range(0, length, size):
        result.append(li[i:i+size])
    return result

def group2(iterable, size):
    result =[] # 先準備將要回傳的串列，初始狀態為空
    it = iter(iterable) # 與 group 函式不同，這裡用 iterable 型態
    while True: # 設定無窮迴圈
        temp = [] # 設定暫存用的串列，每一輪串列都會在這裡被清空
        try: # 在使用 next 時，我們預期他會在取出最後一個元素後引發異常
            for _ in range(size): # 利用迴圈取出指定數量元素，因這裡我們只要次數而非迭代的值，故使用底線(_)
                temp.append(next(it)) # 依序將元素放入 temp 中，直到指定 size
            result.append(temp) # 再將取出的串列附加到 result
        except StopIteration: # 當取完全部元素後引發異常，用 except 捕捉 StopIteration
            if temp != []: # 確定 temp 有值，
                result.append(temp) # 才將值附加到 result 內
            break # 用 break 離開迴圈
    return result # 回傳結果