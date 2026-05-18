class Solution {
    public int solution(int[] common) {
        int answer = 0;
        
        int first = common[1] - common[0];
        int second = common[common.length -1] - common[common.length -2];
        
        if (second - first == 0) {
            answer = common[common.length -1 ] + second;
        } else {
            answer = common[common.length -1 ] * (common[1] / common[0]);
        }
        
        return answer;
    }
}