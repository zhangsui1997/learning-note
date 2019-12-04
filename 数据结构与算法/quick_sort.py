# arr[] --> 排序数组
# left  --> 起始索引
# right  --> 结束索引


def partition(arr, left, right):
    less = left - 1
    pivot = arr[right]
    for i in range(left, right):
        if arr[i] <= pivot:
            less += 1
            arr[i], arr[less] = arr[less], arr[i]
    less += 1
    arr[less], arr[right] = arr[right], arr[less]
    return less


def quick_sort(array, low, high):
    if low < high:
        mid = partition(array, low, high)
        quick_sort(array, low, mid - 1)
        quick_sort(array, mid + 1, high)


arr = [10, 7, 8, 9, 1, 0, 5, 1, 0]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("排序后的数组:", arr)
