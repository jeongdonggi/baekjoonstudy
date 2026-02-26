import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> lst = new ArrayList<Integer>();
        for (int i = 1; i <= n; i += 2) {
            lst.add(i);
        }
        
        return lst.stream().mapToInt(i -> i).toArray();
    }
}