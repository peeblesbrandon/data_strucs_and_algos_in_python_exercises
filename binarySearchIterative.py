from colorama import Fore, Back, Style

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        print(Style.DIM, Fore.YELLOW, "...searching for target in", data[low:high], Style.RESET_ALL)
        mid = (low + high) // 2
        if target == data[mid]:
            print(Fore.GREEN,"SUCCESS: target found at index ", mid, Style.RESET_ALL)
            return True 
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


arr = [1, 2, 5, 6, 8, 10, 11, 13, 15, 16, 19, 20,
    22, 24, 25, 30, 44, 50, 70, 99, 100, 124, 190]
binary_search(arr, 190)
