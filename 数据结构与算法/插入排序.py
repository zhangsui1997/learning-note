def insert_sort(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(i + 1, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = i - 1
        while index >= 0 and key < arr[index]:
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = key
    return arr


print(insertionSort([1, 1, 1, 2, 3, 1, 5, 6, 7, 8, 1, 10, 2]))
