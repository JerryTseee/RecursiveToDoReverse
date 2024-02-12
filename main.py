"""
Design a recursive algorithm for reversing the entries
in an array and analyze the time complexity of your
algorithm.
"""
def reverse(n):
    length = len(n)
    if length == 1:
        return n
    else:
        return reverse(n[1:])+[n[0]]
    
n = [1,2,3]
print(reverse(n))

"""
for f(n)
n=1: C1
otherwise: f(n-1)+C2

Therefore, the time complexity = n
"""
