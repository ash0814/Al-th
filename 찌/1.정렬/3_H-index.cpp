#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// greater<int> 로 대체 가능
bool cmp(int a, int b) {
    return a > b;
}

int solution(vector<int> citations) {
    int answer = 0;

    // n편중 h번 이상 인용된 논문이 h편 이상! h의 최댓값이 H-index
    // 정렬을 해서 자기가 나오는 곳까지 숫자를 센다
    // index + 1이 값보다 처음 커지는 곳의 전 index를 보내면 되니까!

    sort(citations.begin(), citations.end(), cmp);

    // 먼저 f 의 값을 가장 큰 값에서 가장 낮은 값으로 정렬합니다.
    // 그런 다음 f 가 위치보다 크거나 같은 마지막 위치를 찾습니다
    // i <= citations[i]
    for (int i = 0; i < citations.size(); i++) {
        if (i + 1 > citations[i]) // i + 1의 위치보다 f가 작으면 i가 마지막 위치니까
            return i;
    }
    // 생각 좀 같이 해줄 사람!
}