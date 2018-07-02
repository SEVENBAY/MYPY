list = [1, 3, 4, 10, 13, 14, 17, 21, 23, 25, 30, 38, 44, 45, 48]
def half_look(array, num):
    low = 0
    high = len(array)
    while low <= high:
        half = (high + low) // 2
        if num == array[half]:
            print("找到了",half)
            return
        elif num > array[half]:
            low = half+1
        else:
            high = half-1
    print("没找到")

half_look(list, 4)
