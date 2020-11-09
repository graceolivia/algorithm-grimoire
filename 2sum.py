def twoSum(nums, target):
  dick = {}
  for i in range(len(nums)):
    compliment = target - nums[i]
    if compliment in dick:
      return [i, dick[compliment]]
    else:
      dick[nums[i]] = i


arr = [3,2,4]
print(twoSum(arr,6))
