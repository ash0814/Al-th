#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int sum = 0;

    // 다리
    deque<int> d;

    // 다 0으로 채우기
    for (int i = 0; i < bridge_length; i++)
        d.push_back(0);

    //  트럭 배열
    for (int i = 0; i < truck_weights.size(); ) {
        // 맨 처음에 덱에서 빼기전에 합에서 빼주기! >> 다리에서 내려가서 무게를 뺀다!
        sum -= d.front();
        // 원소 하나 빼기! 다리에서 내려간다.
        d.pop_front();
        // 트럭 더미에서 하나 꺼내서 sum에다가 더해주기
        sum += truck_weights[i];
        // 무게보다 덜 나가면
        if (sum <= weight) {
            // 벡터에서 꺼내고 다리에 넣기
            d.push_back(truck_weights[i++]); 
        }
        // 무게보다 더 나가면
        else {
            // 무게를 초기화 시키고
            sum -= truck_weights[i];
            // 0을 추가해주기
            d.push_back(0);
        }
        // 시간지나가게 하기
        ++answer;
    }

    // 마지막에 추가된 상황에 다리길이 만큼을 가야되니까 다리길이 더하기
    return answer + bridge_length;
}