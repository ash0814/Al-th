package skill_check_test_level_1;

public class Problem2 {

    public boolean solution(int x) {
        Integer original = x;
        Integer acc = 0;
        for (; ; ) {
            if (x < 10) {
                acc += x;
                break;
            } else {
                acc += x % 10;
                x /= 10;
            }
        }
        return original % acc == 0;
    }

}
