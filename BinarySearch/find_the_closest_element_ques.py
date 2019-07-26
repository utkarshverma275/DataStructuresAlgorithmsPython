'''
Given a sorted array find the target , if the target is not found return the closest element

A = [1,2,3,8, 9, 12] ; target 6
return 8

We modify the binary search algorithm to find the closest member to the target by recording the mid element
in each iteration of the binary search and updating it in each iteration by measuring distance from target

'''


def record(arr , mid, result ,  target):

    if result==-1 or abs(arr[mid] - target)<abs(arr[result] - target):
        return mid
    else:
        return result

def find_closest(arr, target):
    result = -1
    start = 0
    end = len(a)-1
    while start<=end:
        mid = start + (end-start)//2
        result = record(arr, mid, result, target)
        if mid<target:
            start = mid+1
        elif mid>target:
            end= mid-1
        else:
            return target

    return result

