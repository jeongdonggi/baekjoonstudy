class Solution {
    public int[] solution(int[] arr) {
        int cnt = 1;
        int len = arr.length;
        
        while (cnt < len) {
            if (cnt < len) {
                cnt *= 2;
            }
        }
        
        int[] answer = new int[cnt];
        
        for (int i = 0; i < cnt; i++) {
            if (i < len) {
                answer[i] = arr[i];
            } else {
                answer[i] = 0;
            }
        }
        
        
        
        return answer;
    }
}