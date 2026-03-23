class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int sum = 0;
        int mul = 1;
        
        for (int num : num_list) {
            sum += num;
            mul *= num;
        }
        
        if (num_list.length >= 11) {
            answer = sum;
        } else {
            answer = mul;
        }
        
        return answer;
    }
}