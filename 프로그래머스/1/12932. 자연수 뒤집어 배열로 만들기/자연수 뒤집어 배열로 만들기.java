class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        String num = String.valueOf(n);
        answer = new int[num.length()];
        
        for(int i = 0; i < num.length(); i++){
            answer[i] = (int)(n % 10);
            n = n / 10;
        }
        
        return answer;
    }
}