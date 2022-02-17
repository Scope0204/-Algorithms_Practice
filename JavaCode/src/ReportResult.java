import java.util.*;

public class ReportResult {

    public int[] solution(String[] id_list, String[] report, int k) {
        // 유저 정보 < 이름 : 신고를 성공시킨 횟수 >
        Map<String, Integer> users = new LinkedHashMap<>();
        // 신고 기록 < 이름 : 자신을 신고한 사람 목록 >
        Map<String, HashSet<String>> reportRecord = new HashMap<>();


        for(String id : id_list) {
            users.put(id, 0);
            reportRecord.put(id, new HashSet<>());
        }

        for(String rep : report){
            String reporter = rep.split(" ")[0];
            String user = rep.split(" ")[1];
            // 중복된 값이 저장되지않음(set)
            reportRecord.get(user).add(reporter); //해당 user를 신고한 사람을 기록
        }

        for(String key: reportRecord.keySet()){
            HashSet<String> reportUsers = reportRecord.get(key); // 해당 유저를 리폿한 사람들
            if(reportRecord.get(key).size() >= k){ // k이상 신고를 당했을 경우
                for( String reportUser : reportUsers ){
                    int reportCount = users.get(reportUser); // 리폿한 사람의 현재 신고 횟수
                    users.put(reportUser, reportCount+1); // 신고 횟수 +1 추가
                }
            }
        }

        int[] answer = new int[id_list.length];
        for ( int i = 0 ; i < answer.length ; i++ ){
            answer[i] = users.get(id_list[i]);
        }

        return answer;

    }
}
