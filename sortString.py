import random

def partition(s_list,low,high):

    #move pivot to proper position in the array
    i = low-1
    pivot_index = high
    pivot = s_list[pivot_index]
    for j in range(low,high):
        if s_list[j] <= pivot:
            i = i+1
            s_list[i],s_list[j] = s_list[j],s_list[i]
    s_list[i+1],s_list[pivot_index] = s_list[pivot_index],s_list[i+1]
    return i+1

def randomPivot(s_list,low,high):
    
    #generate a random pivot using Lomuto partitioning (inspired by https://www.geeksforgeeks.org/quicksort-using-random-pivoting/)
    rand = random.randrange(low,high)
    s_list[rand], s_list[high] = s_list[high], s_list[rand]
    return partition(s_list,low,high)

def quickSort(s_list,low,high):

    #RECURSIVE QUICK SORT
    if low < high:
        part = randomPivot(s_list,low,high)
        quickSort(s_list,low,part-1)
        quickSort(s_list,part+1,high)

def sortStringList(s_list):
    #driver method for unit testing
    quickSort(s_list,0,len(s_list)-1)
    return s_list
