import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> answer = new ArrayList<Integer>();
        for(int i = l; i <= r; i++ ) {
            String s = String.valueOf(i);
            boolean b = true;
            for (String c : s.split("")) {
                if (!"05".contains(c)) {
                    b = false;
                    break;
                }
            }
            if (b) {
                answer.add(i);
            }
        }
        if (answer.size() == 0){
            answer.add(-1);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}