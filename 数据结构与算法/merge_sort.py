# 归并排序
def sort_process(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = sort_process(arr[:mid])
    right = sort_process(arr[mid:])
    return merge_sort(left, right)


def merge_sort(left, right):
    p1 = p2 = 0
    help = []
    while (p1 < len(left)) and (p2 < len(right)):
        if left[p1] < right[p2]:
            help.append(left[p1])
            p1 += 1
        else:
            help.append(right[p2])
            p2 += 1
    if left:
        help+=left[p1:]
    if right:
        help+=right[p2:]
    return help

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 0, 1, 2, 4, 3]
    print(sort_process(arr))
