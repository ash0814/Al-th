#include <string>
#include <vector>

using namespace std;

// 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
// 큰거에서 부터 작게 가게하기

// 24 * 1 >> 24 + 24 + 1 + 1 + 4 >> 54
// 12 * 2 >> 12 + 12 + 2 + 2 + 4 >> 32
// 8 * 3 >> 8 + 8 + 3 + 3 + 4 >> 26
// 6 * 4 >> 6 + 6 + 4 + 4 + 4 >> 24 여기서 가로 + 2 세로 + 2

#include <iostream>

vector<int> solution(int brown, int yellow) {
    vector<int> answer;

    for (int i = 1; i < yellow; i++) {
        if (yellow % i != 0) {
            continue;
        }
        int j = yellow / i;
        if (brown == j * 2 + i * 2 + 4) {
            answer.push_back(j + 2);
            answer.push_back(i + 2);
            return answer;
        }
    }
}
