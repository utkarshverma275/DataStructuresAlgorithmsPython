'''
Given an array of integers both +ive and -ive . Find a contiguous subarray that sums to zero.

Q What form to return input
Q What to return if array is empty
Q What to return if no subarray is found
Q What to do if there are multiple subarrays

algorithm is the diff technique

for eg array is [2,4,-2,1,-3,5,-3]

then we calculate the array which sums to a, continuous array
original array : [2, 4, -2, 1, -3, 5, -3]
Diff array     : [2, 6, 4, 5,   2, 7, 4]

The logic for finding an array that sums to zero is : If an element in the diff array repeats then it means that
the indices (in the original array) canceled out and hence the sum dropped to a previous value
In the above example the sum follows the pattern 2..6..4..5..2 Here the sum started from 2 and ended at 2
which means that the elements between 2nd position and the 5th position sum to zero

'''

a = [2, 4, -2, 1, -3, 5, -3]

counter = {}
start = 0
sum = 0

while start<len(a):
    sum = sum + a[start]

    if sum in counter:
        print('we found subarray that sums to zero')
        print('arrays start at {} and ends at {}'.format(counter[sum]+1, start))
    else:
        counter[sum] = start


    start+= 1