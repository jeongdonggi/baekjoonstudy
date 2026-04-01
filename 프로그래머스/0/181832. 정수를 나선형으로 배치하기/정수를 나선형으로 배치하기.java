class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        int num = 0; // 0: 우, 1: 하, 2: 좌, 3: 상
        
        int x = 0;
        int y = 0;
        
        answer[0][0] = 1;
        
        for(int i = 2; i <= n * n; i++) {
            int tx = x + dx[num];
            int ty = y + dy[num];
            
            if (ty < 0 || tx < 0 || ty >= n || tx >= n || answer[ty][tx] != 0) {
                num = (num + 1) % 4;
                tx = x + dx[num];
                ty = y + dy[num];
            }
                
            answer[ty][tx] = i;
            x = tx;
            y = ty;
        }
        
        return answer;
    }
}