'''

Given an array of integers , can be positive or negative , find the contiguous sub - array whose sum is maximum

Questions:
- How do you want the output
- Can the subarray be a empty array

'''


# Brute force approach

def brute_force(array):
    max_array_start , max_array_end = 0
    curr_sum , max_sum = 0

    for i in range(len(a)):
        for j in range(i , len(a)):
            curr_sum = curr_sum + a[j]

            if curr_sum >max_sum:
                max_sum = curr_sum
                max_array_start = i
                max_array_end  = j


    print('max sub array starts at index {} and ends at index j'.format(max_array_start, max_array_end))
    print('max sub array sum is ={}'.format(max_sum))


# Kadane algorithm

'''
max sum at index i = max( 0 , max sum at index(i-1) + a[i] )
This algorithm has O(n) time complexity
 
'''
a = [-1,2,-1,3,4,-5,-3]

def kadane_algorithm(a):
    max_sum = 0
    max_sum_ending = 0
    final_index = -1
    for i in range(len(a)):
        max_sum_ending = max(0, (max_sum_ending + a[i]))
        if max_sum_ending > max_sum:
            max_sum = max_sum_ending
            final_index = i

    print('max sum for sub-array is {}'.format(max_sum))
    print('final index where we achieve max sum is {}'.format(final_index))


kadane_algorithm(a)
