class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        Approach:
        
        Pretty simple and intuitive. 
        Just write down the cumulative sum up until the corresponding index.
        Example:
        nums = [1,2,1,3], k = 3
        sums = [1,3,4,7]. Also, we need 0 which is the sum before the start of the first index. 
        I'll tell you why we need that 0.
        
        First, let's go through this sums array and find out the count of the subarray which has sums = k.
        Idea. lets sums = [0,1,3,4,7]. i.e: add that 0 to the sums array.
        Now, randomly pick any element in the sums array and if you find (that element-k) in the sums array, then,
        you need to increase count by 1.
        
        Meaning, say you pick element 7 and 7-k = 4. 4 is present in the sums array => increase count by one.
        Idea behind is that, whenever you sums increases by a value k, you've found a subarray whose sums = k.
        Simlarly, 4-k = 3 which is present in the sums array => inc count by one.
        Similarly, 3-k = 0 which is present in the sums array => inc count by one.
        
        Now, we use 0 because, we need to calculate the first time we encounter a sums==k. Let's see an example to understand that.
        nums = [3,1], k = 3
        Now, the first value is 3 and sums = 3 and sums-k=0. Now, if you followed the first example,
        what we did was we checked if sums-k was present in the sums array. Similarly, we need 0 to be in the sums array.
        
        Another example, nums = [1,1,1], k = 2
        Here, sums = [1,2,3]
        When we get to index 1, our sums will be equal to 2 and we will calculate sums-k => 2-2=0.
        But we don't have 0 in our sums array. That is why we have it in the sums array.
        
        Bottomline: 0 is just there only for one case. "When our sums==k". Because, rest of the time,
        we only check if sums-k is present in the sums array.
        """
        count = 0
        sums = 0
        d = {}
        d[0] = 1
        
        for i in range(len(nums)):
            sums+=nums[i]
            count+=d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1
        
        return(count)
