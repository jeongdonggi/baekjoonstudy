import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        List<String> answer = new ArrayList<String>();
        
        myStr = myStr.replace("a"," ").replace("b"," ").replace("c"," ");
        if ("".equals(myStr.replace(" ",""))) {
            return new String[]{"EMPTY"};
        }
        
        for(String str : myStr.split(" ")) {
            if (!"".equals(str)) {
                answer.add(str);
            }
        }
                        
        return answer.stream().toArray(String[]::new);
    }
}