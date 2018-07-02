list = [45, 38, 1, 17, 44, 23, 10, 48, 25, 3, 30, 13, 4, 14, 21]
loop_time = 0
for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            loop_time += 1
            print(list, loop_time)
