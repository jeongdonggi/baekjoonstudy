import java.util.*;

class Solution {
    public String solution(String my_string, int n) {
        String[] answer = Arrays.copyOf(my_string.split(""), n);
        return String.join("", answer);
    }
}