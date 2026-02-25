class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        String m = "aeiou";
        
        for (String s : my_string.split("")) {
            if (!m.contains(s)) {
                sb.append(s);
            }
        }
        
        return sb.toString();
    }
}