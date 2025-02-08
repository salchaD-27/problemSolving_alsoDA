# from typing import List
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
#         L,R=0,1
#         while(L<len(nums)-1):
#             R=L+1
#             while(R<L+indexDiff+1 and R<len(nums)):
#                 if(abs(nums[L]-nums[R])<=valueDiff): return True
#                 R+=1
#             L+=1
#         return False

from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def get_bucket_key(num): return num // bucket_size
        
        if indexDiff <= 0 or valueDiff < 0: return False
        bucket = {}
        bucket_size = valueDiff + 1
        for i, num in enumerate(nums):
            bucket_key = get_bucket_key(num)
            if bucket_key in bucket: 
                if abs(bucket[bucket_key] - num) <= valueDiff: return True
            if bucket_key - 1 in bucket and abs(num - bucket[bucket_key - 1]) < bucket_size: return True
            if bucket_key + 1 in bucket and abs(num - bucket[bucket_key + 1]) < bucket_size: return True
            bucket[bucket_key] = num
            if i >= indexDiff: del bucket[get_bucket_key(nums[i - indexDiff])]
        return False