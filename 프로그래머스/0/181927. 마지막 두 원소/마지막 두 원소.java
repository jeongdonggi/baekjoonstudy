import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int len = num_list.length;
        
        List<Integer> answer = new ArrayList<Integer>();
        
        for (int num : num_list) {
            answer.add(num);
        }
        
        if (num_list[len - 2] >= num_list[len -1]) {
            answer.add(num_list[len - 1] * 2);
        } else {
            answer.add(num_list[len -1] - num_list[len - 2]);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}