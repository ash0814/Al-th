#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> leftStack;

    //문자열을 돌면서
    for (int i = 0; i < s.length(); i++) {
        // ( 만 넣을 거야
        if (s[i] == '(')
            leftStack.push(s[i]);
        // ) 나오면 뺄 건데
        else if (s[i] == ')') {
            // 맨위에 있다면 한쌍이니까 빼도
            if (!leftStack.empty() && leftStack.top() == '(')
                leftStack.pop();
            // 그게 아니라면 싸이 안맞으니까
            else
                return false;
        }
    }

    // 남아서 짝이 안맞는경우
    bool answer = leftStack.size() == 0 ? true : false;
    return answer;
}

// core dump >> 비어있을 때 접근을 하면 안되서!
// 19번 줄과 같이 있을 때! 라는 조건을 주어야함!