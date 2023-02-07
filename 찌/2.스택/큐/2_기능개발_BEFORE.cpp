#include <string>
#include <vector>

using namespace std;

// 전에 품
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    return answer;
}

























// #include <string>
// #include <vector>
// #include <stack>
// #include <iostream>

// using namespace std;

// vector<int> solution(vector<int> progresses, vector<int> speeds) {
//     vector<int> answer;

//     for (int i = 0; i < progresses.size(); i++)
//     {
//         for (int j = i; j < speeds.size(); j++)
//             progresses[j] += speeds[j];
//         if (progresses[i] < 100)
//         {
//             i--;
//             continue;
//         }
        
//         int k = 0, n = i;
//         vector<int>::iterator pIter = progresses.begin();
//         for (; progresses[n] >= 100 && n < progresses.size(); k++, n++)
//             {}
//         answer.push_back(k);
//         i = n - 1;
//     }
//     return answer;
// }