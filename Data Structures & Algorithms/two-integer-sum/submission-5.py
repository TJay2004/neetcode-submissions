class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       num_set = set()
       num_dict = {value: key for key, value in enumerate(nums)}
       for i,n in enumerate(nums):
           num_set.add(n)  
           diff = target - n 
           if diff in num_set and num_dict.get(diff) != i:
                return sorted([num_dict.get(diff),i])