import java.util.*;

public class FunctionDevelopment {
        public int[] solution(int[] progresses, int[] speeds) {

            Queue<Integer> que = new LinkedList<>();
            for( int i = 0 ; i <progresses.length ; i++) {
                que.add((int) (Math.ceil((100.0 - progresses[i])/ speeds[i])));
            }
            // ceil() : 입력 인자 값보다 크거나 같은 가장 작은 정수값을 double형으로 반환
            // 2.5 -> 3.0 이런식으로

            List<Integer> answer = new ArrayList<>();

            while(!que.isEmpty()){
                int day = que.poll();
                int count = 1;

                while(!que.isEmpty() && day >= que.peek()){ // 해당 경과일이 지났을때, 이미 구현이 끝난 기능들을 찾음
                    count++; // 같이 끝난 기능들의 개수를 더함
                    que.poll(); // 리스트에서도 뺌
                }

                answer.add(count);

            }

            return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
