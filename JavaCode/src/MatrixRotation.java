public class MatrixRotation {
    int[][] matrix;
    public int[] solution(int rows, int columns, int[][] queries) {

        this.matrix = new int[rows][columns];
        int[] ans = new int[queries.length];

        int num = 0;
        for( int i=0 ; i <rows; i++){
            for (int j = 0; j < columns; j++) {
                num +=1;
                matrix[i][j] = num;
            }
        }
        for( int i = 0; i < queries.length ; i++ ){
            ans[i] = rotation(queries[i]);
        }
        return ans;
    }

    public int rotation(int[] query) {
        int x1 = query[0]-1;
        int y1 = query[1]-1;
        int x2 = query[2]-1;
        int y2= query[3]-1;

        int start = this.matrix[x1][y1]; // 시작위치 값 임시저장
        int min = start; // 최소값 초기화 : 젤 처음은 시작하는 위치가 가장 작다
        for(int i = x1 ; i < x2 ; i++){
            this.matrix[i][y1] = this.matrix[i+1][y1];
            if(min > this.matrix[i][y1]) min = this.matrix[i][y1];
        }
        for(int i = y1; i < y2; i++){ // 회전의 2번
            this.matrix[x2][i] = this.matrix[x2][i+1];
            if(min > this.matrix[x2][i]) min = this.matrix[x2][i];
        }
        for(int i = x2; i > x1; i--){ // 회전의 3번
            this.matrix[i][y2] = this.matrix[i-1][y2];
            if(min > this.matrix[i][y2]) min = this.matrix[i][y2];
        }
        for(int i = y2; i > y1; i--){ // 회전의 4번
            this.matrix[x1][i] = this.matrix[x1][i-1];
            if(min > this.matrix[x1][i]) min = this.matrix[x1][i];
        }
        System.out.println("전" + this.matrix[x1][y1+1]);
        this.matrix[x1][y1+1] = start;
        System.out.println("후" + this.matrix[x1][y1+1]);


        return min; // 최솟값 반환

    }


}
