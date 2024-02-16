#linear search iteratively
def linearSearch(arr, target):
    for elm in arr:
        if elm == target:
            return arr.index(elm)

    return None

# Testing code
li = [2,34,5,5,7,89,6,62,14,25,4,78,76,345,2,56,38,6,78,35,4,68]
print(linearSearch(li,4))