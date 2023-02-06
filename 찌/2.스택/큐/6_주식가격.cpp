#include <string>
#include <vector>
#include <deque>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    deque<int> d;
    // 벡터, 덱에다 옯기기
    for (int i = 0; i < prices.size(); i++) {
        d.push_back(prices[i]);
    }

    // 덱의 사이즈가 0이 되면 멈추기
    while (d.size() != 0) {
        // 맨 처음 값뽑아내기
        int first = d.front();
        // 덱에서 뽑아내기
        d.pop_front();
        // 자기가 큰게 유지되는 횟수
        int count = 0;
        // 나 다음부터 덱에 있는 것에서 확인하기 위함
        for (int i = 0; i < d.size(); i++) {
            // 일단 카운트를 추가하고
            count++;
            // 처음 것이 어느 순간 작아지면 멈추고
            if (first > d[i]) {
                break;
            }
        }
        // answer에 추가!
        answer.push_back(count);
    }

    // 결과 리턴!
    return answer;
}