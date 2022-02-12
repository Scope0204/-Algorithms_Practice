public class StockPrice {
    public int[] solution(int[] prices) {
        int[] ans = new int[prices.length];
        for(int i = 0 ; i<prices.length ; i++){
            int cnt = -1;
            for(int j = i ; j < prices.length ; j++){
                cnt += 1;
                if(prices[i] > prices[j])
                    break;
            }
            ans[i] = cnt;
        }
        return ans;
    }
}
