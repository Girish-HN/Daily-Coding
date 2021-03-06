#Problem 4
#Given an array of integers, find the first missing positive integer in linear time and constant space
#In other words, find the lowest positive integer that does not exist in the array
#The array can contain duplicates and negative numbers as well
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3

def missing_positive_integer(my_list):
    max_value = max(my_list)
    my_list = [num for num in range(1,max(my_list)) if num not in my_list]

    if len(my_list) == 0:
        my_list.append(max_value+1)
    
    return min(my_list)

#Drawback of the above approach is it takes extra space for assigning "max_value" which is not the right solution
my_list = [1,2,3,4,5,8,-1,-12,-3,-4,-8]

print(missing_positive_integer(my_list))


def sortOfSort(arr) :
    for index in range(len(arr)):
        checkValue = arr[index]
        #This approach uses linear sort for positive integers. For reference use the belwo link for algorithm explanation 
        #https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti
        
        while(checkValue > 0 and checkValue != index and checkValue < len(arr) and arr[checkValue] != checkValue):
            print(checkValue, index, arr[checkValue])
            arr[index] = arr[checkValue]
            arr[checkValue] = checkValue
            checkValue = arr[index]
            print(arr)

    return arr[1:] + [arr[0]]

def findFirstMissingNumber(arr):
    arr = sortOfSort(arr)
    print(arr)
    for x in range(len(arr)) :
        if (x+1 != arr[x]) :
            return x+1
    return len(arr) + 1
