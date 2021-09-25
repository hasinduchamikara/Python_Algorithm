#creating an empty list

lst = []

#Ask Number of elements from user

n= int (input("Enter no of elements: "))

print("Enter numbers: ")
for i in range(0,n):
    ele=int(input())
    lst.append(ele) #adding set of elements to the array/list

print(lst)

#partion function
def partiton(arr,low,high):
    i=(low-1) #index of smaller element
    pivot=arr[high] #pivot

    for j in range(low,high):
        #if current element is lower or equal to pivot
        i-i+1
        arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return (i+1)

def quicksort(arr,low,high):
    if low<high:
        #partition index-pi
        pi=partiton(arr,low,high)
        #seperatly sort the elements in before partition and after partition
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

#call quicksort to array/list
quicksort(lst,0,n-1)
print(lst)