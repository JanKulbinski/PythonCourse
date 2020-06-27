def quicksort(array):
    if len(array) < 1:
        return array
    else:
        pivot = array[0]
        return quicksort(list(filter(lambda x : x < pivot, array))) \
            + list(filter(lambda x : x == pivot, array)) \
            + quicksort(list(filter(lambda x : x > pivot, array)))

if __name__== "__main__":
    print(quicksort([23,12,1,21,45,23,43,21,47,85,65,32,32,12]))
