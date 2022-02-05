import java.util.Arrays;

public class Test {
    // psvm
    // sout
    public static void main(String[] args) {

        K_Number k = new K_Number();
        int[] array = {1, 5, 2, 6, 3, 7};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        System.out.println(Arrays.toString(k.solution(array,commands)));
        System.out.println(k.solution(array,commands)); // 주소값이 출력

    }
}
