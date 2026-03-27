import java.util.*;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        
        int arr1Len = arr1.length;
        int arr2Len = arr2.length;
        int arr1Sum = Arrays.stream(arr1).sum();
        int arr2Sum = Arrays.stream(arr2).sum();
        
        if (arr1Len != arr2Len) {
            answer = arr1Len > arr2Len ? 1 : -1;
        } else {
            if (arr1Sum != arr2Sum) {
                answer = arr1Sum > arr2Sum ? 1 : -1;
            } else {
                answer = 0;
            }
        }
        
        return answer;
    }
}