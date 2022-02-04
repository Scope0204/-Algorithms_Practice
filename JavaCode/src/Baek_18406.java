import java.util.Scanner;

public class Baek_18406 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nStr = sc.nextLine(); // 7755

        int sum1 = 0, sum2 = 0;
        int len = nStr.length(); // 4
        for(int i=0 ; i<len ; i++ ){
            if(i < len/2){ // i < 2
                sum1 += nStr.charAt(i) - '0'; // 0은 아스키코드 48
            }else{
                sum2 += nStr.charAt(i) - '0';
            }
        }

        if(sum1 == sum2){
            System.out.println("LUCKY");
        }else{
            System.out.println("READY");
        }
    }
}
