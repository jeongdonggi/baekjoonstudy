class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int a_odd = a % 2;
        int b_odd = b % 2;
        
        if (a_odd == 1 && b_odd == 1) {
            answer = a * a + b * b;
        } else {
            if (a_odd == 0 && b_odd == 0) {
                answer = Math.abs(a - b);
            } else {
                answer = 2 * (a + b);
            }
        }
        
        return answer;
    }
}