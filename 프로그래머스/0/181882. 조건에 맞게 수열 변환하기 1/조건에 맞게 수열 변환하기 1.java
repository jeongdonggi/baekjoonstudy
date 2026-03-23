import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<Integer>();
        for (int num : arr) {
            if (num >= 50 && (num % 2 == 0)) {
                answer.add(num / 2);
            } else if (num < 50 && num % 2 == 1){
                answer.add(num * 2);
            } else {
                answer.add(num);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}