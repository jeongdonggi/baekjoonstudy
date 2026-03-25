import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        String[] strArr = my_string.split(" ");
        
        List<String> answer = new ArrayList<String>();
        
        for(String str : strArr) {
            if (!"".equals(str)) {
                answer.add(str);
            }
        }
        
        return answer.stream().toArray(String[]::new);
    }
}