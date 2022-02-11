import java.util.LinkedList;
import java.util.Queue;

public class CrossBridge {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> trucks = new LinkedList<Integer>();
        for(int truck : truck_weights){
            trucks.add(truck);
        }

        Queue<Integer> bridge = new LinkedList<Integer>();
        for(int i = 0; i<bridge_length ; i++){
            bridge.add(0);
        }

        while(!bridge.isEmpty()){
            answer += 1;
            bridge.poll();
            if(!trucks.isEmpty()){
                int truck = trucks.peek(); // Queue에 첫번째로 저장된 값을 가져옴
                int check = weightCheck(bridge, truck , weight);
                if(check==1){
                    trucks.poll();
                    bridge.add(truck);
                }else{
                    bridge.add(0);
                }
            }

        }

        return answer;
    }
    public int weightCheck(Queue<Integer> bridge, int truck , int weight){
        int sum = 0;
        for(int i : bridge){
            sum += i;
        }
        if(sum + truck <= weight){
            return 1;
        }
        else{
            return 0;
        }
    }
}
