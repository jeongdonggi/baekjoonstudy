class Solution {
    int answer = 0;
    public int solution(String[] s1, String[] s2) {
        for (String s : s1) {
            for (String ss : s2) {
                if (ss.equals(s)) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}