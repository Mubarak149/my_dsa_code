#linear search iteratively
def linearSearch(arr, target):
    for elm in arr:
        if elm == target:
            return arr.index(elm)

    return None

#recursive version
def linearSearch2(arr, target, ind=0):
    targetIndex = 0
    if len(arr) > ind:
        if arr[ind] == target:
            targetIndex = arr.index(target)
            return targetIndex
        else:
            targetIndex = linearSearch2(arr, target,ind + 1)
            return targetIndex
        return targetIndex
    else:
        return None




# Testing code

"""
li = [2,34,5,5,7,89,6,62,14,25,4,78,76,345,2,56,38,6,78,35,4,68]
print(linearSearch(li,4))
print(linearSearch2(li,68))
"""
