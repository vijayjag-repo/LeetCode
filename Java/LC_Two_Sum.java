// Problem - https://leetcode.com/problems/two-sum/

/* 
Solution 1

Pretty straighforward in terms of the approach. 
For each element that you see in the array, scan the remaining items in the array.
If there is a match, return the corresponding indices.
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] ans = new int[2];
        
        for (int i=0; i<nums.length-1; i++) {
            for (int j=i+1; j<nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                    break;
                }
            }
        }
        return ans;
    }
}

/* 
Solution 2

TODO: <Add solution using hashmap>
*/