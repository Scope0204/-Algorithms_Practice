import java.util.*;

public class Printer {
    class Task {
        int location;
        int priority; // 우선 순위

        public Task(int location, int priority) {
            this.location = location;
            this.priority = priority;
        }
    }

    public int solution(int[] priorities, int location) {

        int answer = 0;

        Queue<Task> queue = new LinkedList<>();

        for (int i = 0; i < priorities.length; i++) {
            queue.add(new Task(i, priorities[i]));
        }

        int now = 0;
        while (!queue.isEmpty()) {
            Task cur = queue.poll();
            boolean flag = false;
            for (Task t : queue) {
                if (t.priority > cur.priority) { //  현재 우선순위보다 우선되는 경우가 있을때,
                    flag = true; // 조건문을 실행 시킬 수 있도록 함
                }
            }
            if (flag) { // 우선순위 높은게 있으면 뒤로 보낸다
                queue.add(cur);
            } else { // 해당 작업을 실행
                now++; // 순서를 기록
                if (cur.location == location) { // 작업을 실행한 위치가 찾고있는 위치일경우
                    answer = now; // 지금까지 작업한 순서를 반환함
                    break;
                }

            }
        }
        return answer;
    }
}

