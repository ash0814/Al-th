#include <string>
#include <vector>
#include <queue>
#include <cstdio>

#include <iostream>

using namespace std;

    // while (!pq.empty()) {
    //     cout << pq.top() << " ";
    //     pq.pop();
    // }
    // cout << endl;
int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int> > pq;

    for (int i = 0; i < scoville.size(); i++) {
        pq.push(scoville[i]);
    }


    while (1) {
        // top이 가장 작은 건데 K보다 큰거니까 조건에 만족!
        if (pq.top() >= K)
            return answer; // 탈출 조건

        // 2개 이상 일때!
        if (pq.size() >= 2) {
            // 처음 것 빼기
            int min = pq.top();
            pq.pop();
            // 두번째 빼기
            int min2 = pq.top();
            pq.pop();
            // 조합식으로 다시한번 추가하기!
            pq.push(min + min2 * 2);
        }
        else { // 두개 보다 작고 K보다 작을 때는 결과 값이 없으니까
            return -1;
        }
        answer++;
    }
    // queue에 추가하고 두개 빼고 연산하고, 다시 넣고를 반복하고 횟수 계산하고
    // 맨앞에 있는 것이 k보다 크면 그때 연산횟수 return
    // 맨앞이 작으면 -1
}