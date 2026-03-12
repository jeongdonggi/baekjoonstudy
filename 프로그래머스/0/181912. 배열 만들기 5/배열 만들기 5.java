import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<Integer>();
        for (String intStr : intStrs) {
            int temp = Integer.parseInt(intStr.substring(s, s+l));
            if (k < temp) {
                answer.add(temp);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}