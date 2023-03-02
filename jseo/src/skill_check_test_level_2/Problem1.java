package skill_check_test_level_2;

import java.util.ArrayList;
import java.util.List;

public class Problem1 {

    private void print(int[][] map, int size) {
        for (Integer i = 0; i < size; i++) {
            for (Integer j = 0; j < size; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.print("\n");
        }
    }

    public int[][] generateSnailMap(int n) {
        Integer trail = 1;
        Integer iteration = n;
        Integer rowIndex = 1;
        Integer colIndex = 1;
        int[] answer = {};
        int[][] map = new int[n + 1][n + 1];
        while (true) {
            for (Integer i = 1; i <= iteration; i++) {
                map[rowIndex++][colIndex] = trail++;
            }
            colIndex++;
            rowIndex--;
            if (--iteration == 0) {
                break;
            }
            for (Integer i = 1; i <= iteration; i++) {
                map[rowIndex][colIndex++] = trail++;
            }
            rowIndex--;
            colIndex--;
            colIndex--;
            if (--iteration == 0) {
                break;
            }
            for (Integer i = 1; i <= iteration; i++) {
                map[rowIndex--][colIndex--] = trail++;
            }
            rowIndex++;
            rowIndex++;
            colIndex++;
            if (--iteration == 0) {
                break;
            }
        }
        return map;
    }

    int[] convertMultiArrayToSingleArray(int[][] map, int n) {
        List<Integer> list = new ArrayList<>();
        for (Integer i = 0; i < n + 1; i++) {
            for (Integer j = 0; j < n + 1; j++) {
                if (map[i][j] != 0) {
                    list.add(map[i][j]);
                }
            }
        }
        return list.stream().mapToInt(e -> e).toArray();
    }

    public int[] solution(int n) {
        int[][] map = generateSnailMap(n);
        return convertMultiArrayToSingleArray(map, n);
    }

}
