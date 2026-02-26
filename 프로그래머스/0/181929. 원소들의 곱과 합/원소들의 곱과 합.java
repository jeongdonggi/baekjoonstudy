class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int mul = 1;
        int plus = 0;
        
        for (int num : num_list) {
            mul *= num;
            plus += num;
        }
        
        System.out.print(mul + " " + plus);
        
        return mul < plus * plus ? 1 : 0;
    }
}