class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        for (String s : my_string.split("")) {
            if (letter.equals(s)) {
                continue;
            }
            answer += s;
        }
        return answer;
    }
}