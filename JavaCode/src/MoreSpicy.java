import java.util.*;

class MoreSpicy {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();

        for(int scov : scoville){
            priorityQueue.add(scov);
        }

        while(priorityQueue.peek() < K && priorityQueue.size() >= 2){
            int a= priorityQueue.poll();
            int b = priorityQueue.poll();
            priorityQueue.add(a+(b*2));
            answer += 1;
        }

       if(priorityQueue.peek() < K){
           return -1;
       }
       else{
           return answer;
       }
    }
}