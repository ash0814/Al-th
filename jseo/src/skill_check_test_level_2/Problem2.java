package skill_check_test_level_2;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

public class Problem2 {

    public int solution(int[] cards) {
        int size = 0;
        int groupSize = 0;
        int offset = 0;
        int index = 0;
        Map<Integer, Boolean> visited = new ConcurrentHashMap<>();
        List<Integer> groupSizes = new ArrayList<>();
        while (true) {
            index = cards[index] - 1;
            if (visited.getOrDefault(index, false)) {
                index = ++offset;
                groupSizes.add(groupSize);
                groupSize = 0;
                if (size == cards.length) {
                    break;
                }
            } else {
                size++;
                groupSize++;
                visited.put(index, true);
            }
        }
        groupSizes.sort(Comparator.reverseOrder());
        return groupSizes.get(0) * groupSizes.get(1);
    }

}
