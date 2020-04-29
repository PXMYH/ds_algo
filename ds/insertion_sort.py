import random
def insertionSort(nums):
    '''
    iterate through the array and swap the elements if current element is larger than next
    '''
    for i in range(1,len(nums)):
        for j in range(i, 0, -1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1] # swap elements
    return nums

def binaryInsertionSort():
    pass

# driver code
nums = random.sample(range(1, 1000000000000), 100000000000)
# nums = [4,3,2,1,8,5,6,12,31,23,42,12]
print(f"input = {nums}")
res = insertionSort(nums)
print(f"res = {res}")
