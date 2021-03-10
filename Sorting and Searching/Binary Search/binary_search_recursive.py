l = [1,8,4,9,21,42,13,15,7,22,43]
l.sort()
x = 21

def binary_sort_recursive(l, x, left, right):
    if left > right:
        return False

    # Why use left + ((right - left) // 2) since it equals (right + left) / 2? 
    # For Languages such as C++, C# and Java will be overflowed if (left + right) > 2147483647
    # For JavaScript, it will fail because (1+2)/2 = 1.5 not 1 
    # Python handles this fine 
    mid = left + ((right - left) // 2) 
    if l[mid] == x:
        return True
    elif x < l[mid]:
        return binary_sort_recursive(l, x, left, mid - 1)
    else:
        return binary_sort_recursive(l, x, mid + 1, right)
