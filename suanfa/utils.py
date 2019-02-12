# coding=utf8
import time


# 计算算法执行时间装饰器
def use_time(func):
    def use_time_inner(*args, **kwargs):
        begin_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        global t
        t = end_time - begin_time
        print('use time(%s):%ss' % (func.__name__, t))
        return f
    return use_time_inner


# 二分查找算法
@use_time
def half_find(array, data):
    begin = 0
    end = len(array) - 1
    while begin <= end:
        mid = (begin+end) // 2
        if array[mid] == data:
            return '%s founded at %s' % (data, mid)
        elif array[mid] > data:
            end = mid - 1
        else:
            begin = mid + 1
    return 'not found'


# 冒泡排序算法
@use_time
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# 冒泡算法优化
# 遍历一遍，如果没有交换的元素，证明序列已经有序，则直接结束
@use_time
def bubble_better(array):
    for i in range(len(array)-1):
        exchange = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                exchange = True
        if not exchange:
            break
    return array


# 选择排序算法
@use_time
def choice_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# 插入排序算法
@use_time
def insert_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


# 快速排序算法
# 快速排序中的一次调整，即将第一个元素放在某个位置，使该元素右边的元素都比该元素大，左边的元素都比该元素小
def query_mid(array, left, right):
    tmp = array[left]
    while left < right:
        while left < right and tmp <= array[right]:
            right -= 1
        array[left] = array[right]
        while left < right and tmp >= array[left]:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    return left


# 应用递归实现快速排序
def _quick_sort(array, left, right):
    if left < right:
        mid = query_mid(array, left, right)
        _quick_sort(array, left, mid-1)
        _quick_sort(array, mid+1, right)
    return array


# 装饰器不应该直接装饰递归函数，应该再次封装一层
@use_time
def quick_sort(array):
    return _quick_sort(array, 0, len(array)-1)


# 堆排序算法
# 构建堆的调整过程
def shift(array, low, high):
    tmp = array[low]
    i = low
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and array[j] < array[j + 1]:
            j += 1
        if tmp < array[j]:
            array[i] = array[j]
            i = j
            j = 2 * i + 1
        else:
            break
    array[i] = tmp


@use_time
def heap_sort(array):
    n = len(array)
    # 将array构造成大顶堆
    for i in range(n//2-1, -1, -1):
        shift(array, i, n-1)
    # 从堆顶开始取数
    for i in range(n):
        array[0], array[n-1-i] = array[n-1-i], array[0]
        shift(array, 0, n-i-2)
    return array


# 归并排序算法
# 一次归并排序
def merge(array, low, mid, high):
    tmp_list = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if array[i] < array[j]:
            tmp_list.append(array[i])
            i += 1
        elif array[i] > array[j]:
            tmp_list.append(array[j])
            j += 1
        else:
            tmp_list.append(array[i])
            i += 1
    if j <= high:
        for num in array[j:high+1]:
            tmp_list.append(num)
    if i <= mid:
        for num in array[i:mid+1]:
            tmp_list.append(num)
    array[low:high+1] = tmp_list
    return array


# 应用递归实现归并排序
def _merge_sort(array, low, high):
    if low < high:
        mid = (low+high) // 2
        _merge_sort(array, low, mid)
        _merge_sort(array, mid+1, high)
        merge(array, low, mid, high)
    return array


# 装饰器不应该直接装饰递归函数，应该再次封装一层
@use_time
def merge_sort(array):
    return _merge_sort(array, 0, len(array)-1)


# 希尔排序算法
@use_time
def shell_sort(array):
    gap = len(array) // 2
    while gap >= 1:
        for i in range(gap, len(array)):
            tmp = array[i]
            j = i - gap
            while j >= 0 and array[j] > tmp:
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = tmp
        gap = gap / 2
    return array
