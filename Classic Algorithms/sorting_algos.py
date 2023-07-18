# Implement two types of sorting algorithms: Merge sort and bubble sort.
from random import randint


def merge_sort(to_sort: list[int]) -> None:
    pass


def bubble_sort(to_sort: list[int]) -> list[int]:
    lst = to_sort[:]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                sorted = False
    return lst


to_sort = [randint(-100, 100) for x in range(10)]
print('Unsorted:')
print(to_sort)
print('\n')

print('Bubble sort:')
sorted_bubblesort = bubble_sort(to_sort)
print(sorted_bubblesort)
print(f'Sorted: {sorted(to_sort) == sorted_bubblesort}')
print('\n')

# print('Merge sort:')
# sorted_mergesort = merge_sort(to_sort)
# print(sorted_mergesort)
# print(f'Sorted: {sorted(to_sort) == sorted_mergesort}')
