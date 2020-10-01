# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        rest_of_list = arr[i:]
        next_smallest_i = rest_of_list.index(min(rest_of_list)) + i
        # swap
        current = arr[i]
        arr[i] = arr[next_smallest_i]
        arr[next_smallest_i] = current

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        times_swapped = 0
        for i in range(len(arr)-1):
            first = arr[i]
            second = arr[i+1]
            if first > second:
                arr[i] = second
                arr[i+1] = first
                times_swapped += 1
        if times_swapped is 0:
            swapped = False


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # exception for empty list
    if len(arr) is 0:
        return []
    # get max if none is provided
    if not maximum:
        maximum = max(arr)
    # error message if there are negative numbers in arr
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    # create buckets for all possible values in arr
    buckets = [0] * (maximum + 1)
    # count the values
    for x in arr:
        buckets[x] += 1
    # created a sorted array using the numbers from buckets as indeces
    for i in range(1, len(buckets)):
        buckets[i] += buckets[i-1]
    output = [0] * len(arr)
    for x in arr:
        output[buckets[x]-1] = x
        buckets[x] -= 1

    return output
