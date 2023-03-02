package skill_check_test_level_1;

public class Problem2Main {

    static public void grade(Boolean input, Boolean output) {
        Boolean equals = input == output;
        if (equals) {
            System.out.println("OK");
        } else {
            System.out.println("KO");
        }
    }

    static public void main(String[] args) {
        Problem2 problem2 = new Problem2();
        Integer input1 = 10;
        Integer input2 = 12;
        Integer input3 = 11;
        Integer input4 = 13;
        grade(problem2.solution(input1), true);
        grade(problem2.solution(input2), true);
        grade(problem2.solution(input3), false);
        grade(problem2.solution(input4), false);
    }

}
