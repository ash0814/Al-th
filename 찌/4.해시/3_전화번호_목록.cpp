#include <string>
#include <vector>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    return answer;
}


// #include <string>
// #include <vector>
// #include <map>
// #include <algorithm>
// #include <iostream>
// #include <cstring>

// using namespace std;

// bool solution(vector<string> phone_book) {
//     bool answer = true;

//     sort(phone_book.begin(), phone_book.end());
    
//     for (int i = 0; i + 1 < phone_book.size(); i++)
//     {
//         if (phone_book[i] == phone_book[i + 1].substr(0, phone_book[i].size()))
//             return (false);
//     }
//     return answer;
// }