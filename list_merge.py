l1 = [1, 3, 5, 7, 9, 11, 18, 22]
l2 = [2, 3, 4, 6, 8, 16, 23]
def merge(list1, list2):
    """
    合并有序列表
    :param list1: 列表1
    :param list2: 列表2
    :return: 新列表
    """

    result_list = []
    while list1 and list2:
        if list1[0] > list2[0]:
            result_list.append(list2[0])
            del list2[0]
        elif list1[0] < list2[0]:
            result_list.append(list1[0])
            del list1[0]
        else:
            result_list.append(list1[0])
            result_list.append(list2[0])
            del list1[0]
            del list2[0]
    if list1:
        result_list.extend(list1)
    elif list2:
        result_list.extend(list2)

    print(result_list)


merge(l1,l2)