import java.util.Arrays;

public class K_Number {
    public int[] solution(int[] array, int[][] commands){
        int[] answer = new int[commands.length];
        for(int idx = 0 ; idx < commands.length ; idx++ ){
            int[] comm = commands[idx];
            int i = comm[0];
            int j = comm[1];
            int k = comm[2];

            int[] arr = Arrays.copyOfRange(array, i-1, j);
            Arrays.sort(arr);
            answer[idx] = arr[k-1];
        }
        return answer; // 배열의 주소값을 리턴함을 명심하자
    }
}
