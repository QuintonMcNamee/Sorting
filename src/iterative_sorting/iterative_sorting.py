# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # 1. Start with current index = 0
    cur_index = 0
    smallest_index = 0
    # 2. For all indices EXCEPT the last index:
    # a. Loop through elements on right-hand-side
    # of current index and find the smallest element
    for x in range(len(arr)):
        cur_index = x
        smallest_index = cur_index
        for i in range(x+1, len(arr)):
            if arr[smallest_index] > arr[i]:
                smallest_index = i
    
        # b. Swap the element at current index with the
        # smallest element found in above loop
        temp = arr[x]
        arr[x] = arr[smallest_index]
        arr[smallest_index] = temp
 
    return arr
        


    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             

        # TO-DO: swap



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if arr == []:
        return arr
        
    looped_counter = 0
    # 1. Loop through your array
    for x in arr:
        for index in range(0, len(arr)-1):
    #     - Compare each element to its neighbor
            if arr[index] > arr[index+1]:
    #     - If elements in wrong position (relative to each other, swap them)
                looped_counter += 1
                temp = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = temp
    # 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        if looped_counter == 0:
            return arr
        else:
            looped_counter = 0


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr