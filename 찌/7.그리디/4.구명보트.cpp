#include <string>
#include <vector>
#include <algorithm>

#include <iostream>

using namespace std;

// 정렬을 해도 되는 건지
// 정렬을 하면 안되는 건지!
// 두명씩 밖에 못탐?

int solution(vector<int> people, int limit) {
    int answer = 0;

    sort(people.begin(), people.end());

    // 큰거를 담고 남은공간에 작은 것을 담는다

    int firstIndex = 0;
    for (int i = people.size() - 1; i >= 0;) {
        //어짜피 i만 줄어들어
        // 넘어갔을 때! > 이하이거나 같을 경우
        if (firstIndex > i) {
            break;
        }
        // 같을때
        else if (firstIndex == i) {
            answer++;
            break;
        }
        //초과
        if (people[i] + people[firstIndex] > limit) {
            answer++;
            i--;
        }
        // 이하이거나 같음
        else {
            answer++;
            firstIndex++;
            i--;
        }
    }

    return answer;
}