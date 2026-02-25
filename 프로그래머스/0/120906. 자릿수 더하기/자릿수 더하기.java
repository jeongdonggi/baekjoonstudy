import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        String s = String.valueOf(n);
        
        for (String  num : s.split("")) {
            answer += Integer.parseInt(num);
        } 
        
        return answer;
    }
}