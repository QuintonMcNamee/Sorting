import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr

# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        middle = math.floor(len(arr)/2)
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        index_1 = 0
        index_2 = 0
        index_3 = 0

        while index_1 < len(left) and index_2 < len(right):
            if left[index_1] < right[index_2]:
                arr[index_3] = left[index_1]
                index_1 += 1
            else:
                arr[index_3] = right[index_2]
                index_2 += 1
            index_3 += 1

        while index_1 < len(left):
            arr[index_3] = left[index_1]
            index_1 += 1
            index_3 += 1

        while index_2 < len(right):
            arr[index_3] = right[index_2]
            index_2 += 1
            index_3 += 1
    print(arr)
    return arr

merge_sort([4, 3, 5, 1, 9])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
