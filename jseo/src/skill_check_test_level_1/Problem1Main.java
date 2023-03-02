package skill_check_test_level_1;

public class Problem1Main {

    static public void grade(Integer input, Integer output) {
        Boolean equals = input == output;
        if (equals) {
            System.out.println("OK");
        } else {
            System.out.println("KO");
        }
    }

    static public void main(String[] args) {
        Problem1 problem1 = new Problem1();
        Integer input1 = 12;
        Integer input2 = 5;
        Integer input3 = 9;
        grade(problem1.solution(input1), 28);
        grade(problem1.solution(input2), 6);
        grade(problem1.solution(input3), 13);
    }

}
