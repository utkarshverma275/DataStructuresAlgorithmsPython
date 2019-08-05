'''
Recursive problems
All recursive algorithms have the following:
- base case
- working towards a base case
- recursive step

For each function call recursion uses space on the memory stack. Space complexity is O(n) and time Complexities is exponential

Recursion is when a function  calls itself
A typical problem hello world problem for recursive algorithms is finding the nth element in a fibonacci series
1,1,2,3,5,8,13...
This can be understood as t(n) = t(n-1) + t(n-2)
Eg find the 5th term of the fibonacci series
Finding the pattern - > every term in the fibonacci series is the sum of two previous terms
Base case => t(2)=1    ; t(1)=1
t(5) =       t(4)           +         t(3)
         t(3)   +  t(2)     +     t(2) +  t(1)
       t(2)+t(1)
t(5) = t(2)+t(1) + t(2)     +     t(2) + t(1)
t(5) = 1   +  1  +  1       +      1   +  1
t(5) = 5

'''

def find_fibo_n(n):
    # base case
    if n==0:
        return None

    if n==1:
        return 1
    if n==2:
        return 1

    # recursive step

    return find_fibo_n(n-1) + find_fibo_n(n-2)


nth_fibo = find_fibo_n(8)
print(nth_fibo)