def selectionsort(array):
    for i in range(0, len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[min] > array[j]):
                min = j
        array[min], array[i] = array[i], array[min]
    return array
array = [int(x) for x in input("Enter the elements separated by space: ").split()]
print("Unsorted array: ",(array))
print("Sorted array: ",selectionsort(array))