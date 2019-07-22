'''

Given an array of positive integers find the subarray that sums to X

Q How to return output
Q What to return if the array is empty
Q What to return if the no subarray is found
Q What to do if there are multiple subarray

'''

a = [2,6,4,7,0,3]
x = 14

def solution(array):
    start = 0
    end = -1
    sum = 0
    print('length of a = {}'.format(len(a)))
    while start< len(a):

        if sum < x:
            end = end +1
            if end < len(a):
                sum = sum + a[end]
            else:
                print('end pointer reached the end of the array and no solution is reached')
                print('start pointer is at index {}'.format(start))
                break





        elif sum > x :
            if start<len(a):
                sum = sum - a[start]
                start =  start + 1
            else:
                print('there was no sub array with sum equal to x')
                break

        else :
            print('Solution is reached \nstart index = {}'.format(start))
            print('end index = {}'.format(end))
            break



