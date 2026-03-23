class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int[] preview = new int[arr.length];
        int[] after = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++) {
            preview[i] = arr[i];
        }
        
        int cnt = 0;
        
        while(true) {
            boolean b = true;
            for (int i = 0; i < after.length; i++) {
                if (preview[i] >= 50 && preview[i] % 2 == 0) {
                    after[i] = preview[i] / 2;
                } else if (preview[i] < 50 && preview[i] % 2 == 1) {
                    after[i] = preview[i] * 2 + 1;
                } else {
                    after[i] = preview[i];
                }
                           
                if (after[i] != preview[i]) {
                    b = false;
                }
            }
                           
            if (b) {
                answer = cnt;
                break;
            } else {
                for (int i = 0; i < after.length; i++) {
                    preview[i] = after[i];
                }
            }
            cnt++;
        }
        
        return answer;
    }
}