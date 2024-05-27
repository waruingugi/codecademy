# In binary search, the inputs are always sorted.
# So we divide the list in half and compare our target with the middle element.
# If they match, we return the index
# If they don't match, we begin again at the first step with the appropriate
# half of the original list.
# When the list is empty, the target is not found


def binary_search(
    sorted_list, left_pointer, right_pointer, target
):
    if left_pointer >= right_pointer:
        return "Value not found"
    
    # We calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    
    if mid_val > target:
        # We reduce the sub-list by passing in a new right_pointer
        return binary_search(
            sorted_list, left_pointer, mid_idx, target
        )
    
    if mid_val < target:
        # We reduce the sub-list by passing in a left_pointer
        return binary_search(
            sorted_list, mid_idx + 1, right_pointer, target
        )
