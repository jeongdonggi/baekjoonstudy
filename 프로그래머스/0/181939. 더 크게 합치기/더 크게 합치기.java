class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int one = Integer.parseInt(a+""+b);
        int two = Integer.parseInt(b+""+a);
        return Math.max(one, two);
    }
}