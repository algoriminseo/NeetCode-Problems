class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = left + 1;
        int res = 0;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                res = Math.max(res, prices[right] - prices[left]);    
            }
            else {
                left = right;
            }
            right++;

        }
        return res;
    }   
}
