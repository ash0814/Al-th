package skill_check_test_level_1;

public class Problem1 {

    public int solution(int n) {
        Integer answer = 0;
        for (Integer i = 1; i <= n; i++) {
            if (i > n / i) {
                break;
            }
            if (n % i == 0) {
                answer += i;
                if (n / i != i) {
                    answer += n / i;
                }
            }
        }
        return answer;
    }

}
