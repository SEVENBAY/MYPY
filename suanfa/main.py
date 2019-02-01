# coding=utf8
import random
import sys
import copy
from utils import half_find, bubble, bubble_better, choice, insert_sort, quick_sort, heap_sort

# 为快速排序设置递归深度，否则会超出递归深度而报错
sys.setrecursionlimit(1000)

# 生成序列
a = range(1000)
random.shuffle(a)
l1 = copy.copy(a)
l2 = copy.copy(a)
l3 = copy.copy(a)
l4 = copy.copy(a)
l5 = copy.copy(a)
l6 = copy.copy(a)

# 各排序算法执行
r1 = bubble(l1)  # 冒泡排序(O(N**2))
r2 = bubble_better(l2)  # 冒泡排序优化(O(N**2))
r3 = choice(l3)  # 选择排序(O(N**2))
r4 = insert_sort(l4)  # 插入排序(O(N**2))
r5 = quick_sort(l5)  # 快速排序(O(n*logn))
r6 = heap_sort(l6)  # 堆排序(O(n*logn))

# 二分查找执行
r7 = half_find(r6, random.randint(0, len(a)))
