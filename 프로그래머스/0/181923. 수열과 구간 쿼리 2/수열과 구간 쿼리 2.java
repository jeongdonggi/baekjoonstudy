import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        int i = 0;
        
        for (int[] query : queries) {
            int[] array = Arrays.copyOfRange(arr, query[0], query[1] + 1);
            Arrays.sort(array);
            
            int ans = -1;
            for (int num : array) {
                if (query[2] < num) {
                    ans = num;
                    break;
                }
            }
            
            answer[i++] = ans;
        }
        return answer;
    }
}

