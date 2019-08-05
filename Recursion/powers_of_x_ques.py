'''
Find the result of X^y in O(logn) time complexity

Explanation
if n is even
X^n = X^(n/2) * X^(n/2)

if n is odd
X^n = X * X^(n//2) * X(n//2)

'''

def power(X,n):
    #base:
    if n==1:
        return X
    if n==0:
        return 1
    if n==-1:
        return (1/X)

    #recursion
    if n%2==0:
        return power(X,n/2)*power(X , n/2)
    elif n<0:
        return (1/X)*power(X,n//2)*power(X,n//2)
    else:
        return X*power(X, n//2)*power(X, n//2)


y = power(2, -2)

print(y)
