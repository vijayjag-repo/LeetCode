// Problem - https://leetcode.com/problems/running-sum-of-1d-array/

/*
Solution

Straightforward. Just run through the array and add the sum along the way.
*/

class Solution {
    public int[] runningSum(int[] nums) {
        
        int[] ans = new int[nums.length];
        ans[0] = nums[0];
        
        for (int i=1; i<nums.length; i++) {
            ans[i] = ans[i-1] + nums[i];
        }
        
        return ans;
    }
}
