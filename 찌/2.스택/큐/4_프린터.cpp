#include <string> 
#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>

using namespace std;

// 돌면서 자기가 제일 크면 출력 하고 제거
// location이 몇번 째로 출력이 되는지 확인

int solution(vector<int> priorities, int location) {
    int answer = 0;

    // 덱을 사용하자!
    deque<int> q;
    for (int i = 0; i < priorities.size(); i++) {
        q.push_back(priorities[i]);
    }

    while (1)
    {
        // 한 사이클에서 최댓값을 구한다.
        deque<int>::iterator maxIt = max_element(q.begin(), q.end());
        // 처음이 최댓값이면
        if (*maxIt == *q.begin()) {
            // 뺀다
            q.pop_front();
            // 위치를 하나 줄인다.
            // 순위 업
            ++answer;
            if (location == 0)
                return answer;
        }
        // 처음이 최댓값이 아니면
        else {
            int front = q.front();
            // 맨 앞에것을 빼서
            q.pop_front();
            // 뒤로 무른다.
            q.push_back(front);
            if (location == 0) {
                location = q.size();
            }
        }
        location--;
    }

    return answer;
}