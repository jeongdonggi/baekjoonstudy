class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        
        String[] myStringArr = myString.split("");
        String[] patArr = pat.split("");
        int cnt = pat.length() - 1;
        int point = myString.length() - 1;
        //
        for (int i = myStringArr.length -1; i >= 0 ; i--) {
            if (patArr[cnt].equals(myStringArr[i])) {
                --cnt;
                point = i;
                if (cnt == -1) {
                    break;
                }
            } else {
                cnt = patArr.length -1;
            }
        }
        answer = myString.substring(0, point + pat.length());
        
        return answer;
    }
}