def sum_all_in_list(input_list):
    list_sum = 0
    for i in input_list:
        list_sum = list_sum + i
    return list_sum

if __name__=="__main__":
    lst = [1, 3, 7, 11, 65, 1, 54]
    print(sum_all_in_list(lst))
