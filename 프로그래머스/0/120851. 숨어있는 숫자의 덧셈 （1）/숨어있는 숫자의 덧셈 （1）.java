class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        String number = "123456789";
        
        for (String s : my_string.split("")) {
            if (number.contains(s)) {
                answer += Integer.parseInt(s);
            }
        }
        
        return answer;
    }
}