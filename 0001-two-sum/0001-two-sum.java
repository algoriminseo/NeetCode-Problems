import java.util.Hashtable;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] res = new int[2];
        Hashtable<Integer, Integer> numMap = new Hashtable<>();
    
        for(int i = 0 ; i < nums.length; i++) {
            numMap.put(nums[i], i);
        }

        for(int j = 0 ; j < nums.length; j++) {
            int diff = target-nums[j];
            if (numMap.containsKey(diff) && (j != numMap.get(diff))) {
                res[0] = j;
                res[1] = numMap.get(diff);
            
            }
        }   
        return res;
    }
}