list1 = [45, 38, 1, 17, 44, 23, 10, 48]
list = [45, 38, 1, 17, 44, 23, 10, 48, 25, 3, 30, 13, 4, 14, 21]
#min_index = 0
loop_time = 0
for i in range(len(list)):
    min_index = i
    for j in range(i+1,len(list)):
        loop_time += 1
        if list[j]<list[min_index]:
            min_index = j
    list[i],list[min_index] = list[min_index],list[i]
    #min_index += 1
    print(list)

#print(list)