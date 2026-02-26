class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        String[] arr = {"", ""};
        
        for (int num : num_list) {
            arr[num % 2] += String.valueOf(num);
        }

        return Integer.parseInt(arr[0]) + Integer.parseInt(arr[1]);
    }
}