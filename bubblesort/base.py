# Bubble Sort Algorithm

nums = [10, 9, 8, 7, 6, 5]
print(f"PRE-SORT: {nums}")


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp



def bubble_sort_unoptimized(arr):
    iteration_count = 0

    for el in arr:
        for index in range((len(arr) - 1)):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)


def bubble_sort(arr):
    iteration_count = 0

    for i in range(len(arr) - 1):
        for idx in range(len(arr) - i - 1):
            iteration_count += 1

            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print(f"Iteration count: {iteration_count}")

# bubble_sort_unoptimized(nums)
bubble_sort(nums)
print(nums)