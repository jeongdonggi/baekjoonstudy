import java.util.*;

class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> answer = new ArrayList<String>();
        
        for (String pic : picture) {
            for(int i = 0; i < k; i++) {
                StringBuilder sb = new StringBuilder();
                for (String p : pic.split("")) {
                    for (int j = 0; j < k; j++) {
                        sb.append(p);   
                    }
                }
                answer.add(sb.toString());
            }
        }
        
        return answer.stream().toArray(String[]::new);
    }
}