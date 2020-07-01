from colorama import Fore, Back, Style

def insertionSort(unsorted_list):
    indexing_length = range(1, len(unsorted_list))
    for i in  indexing_length:
        value_to_sort = unsorted_list[i]
        while value_to_sort < unsorted_list[i - 1] and i > 0:
            print(unsorted_list)
            unsorted_list[i], unsorted_list[i - 1] = unsorted_list[i - 1], unsorted_list[i]
            i -= 1
    return unsorted_list # now sorted

list_to_sort = [3,1,45,23,2,3,5,6,3,1,3,5,673,6,3,45,0]
print(Fore.GREEN, insertionSort(list_to_sort), Style.RESET_ALL, sep='')           
