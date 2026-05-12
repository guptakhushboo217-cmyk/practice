nums=[23,34,45,67,99,89,77,69,30,25]
#nums=sorted(nums)
#print(nums[-2]) 

first=second=nums[0]
for num in nums:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first: 
        second=num 
print(second) 
