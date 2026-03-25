import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<Integer>();
        for (int num : arr) {
            for (int i = 0; i < num; i++) {
                answer.add(num);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}