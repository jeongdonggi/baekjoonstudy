import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {        
        Deque<Integer> answer = new ArrayDeque<Integer>();
        
        for (int num : arr) {
            if (!answer.contains(num) && answer.size() < k) {
                answer.offer(num);   
            }
        }
        
        int len = answer.size();
        for (int i = 0; i < k - len; i++) {
            answer.offer(-1);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}