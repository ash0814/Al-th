#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    int start = 0;
    // 전체를 도는데 number크기에서 k를 뺀 것 만큼만 돈다
    for (int i = 0; i < number.size() - k; i++) {
        // max 초기화
        char max = 0;
        // (초기화되는)start부터 k + i번째 까지
        for (int j = start; j <= k + i; j++) {
            if (max < number[j]) {
                // max 에 대입
                max = number[j];
                // 위치 변경, 가장 큰것의 다음 것부터 돌아야하기 때문에!
                start = j + 1;
            }
        }
        // for문을 돌면서 나온 max 추가
        answer += max;
    }
    return answer;
}