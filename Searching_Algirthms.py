def binary_search(num_list,item):
    left_index = 0
    right_index = len(num_list) - 1
    while left_index<= right_index:
        middle_index = (left_index+right_index ) //2
        middle_number = num_list[middle_index]
        if middle_number == item:
            print("found the item at position {}".format(middle_index))
            return middle_index
        elif item < middle_number:
            right_index = middle_index - 1
        else:
            left_index = middle_index+1
    return -1

lst = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,19,22,23,34,45,56,67,78]
binary_search(lst,23)