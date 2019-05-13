#Move duplicates to the end of list
def moveDuplicates(arr):
    arr.sort()
    num_list = []
    dup_list = []
    for num in arr:
        if num not in num_list:
            num_list.append(num)
        else:
            dup_list.append(num)
    return num_list+dup_list

#Driver program
arr = [3,6,2,8,4,6,2,2,1,3]
print (moveDuplicates(arr))
