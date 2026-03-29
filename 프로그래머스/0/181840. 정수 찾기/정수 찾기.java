import java.util.*;

class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        
        Arrays.sort(num_list);
        
        for(int num : num_list) {
            if (num == n) {
                answer = 1;
                break;
            }
        }
        
        return answer;
    }
}