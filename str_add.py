def str_add(str1, str2, n):
    """
    实现字符串数字不同进制下相加
    :param str1: 字符串1
    :param str2: 字符串2
    :param n: 进制
    :return:
    """
    result_str = ""
    flag = 0
    str1_len = len(str1)
    str2_len = len(str2)
    max_len = max(str1_len, str2_len)
    if str1_len < str2_len:
        str1 = "0" * (str2_len - str1_len) + str1
    if str1_len > str2_len:
        str2 = "0" * (str1_len - str2_len) + str2

    while max_len > 0:
        i = int(str1[max_len-1]) + int(str2[max_len-1]) + flag
        if i >= n:
            flag = 1
            i = i % n
            result_str = str(i) + result_str
            max_len -= 1
            if max_len == 0:
                result_str = "1" + result_str
        else:
            flag = 0
            result_str = str(i) + result_str
            max_len -= 1

    print(result_str)
    # print(str(int(result_str)))


str_add("11", "1", 10)