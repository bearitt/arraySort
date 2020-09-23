
def sortIntegerList(list):

    # INSERTION SORT
    
    for i in range(0,len(list)):
        item = list[i]
        count = i - 1
        while count >= 0 and (list[count] > item):
            list[count+1] = list[count]
            count -= 1
        list[count+1] = item
    return list
