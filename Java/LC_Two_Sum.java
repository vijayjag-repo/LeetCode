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

HashMap method. 
Iterate through the array.
Whenever you come across an element, add the element to the hashmap.
Also, if the Hashmap already contains the <target - current element>, then we've found a match.
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] ans = new int[2];
        
        for (int i=0; i<nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                ans[0] = i;
                ans[1] = map.get(target - nums[i]);
                break;
            }
            else {
                map.put(nums[i],i);
            }
        }
        
        return ans;
    }
}
