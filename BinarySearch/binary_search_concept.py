'''

Binary search is a technique to search for an element in an array etc.
This technique can be applied to only sorted arrays
Time complexity O(logn)
Divides the decision by half in every iteration
'''

def binary_search(l:list, target:int) -> int:
    '''
    This method performs a binary search on "sorted" list l and returns the index of the target element.
    If target is not found it returns -1
    :param l: Sorted list of integers
    :param target: Target int to find in the list l
    :return: Index of the Target ; -1 implies invalid input ; -2 implies target not found
    '''

    if l is None or target is None or not isinstance(target , int):
        return -1

    else:
        start = 0
        end = len(l) - 1

        while start<=end:
            mid = start + (end - start)//2
            if l[mid]>target:
                end = mid-1
            elif l[mid]<target:
                start = mid+1
            else:
                return mid

    return -2


# test
print(binary_search([6,10,12,24,30,35,40], 10))