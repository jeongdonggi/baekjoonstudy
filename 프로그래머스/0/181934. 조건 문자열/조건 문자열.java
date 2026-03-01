class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        boolean answer = false;
        
        answer = ">".equals(ineq) ? n > m : n < m;
        
        if (!answer && "=".equals(eq)) {
            answer = n == m ? true : false;
        }
        
        return (answer) ? 1 : 0;
    }
}