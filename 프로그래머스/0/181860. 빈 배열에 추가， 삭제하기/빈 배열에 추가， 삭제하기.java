import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> answer = new ArrayList<Integer>();
        
        for(int i = 0; i < flag.length; i++) {
            for(int j = 0; j < arr[i]; j++) {
                if (flag[i]) {
                    answer.add(arr[i]);
                    answer.add(arr[i]);
                } else {
                    answer.remove(answer.size() - 1);
                }
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}