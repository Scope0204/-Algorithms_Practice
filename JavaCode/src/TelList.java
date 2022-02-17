import java.util.Arrays;

public class TelList {
    public boolean solution(String[] phone_book) {
        boolean answer = true;

        Arrays.sort(phone_book);

        for(int i = 0 ; i < phone_book.length-1 ; i++){
            // 해당 수가 다음 수의 접두사인 경우
            if(phone_book[i+1].startsWith(phone_book[i])){
                return false;
            }
        }

        return answer;
    }
}
