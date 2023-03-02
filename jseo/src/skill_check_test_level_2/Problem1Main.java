package skill_check_test_level_2;

import skill_check_test_level_1.Problem2;

import java.util.Arrays;

public class Problem1Main {

    static public void grade(int[] input, int[] output) {
        Boolean equals = Arrays.equals(input, output);
        if (equals) {
            System.out.println("OK");
        } else {
            System.out.println("KO");
        }
    }

    static public void main(String[] args) {
        Problem1 problem1 = new Problem1();
        Integer input1 = 4;
        int[] output1 = {1, 2, 9, 3, 10, 8, 4, 5, 6, 7};
        Integer input2 = 5;
        int[] output2 = {1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9};
        Integer input3 = 6;
        int[] output3 = {1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11};
        grade(problem1.solution(input1), output1);
        grade(problem1.solution(input2), output2);
        grade(problem1.solution(input3), output3);
    }

}
