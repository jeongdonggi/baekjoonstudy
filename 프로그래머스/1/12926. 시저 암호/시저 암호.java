class Solution {
    public String solution(String s, int n) {
        String answer = "";
        String[] arr = s.split("");
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                answer += ' ';
            } else {
                char c = s.charAt(i);
                if (Character.isLowerCase(c)) {
                    answer += (char)((c - 'a' + n)  % 26 + 'a');
                } else {
                    answer += (char)((c - 'A' + n)  % 26 + 'A');
                }
            }
        }
        
        return answer;
    }
}