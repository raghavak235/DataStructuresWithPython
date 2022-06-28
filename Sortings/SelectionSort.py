
def selection_sort(arr):
    for i in range(len(arr)):
        min_ele_index = i
        for j in range((i+1), len(arr)):
            if arr[j] < arr[min_ele_index]:
                min_ele_index = j

        arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]



arr=[10,1,2,20,5]
selection_sort(arr)
print(arr)
