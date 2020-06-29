from colorama import Fore, Back, Style

def binary_search(data, target, low, high): 
    # print status
    print(Style.DIM, Fore.YELLOW, "...searching for", target, "in:", data[low:high], Style.RESET_ALL)

    if low > high:                          # check for empty interval
        print(Fore.RED, "FAILURE:", target, "not found in data", Style.RESET_ALL)
        return False
    else: 
        mid = (low + high) // 2             
        if target == data[mid]:             # found match
            print(Fore.GREEN, "SUCCESS: target located at index", mid, Style.RESET_ALL)
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else: 
            # recur on portion right of the middle
            return binary_search(data, target, mid + 1, high)


arr = [1,2,5,6,8,10,11,13,15,16,19,20,22,24,25,30,44,50,70,99,100,124,190]
binary_search(arr, 190, 0, len(arr) - 1)
