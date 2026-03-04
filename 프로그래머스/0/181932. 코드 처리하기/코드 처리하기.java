class Solution {
    public String solution(String code) {
        StringBuilder answer = new StringBuilder();
        
        int mode =  0;
        
        for(int i = 0; i < code.length();i++) {
            
            if (code.charAt(i) == '1') {
                mode = (mode + 1) % 2;
                continue;
            }
            
            if (mode == 0) {
                 if (i % 2 == 0) {
                     answer.append(code.charAt(i));
                 }
            } else {
                if (i % 2 == 1) {
                    answer.append(code.charAt(i));
                }
            }
        }
        
        return answer.toString().length() == 0 ? "EMPTY" : answer.toString();
    }
}