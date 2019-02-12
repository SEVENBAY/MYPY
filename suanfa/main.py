# coding=utf8
import random
import sys
import copy
from utils import half_find, bubble_sort, bubble_better, choice_sort, insert_sort, quick_sort, heap_sort, merge_sort, \
    shell_sort

# 为快速排序设置递归深度，否则会超出递归深度而报错
sys.setrecursionlimit(10000)

# 生成序列
a = range(10000)
random.shuffle(a)
l1 = copy.copy(a)
l2 = copy.copy(a)
l3 = copy.copy(a)
l4 = copy.copy(a)
l5 = copy.copy(a)
l6 = copy.copy(a)
l7 = copy.copy(a)
l8 = copy.copy(a)

# 各排序算法执行
r1 = bubble_sort(l1)  # 冒泡排序(O(N**2))
r2 = bubble_better(l2)  # 冒泡排序优化(O(N**2))
r3 = choice_sort(l3)  # 选择排序(O(N**2))
r4 = insert_sort(l4)  # 插入排序(O(N**2))
r5 = quick_sort(l5)  # 快速排序(O(n*logn))
r6 = heap_sort(l6)  # 堆排序(O(n*logn))
r7 = merge_sort(l7)  # 归并排序(O(n*logn))
r8 = shell_sort(l8)  # 希尔排序(O(1.3n))

# 二分查找执行
r9 = half_find(r6, random.randint(0, len(a)))
