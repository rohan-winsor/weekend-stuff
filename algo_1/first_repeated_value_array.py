def first_repeated_value(arr):
    out = {}
    for i in arr:
        if i not in out.keys():
            out[i] = 1
        else:
            return i
print(first_repeated_value([2,3,4,5]))