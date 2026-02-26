import java.util.Hashtable;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] res = new int[2];
        Hashtable<Integer, Integer> numMap = new Hashtable<>();
    
        for(int i = 0 ; i < nums.length; i++) {
            int diff = target - nums[i];

            if (numMap.containsKey(diff) ) {
                return new int[] {i, numMap.get(diff)};
            }


            numMap.put(nums[i], i);
        }

    
        return new int[] {};
    }
}