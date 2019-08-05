'''
Questions is to print all possible combinations of length X from the elements of an array
Array  = [1,2,3,4,5,6,7]
Print all combinations of length 3
(1,2,3) ; (1,2,4) ; (1,2,5) ; .... (5,6,7)


'''

def print_combo(a , X):
    if (a==None) or (len(a)==0) or (X>len(a)):
        return

    buffer = [None]*X
    print_combo_helper(a , buffer , 0,0 , X)


def print_combo_helper(a , buffer,start_index , buffer_index ,X):
    #define terminal cases
    if buffer_index==X:
        print(buffer)
        return

    if start_index==len(a):
        return


    # find the candidate to start
    i= start_index
    while i<len(a):
        buffer[buffer_index] = a[i]

        print_combo_helper(a ,buffer , i+1 , buffer_index+1 ,X)
        i+=1



a = [1,2,3,4,5,6,7,8,9]
X = 2
print_combo(a, X)


