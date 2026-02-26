class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = left + 1;

        int maxP = 0;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                maxP = Math.max(maxP, prices[right]- prices[left]);
            }
            else {
                left = right;
            }
            right++;
        }   
        return maxP;

    }
}