class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int maxNum = 0;
        
        for (int side : sides) {
            if (maxNum < side) {
                maxNum = side;
            }
            answer += side;
        }
        
        if (maxNum < (answer - maxNum)){
            return 1;
        }
        
        return 2;
    }
}