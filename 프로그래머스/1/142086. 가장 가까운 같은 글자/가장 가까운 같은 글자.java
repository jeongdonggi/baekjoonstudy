import java.util.*;

class Solution {
    public int[] solution(String s) {
        List<Integer> answer = new ArrayList<>();
        Map<Character, Integer> point = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (point.containsKey(c)){ // key가 없으면 value에 현재 인덱스 넣고 -1 
                answer.add(i - point.get(c));
            } 
            else { // key가 있으면 value랑 지금 위치 비교해서 값 넣고 value 업데이트
                answer.add(-1);
            }
            point.put(c, i);
        }
                
        return answer.stream().mapToInt(Integer::intValue).toArray(); // array로 변경 해야됨
    }
}