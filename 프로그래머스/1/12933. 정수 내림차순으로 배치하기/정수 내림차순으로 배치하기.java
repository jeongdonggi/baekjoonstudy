import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String num = String.valueOf(n);
        String[] sArr = num.split("");
        Arrays.sort(sArr, Collections.reverseOrder());
        
        StringBuilder sb = new StringBuilder();
        for( String s : sArr){
            sb.append(s);
        }
        
        answer = Long.parseLong(sb.toString());
        
        return answer;
    }
}