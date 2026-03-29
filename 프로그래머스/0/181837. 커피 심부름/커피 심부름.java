class Solution {
    public int solution(String[] order) {
        int answer = 0;
        for (String cafe : order) {
            if (cafe.contains("americano") || "anything".equals(cafe)) {
                answer += 4500;
            } else {
                answer += 5000;
            }
        }
        
        return answer;
    }
}