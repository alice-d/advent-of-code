nums=[3,8,9,1,2,5,4,6,7]
#nums=[3,6,4,2,8,9,7,1,5]

for i in range(100):
    curr =nums[0]
    nnumst3 = nums[1:4]

    nums = nums[4:]
    num=curr-1

    while num!= curr:

        if (num in nums):
            break
        else:
            if num<=1:
                num=max(nums)
            else:
                num-=1
    destIndnums = nums.index(num)
    nums = nums[:destIndnums+1] + nnumst3 + nums[destIndnums+1:] +[curr]

    #print(nums)
one =  nums.index(1)

final = nums[one+1:] + nums[:one]
#print(final)
print("Part 1: ", "".join(list(map(str,final))))



