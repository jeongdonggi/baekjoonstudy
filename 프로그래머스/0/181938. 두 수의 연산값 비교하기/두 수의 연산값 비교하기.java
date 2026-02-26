import java.util.*;

class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int one = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int two = 2 * a * b;
        answer = Math.max(one, two);
        return answer;
    }
}