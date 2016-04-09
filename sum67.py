def sum67(nums):
  count = 0
  for a in nums:
   if a == 6:
    while True:
     nums.remove(nums[count])
     if nums[count] == 7:
      nums.remove(nums[count])
      break
   count += 1
  return sum(nums)

