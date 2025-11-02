# two sum problem
def two_sum(arr,target):
    left =0
    right = len(arr)-1
    arr.sort()
    print(arr)
    while left<right:
        if target == arr[left]+arr[right]:
            print(arr[left],arr[right])
            left += 1
            right -= 1
        elif target > arr[left] + arr[right]:
            left+=1
        else:
            right-=1
    return -1
# two_sum([20,33,52,32,1,6,2,3,4,30],36)

def triple_sum(arr,target):
    for i in range(len(arr)-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        
        while left < right:
            total = arr[i]+arr[left]+arr[right]
            if target < total:
                right -=1 
            elif target > total:
                left+=1
            else:
                if target == total:
                    print(arr[i], arr[left], arr[right])
                    left+=1
                    right-=1
                while left<right and arr[left] == arr[left-1]:
                    left+=1
                while left<right and arr[right] == arr[right+1]:
                    right-=1
                    
triple_sum([-3,-2,-1,0,1,2,3],0)
