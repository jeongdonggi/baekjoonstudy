class Solution {
    public String solution(String my_string, int[][] queries) {        
        for(int[] query : queries) {
            String temp = my_string.substring(0, query[0]);
            for (int i = query[1]; i >= query[0]; i--) {
                temp += my_string.charAt(i);
            }
            temp += my_string.substring(query[1] + 1, my_string.length());
            my_string = temp;
        }
        
        return my_string;
    }
}