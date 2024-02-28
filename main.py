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

#another recursion method:
"""
def reverse_array_in_place(arr, start, end):
    if start >= end:
        return  # Base case: array is reversed
    # Swap elements at start and end positions
    else:
        arr[start], arr[end] = arr[end], arr[start]
        # Recurse with updated pointers
        reverse_array_in_place(arr, start + 1, end - 1)
        return arr

# Example usage:
array = [10, -2, 3, 4, 5]
n = len(array)
print(reverse_array_in_place(array, 0, n - 1))
"""
