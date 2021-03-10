l = [1,8,4,9,21,42,13,15,7,22,43]
l.sort()
x = 21

def binary_sort_iterative(l,x):
    left = 0
    right = len(l) - 1
    while left <= right:
        # Why use left + ((right - left) // 2) since it equals (right + left) / 2? 
        # For Languages such as C++, C# and Java will be overflowed if (left + right) > 2147483647
        # For JavaScript, it will fail because (1+2)/2 = 1.5 not 1 
        # Python handles this fine 
        mid = left + ((right - left) // 2) 
        if l[mid] == x:
            return True
        elif x < l[mid]:
            right = mid - 1 
        else:
            left = mid + 1 
    return False

print(binary_sort_iterative(l,x))
