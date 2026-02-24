class Solution {
    public int solution(int[] numbers) {        
        for (int i = 0; i < numbers.length - 1; i++ ) {
            for (int j = 0; j < numbers.length - 1; j++) {
                if (numbers[j] < numbers[j + 1]) { // 역순
                    int temp = numbers[j];
                    numbers[j] = numbers[j+1];
                    numbers[j+1] = temp;
                }
            }
        }
        return numbers[0] * numbers[1];
    }
}