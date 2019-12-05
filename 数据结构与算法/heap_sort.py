def heap_sort(arr):
    if len(arr) < 2:
        return arr
    size = len(arr)

    for i in range(size):
        # 构造大根堆(每个子树的父节点都是该子树的最大值)
        heap_insert(arr, i)
    size -= 1
    arr[0], arr[size] = arr[size], arr[0]

    while size > 0:
        heap_helper(arr, 0, size)
        size -= 1
        arr[0], arr[size] = arr[size], arr[0]


def heap_insert(arr, index):
    while arr[index] > arr[(index - 1) // 2] and index > 0 and ((index - 1) // 2) > 0:
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2


def heap_helper(arr, index, size):
    # 如果存在子节点且大于父节点就交换,然后退出循环
    left = 2 * index + 1
    while left < size:
        # 先比较左右节点
        largest = left + 1 if (left + 1) < size and arr[left + 1] > arr[left] else left
        # 和第一个父节点比
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break  # 大根堆若第一个都小 那么就直接退出循环
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = 2 * index + 1


arr = [10, 7, 1, 8, 9, 5, 0, 0, 1]
heap_sort(arr)
print(arr)
