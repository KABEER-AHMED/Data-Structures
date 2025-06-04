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

def occurrences_calculator_seq(num_lst, num):
    occur_list = []
    for i in range(len(num_lst)):
        if num == num_lst[i]:
            occur_list.append(i)
    print ( "the occurrences occurred at the following indices {}".format(occur_list))
    return occur_list
def First_occurrence_bin(num_list,num):
    left_index = 0
    right_index = len(num_list) - 1
    result = -1
    while left_index<= right_index:
        middle_index = (left_index+right_index ) //2
        middle_number = num_list[middle_index]
        if middle_number == num:
            result = middle_index
            right_index = middle_index -1 
            
        elif num < middle_number:
            right_index = middle_index - 1
        else:
            left_index = middle_index+1
    return result
def last_Occurrence_bin(num_list,num):
    left_index = 0
    right_index = len(num_list) -1
    result =-1
    while left_index <= right_index:
        middle_index = (left_index+right_index ) //2
        middle_number = num_list[middle_index]
        if middle_number == num:
            result = middle_index
            left_index = middle_index +1
        elif num < middle_number:
            right_index = middle_index - 1
        else:
            left_index = middle_index+1
    return result

lst = [1,2,3,4,5,6,7,8,9,10,12,12,12,12,13,14,15,16,17,19,22,23,34,45,56,67,78]
binary_search(lst,23)
x= (last_Occurrence_bin(lst,12)  -  First_occurrence_bin(lst,12)) +1
print(x)