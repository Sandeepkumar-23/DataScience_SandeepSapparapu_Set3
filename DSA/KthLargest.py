def Kth_Largest(nums,k):
    target=len(nums)-k
    left=0
    right=len(nums)-1
    
    while left <= right:
        pivot=nums[right]
        i=left 
        for j in range(left,right):
            if nums[j]<=pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i], nums[pivot]=nums[pivot],nums[i]  
        
        if i==target:
            return nums[i]
        elif i<target:
            left=i+1
        else:
            right=i-1      
    
nums=[11,7,9,4,35,4]
k=2
result=Kth_Largest(nums,k)
print(result)