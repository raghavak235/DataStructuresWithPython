
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    print(arr)


insertion_sort([6,5,3,1,8,7,2,4])
