def quicksort(Input):
    length = len(Input)
    if length <= 1:
        return Input
    pivot = Input.pop()
    greater = []
    less = []
    for number in Input:
        if number > pivot:
            greater.append(number)
        else:
            less.append(number)
    return(quicksort(less)+[pivot]+quicksort((greater)))
print(quicksort([1,5,7,8,4,3,6,8,9,5,4,2,6,8,9]))
