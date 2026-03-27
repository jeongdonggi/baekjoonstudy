import java.util.*;

class Solution {
    public int solution(String[] strArr) {        
        int[] lenArr = new int[31];
        
        for(String str : strArr) {
            lenArr[str.length()] += 1;
        }
        
        return Arrays.stream(lenArr).max().orElse(0);
    }
}