#include <string>
#include <vector>
#include <map>

#include <iostream>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;

    // map으로 해야겠다
    map<string, int> s;

    // map에 같은 종류일 때 증가 시키기
    for (int i = 0; i < clothes.size(); i++) {
        ++s[clothes[i][1]];
    }
    for (map<string, int>::iterator it = s.begin(); it != s.end(); ++it) {
        answer *= (it->second + 1); // 아무것도 안고르는 경우 추가해주기
    }
    return answer - 1; // x x x 를 픽한 경우 빼주기
}