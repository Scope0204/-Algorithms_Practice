import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FailureRate {
    public int[] solution(int N, int[] lastStages) {
        int nPlayers = lastStages.length; // 플레이어 수
        int[] nStagePlayers = new int[N + 2]; // N 스테이지에 있는 플레이어 수, 전부 클리어한 사람의 경우 N+1 에 있음 -> 2를 더함
        for (int stage : lastStages) {
            nStagePlayers[stage] += 1;
        }

        int remainingPlayers = nPlayers; // 남은 플레이어 수 = 초기값은 기존 플레이어 수
        List<Stage> stages = new ArrayList<>();
        for (int id = 1 ; id <= N; id++) {
            double failure = (double) nStagePlayers[id] / remainingPlayers; // 현재 스테이지에 머문 플레이어 수 / 남은 플레이어 수 = 실패율(double)
            remainingPlayers -= nStagePlayers[id]; // 남은 플레이어 수 -= 현재 실패한 플레이어 수

            Stage s = new Stage(id, failure); // (현재 스테이지, 실패율)
            System.out.println(s.id+" "+s.failure);
            stages.add(s);
        }

        Collections.sort(stages);

        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = stages.get(i).id;
            System.out.println(answer[i]);
        }
        return answer;
    }

    class Stage implements Comparable<Stage> {
        public int id; // 스테이지
        public double failure; // 실패율

        public Stage(int id_, double failure_) {
            id = id_;
            failure = failure_;
        }

        @Override
        public int compareTo(Stage o) { // 실패율에 따른 정렬

            if (failure < o.failure ) {
                return 1;
            }
            if (failure > o.failure ) {
                return -1;
            }
            return 0;

        }
    }


}
