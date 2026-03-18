import java.util.*;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        List<String> strArr = new ArrayList<String>();
        
        for(int i = 0; i < todo_list.length; i++) {
            if (finished[i] == false) {
                strArr.add(todo_list[i]);
            }
        }
        return strArr.stream().toArray(String[]::new);
    }
}