#arr = array
#low = start_index
#high = End_index
#x = search value
#mid = Mid_index

arr = []
for v in range(4):
    arr.append(int(input("Enter a Number :")))
print(arr)

x = int(input("Enter the search value : "))

#implementing binarysearch
def binarySearch(arr, low,high, x):
    #check base case
    if high  >= low:
        mid = (high+low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr,low, mid-1, x)

        else:
            return binarySearch(arr, mid+1, high, x)

    else:
        return -1

#function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
