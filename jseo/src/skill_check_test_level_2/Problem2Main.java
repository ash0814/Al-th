package skill_check_test_level_2;

public class Problem2Main {

    static public void grade(int input, int output) {
        Boolean equals = input == output;
        if (equals) {
            System.out.println("OK");

        } else {
            System.out.println("KO");
        }
    }

    static public void main(String[] args) {
        Problem2 problem2 = new Problem2();
        int[] input = {8, 6, 3, 7, 2, 5, 1, 4};
        int output = 12;
        grade(problem2.solution(input), output);
    }

}
