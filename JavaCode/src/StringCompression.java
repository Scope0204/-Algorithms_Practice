public class StringCompression {
    public int solution(String s) {
        int answer = s.length();

        for( int step = 1; step < s.length()/2+1 ; step++ ){
            // step : 1~s.length()/2 까지의 단계를 늘려가며 함
            String compressed = ""; // 압축하여 나온 문자열
            String prev = s.substring(0,step); // step만큼의 문자열 추출 : 압축할 문자
            int count = 1; // 압축 횟수 : : 현재 압축정도

            // step 크기만큼 증가시키며 이전 문자열과 비교
            for (int i = step ; i < s.length(); i += step ){
                String next = s.substring(i, i + step > s.length() ? s.length() : i + step );

                // 이전 상태와 동일한 경우 count 증가
                if (prev.equals(next)) {
                    count += 1;
                }
                // 다른 문자열이 나온경우 -> 더 이상 압축 불가
                else{
                    // 2번 이상 압축한 경우에만 count를 형변환해서 붙여주고, 아닌 경우에는 그냥 prev
                    if(count>=2){
                        compressed += Integer.toString(count) + prev;
                    }
                    else {
                        compressed += prev;
                    }
                    prev = next; // next와 비교해주기 위해 상태 초기화
                    count = 1; // 압축 횟수도 초기화
                }
            }
            // 남아있는 문자열도 조건에 맞게 뒤에 추가
            // 중복되는 부분은 함수로 만들면 될 것 같다
            if(count>=2){
                compressed += Integer.toString(count) + prev;
            }
            else {
                compressed += prev;
            }

            answer = Math.min(answer, compressed.length());
        }

        return answer;
    }
}
