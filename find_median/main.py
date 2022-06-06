def quicksort(l, r, nums):
    if (l < r):
        pi = partition(l, r, nums)

        quicksort(l, pi - 1, nums)
        quicksort(pi + 1, r, nums)


def partition(l, r, nums):
    pivot = nums[r]
    pointer = l - 1

    for j in range(l, r):
        if nums[j] < pivot:
            pointer += 1
            nums[pointer], nums[j] = nums[j], nums[pointer]

    nums[pointer + 1], nums[r] = pivot, nums[pointer + 1]
    return pointer + 1


if __name__ == '__main__':
    arr = [10, 80, 30, 90, 40, 50, 70]
    print('before', arr)
    quicksort(0, len(arr) - 1, arr)
    print('after', arr)
