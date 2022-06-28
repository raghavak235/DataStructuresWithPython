def merge_sort(arr):
    # pass
    len_arr = len(arr)
    middle = len_arr//2
    left = arr[:middle]
    right = arr[middle:]
    merge_sort(left)
    merge_sort(right)



def merging_sorted_elements(a, b):
    sorted_list=[]

    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i<len_a and j<len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len(a):
         sorted_list.append(a[i])
         i += 1

    while j < len(b):
         sorted_list.append(b[j])
         j += 1

    return sorted_list

    pass



if __name__ == '__main__':
    # pass
    a = [5,8,12,56,68]
    b = [7,9,45,51,100]

    print(merging_sorted_elements(a,b))

