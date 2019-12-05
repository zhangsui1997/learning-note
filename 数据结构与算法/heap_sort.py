arr = [10, 7, 1, 8, 9, 5, 1]


def heap_sort(arr):
    if len(arr) < 2:
        return arr
    size = len(arr)
    for i in range(size):
        heap_insert(arr, i)

    size -= 1
    arr[0], arr[size] = arr[size], arr[0]

    for i in size[::-1]:
        heap_helper(arr, i)
        arr[0], arr[i] = arr[i], arr[0]


def heap_insert(arr, index):
    while arr[index] > arr[(index - 1) // 2] and index > 0 and ((index - 1) // 2) > 0:
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2


def heap_helper(arr, index, size):
    # 如果存在子节点且大于父节点就交换,然后退出循环
    while arr[(index - 1) // 2]


heap_sort(arr)
print(arr)
