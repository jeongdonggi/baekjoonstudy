import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> answer = new ArrayList<Integer>();
        
        Set<Integer> delete_set = new HashSet<Integer>();
        
        for(int delete : delete_list) {
            delete_set.add(delete);
        }
        
        for(int num : arr) {
            if (!delete_set.contains(num)) {
                answer.add(num);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}