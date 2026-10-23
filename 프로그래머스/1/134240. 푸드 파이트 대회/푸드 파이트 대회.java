class Solution {
    public String solution(int[] food) {
        StringBuilder answer1 = new StringBuilder();
        StringBuilder answer2 = new StringBuilder();
        
        for (int i = 1; i < food.length; i++) {
            for (int j = 0; j < (int)(food[i] / 2); j++) {
                answer1.append(i);
            }
        }
        
        for (int j = answer1.length() - 1; j >= 0; j--) {
            answer2.append(answer1.charAt(j));
        }
        
        answer1.append(0);
        
        return answer1.toString() + answer2.toString();
    }
}