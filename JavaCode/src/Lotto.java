class Lotto {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0}; // 최고 순위 , 최저 순위
        int[] point = {6,6,5,4,3,2,1};
        int zero_cnt = 0;
        int cnt = 0;

        for(int lotto : lottos ){
            if(lotto == 0){
                zero_cnt +=1;
            }
            else {
                for (int win_num : win_nums) {
                    if (lotto == win_num) {
                        cnt += 1;
                        break;
                    }
                }
            }
        }

        answer[0] = point[zero_cnt+cnt];
        answer[1] = point[cnt];
        return answer;
    }
}