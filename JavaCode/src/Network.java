class Network {
    static int[]visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited= new int[computers.length];
        for(int i = 0; i < computers.length ; i++){
            visited[i] = 0;
        }

        for(int i = 0 ; i <visited.length ; i++){
            if(visited[i] == 0){
                dfs(i,computers);
                answer++;
            }
        }

        return answer;
    }

    void dfs(int i, int[][] computers){
        visited[i] = 1;
        for(int j = 0 ; j <visited.length; j++){
            if(visited[i] == 0 && computers[i][j] ==1){
                dfs(j, computers);
            }
        }
    }
}