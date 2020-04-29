def partition(left, right, pivot_index):
    pivot = nums[pivot_index]
    # 1. move pivot to end
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    # 2. move all smaller elements to the left
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    # 3. move pivot to its final place
    # remember, at this time, pivot is at the end of the array
    # because we swapped it at the start of partitioning algo
    nums[right], nums[store_index] = nums[store_index], nums[right]

    return store_index
