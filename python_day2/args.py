def maximum(*nums):
    maxi = nums[0]
    for i in nums[1:]:
        if i > maxi:
            maxi = i
    return maxi
print(maximum(1, 2, 3, 4, 5))