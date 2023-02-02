#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// 순열과 조합은 시간초과!
// 무조건 문자열로 비교를 해야함!


// 두 개의 숫자를 정렬할 때 기준을 두자!
// 두 숫자의 string합을 비교하여 우위에 둘 숫자를 결정

//comp bool반환하는 함수
bool comp(string a, string b) {
    return a + b > b + a;
    // 이런 기준을  vector 내부의 원소들이 다 맞을 때 까지 돈다!
}
// true반환 > 두 매개변수가 정렬! >> 가만히
// false반환 > 자동적으로 바꿔줌 a,b의 위치를 Temp에서 변경

string solution(vector<int> numbers) {
    string answer = "";

    // 문자열 비교로 해결을 해 나아가야하기 때문에 문자열 vector에 따로!
    vector<string> stringTemp;
    for (int i = 0; i < numbers.size(); i++)
        stringTemp.push_back(to_string(numbers[i]));

    // 우리 입맛 대로 정렬!
    sort(stringTemp.begin(), stringTemp.end(), comp); 

    //  다합친 결과
    for (int i = 0; i < stringTemp.size(); i++)
        answer += stringTemp[i];
    
    // 처음이 0이면 그 뒤의 것도 다 0 이어서  return 0 위함
    if (stringTemp[0] == "0")
        return "0";

    return answer;
}