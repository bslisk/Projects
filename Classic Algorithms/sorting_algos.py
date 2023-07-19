# Implement two types of sorting algorithms: Merge sort and bubble sort.
from random import randint


def merge(array_1, array_2):
    merged = []
    # Pointers for each array
    i = 0
    j = 0
    # If one array has been fully iterated over, break loop
    while i != len(array_1) and j != len(array_2):
        if array_1[i] < array_2[j]:
            merged.append(array_1[i])
            i += 1
        else:
            merged.append(array_2[j])
            j += 1
    if i != len(array_1):  # And add the remainder of the other array to the output, as they are both already sorted
        merged += array_1[i:]
    elif j != len(array_2):
        merged += array_2[j:]
    return merged


def merge_sort(to_sort: list[int]) -> list[int]:
    if len(to_sort) < 2:  # Base case: if array contains 1 item, stop splitting and begin merging
        return to_sort
    halfway_point = len(to_sort) // 2
    left = merge_sort(to_sort[:halfway_point])
    right = merge_sort(to_sort[halfway_point:])
    return merge(left, right)


def bubble_sort(to_sort: list[int]) -> list[int]:
    lst = to_sort[:]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]  # Keep swapping elements until array is sorted
                sorted = False  # If the array is sorted, this will not be called and the while loop will break
    return lst


to_sort = [randint(-100, 100) for _ in range(10)]  # Initializing randomly generated array to sort
print('Unsorted:')
print(to_sort)
print('\n')

print('Bubble sort:')
sorted_bubblesort = bubble_sort(to_sort)
print(sorted_bubblesort)
print(f'Sorted: {sorted(to_sort) == sorted_bubblesort}')
print('\n')

print('Merge sort:')
sorted_mergesort = merge_sort(to_sort)
print(sorted_mergesort)
print(f'Sorted: {sorted(to_sort) == sorted_mergesort}')
