import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Big_Num {
    public String solution(int[] numbers) {
        String answer = "";

        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < numbers.length; i++) {
            list.add(numbers[i]);
        }
        Collections.sort(list, (a, b) -> {
            //System.out.println(a+" "+b);
            //System.out.println(list);
            String as = String.valueOf(a), bs = String.valueOf(b);
            //System.out.println(Integer.parseInt(as + bs) + " " + Integer.parseInt(bs + as));
            //System.out.println(-Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as)));
            return -Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as));
        });
        StringBuilder sb = new StringBuilder();
        for(Integer i : list) {
            sb.append(i);
        }
        answer = sb.toString();
        if(answer.charAt(0) == '0') {
            return "0";
        }else {
            return answer;
        }
    }
}
