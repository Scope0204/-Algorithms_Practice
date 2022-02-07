public class FunctionDevelopment2 {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] temp = new int[100]; //작업의 개수는 100개 이하이므로 100으로 선언
        int day = 0; //temp에 적용할 배포일 수

        //각 항목마다 100까지 검사해야하므로 for문안에 while문이 돌아감
        for (int i = 0; i < progresses.length; i++) {
            while (progresses[i] + (speeds[i] * day) < 100) {
                day++;
            }
            temp[day]++; // 해당 날짜에 해결되는 기술의 수를 기록
        }

        int cnt = 0;

        //temp에 들어간 배열의 길이를 알기위한 코드
        for (int n : temp) {
            if (n != 0) { // 초기에 전부 0으로 되어있어 , 값이 기록된 부분만 찾기위해선 0이 아닌부분만 찾아주면 됨
                cnt++;
            }
        }

        int[] ans = new int[cnt]; // 구해낸 배열의 길이를 이용해 배열 생성

        cnt = 0;
        for (int n : temp) {
            if (n != 0) {
                ans[cnt] = n;
                cnt++;
                // ans[cnt++] = n; 로 줄여서도 쓸 수 있음
            }
        }

        return ans;
    }
}
