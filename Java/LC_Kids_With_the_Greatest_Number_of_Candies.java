// Problem - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


/*
Solution

Standard approach. Just find the max element in the list first.
Once you have that, loop through and add the extra candies. If the value exceeds the max element found above^, then 'true' else 'false'
*/
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        List<Boolean> ans = new ArrayList<Boolean>();
        int maxCandies = getMaxValue(candies);
        
        for (int i=0; i<candies.length; i++) {
            if (candies[i] + extraCandies >= maxCandies) {
                ans.add(i, true);
            }
            else {
                ans.add(i, false);
            }
        }
        
        return ans;
    }

    public int getMaxValue(int[] candies) {
        
        int maxValue = 0;
        for (int i=0; i<candies.length; i++) {
            if (candies[i] > maxValue) {
                maxValue = candies[i];
            }
        }
        
        return maxValue;
    }
}
