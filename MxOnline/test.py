nums=range(2,20)

for i in nums:
    nums = filter(lambda x:x == i or x % i ,nums)
print(type(nums))

print(list(nums))
print (type(nums))