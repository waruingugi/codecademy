# Merge Sort

def merge_sort(items):
    if len(items) <= 1:
        return items
    
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right
    
    return result

unordered_list = [3, 7, 9, 2, 1, 6, 5]
print(merge_sort(unordered_list))
