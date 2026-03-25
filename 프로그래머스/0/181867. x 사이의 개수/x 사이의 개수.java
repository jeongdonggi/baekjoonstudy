import java.util.*;

class Solution {
    public int[] solution(String myString) {
        List<Integer> answer = new ArrayList<Integer>();
        
        int cnt = 0;
        for (char c : myString.toCharArray()) {
            if (c == 'x') {
                answer.add(cnt);
                cnt = 0;
            } else {
                cnt++;
            }
        }
        
        answer.add(cnt);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}