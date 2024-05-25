from random import randrange, shuffle


def quicksort(list, start, end):
    if start > end:
        return

    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]

    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # Tracks all elements which should be to the left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # If we found an element out of place
        if list[i] < pivot_element:
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1

    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

    # Recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)

    return list



list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)
