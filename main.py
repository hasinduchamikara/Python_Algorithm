#creating an empty list

lst = []

#Ask Number of elements from user

n= int (input("Enter no of elements: "))

print("Enter numbers: ")
for i in range(0,n):
    ele=int(input())
    lst.append(ele) #adding set of elements to the array/list

print(lst)

#function to do insertion sort

def insertionSort (arr):
    #traverse  through 1 to len(arr)

    for i in range(1,len(arr)):
        key=arr[i]

        #Move elements of arr[0..1-1], that are greater than key, to one position ahed of their current position

        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key

#calling the function
insertionSort(lst)

#print the sorted array
print("sorted array is: ")
for i in range(len(lst)):
    print("%d" %lst[i])

#print (lst)
