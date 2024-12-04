def mergeSort(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    # Recursively sort the left and right halves
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)

    # Merge the sorted halves
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    p1 = low
    p2 = mid + 1

    # Merge the two halves
    while p1 <= mid and p2 <= high:
        if arr[p1] < arr[p2]:
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2 += 1

    # Add remaining elements from the left half
    while p1 <= mid:
        temp.append(arr[p1])
        p1 += 1

    # Add remaining elements from the right half
    while p2 <= high:
        temp.append(arr[p2])
        p2 += 1

    # Copy sorted elements back to the original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
