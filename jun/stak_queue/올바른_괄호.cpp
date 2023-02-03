#include<string>
#include <iostream>

// using namespace std;

bool solution(std::string s)
{
    int an =0;
    bool answer = true;
    if( s[0] == ')')
        return false;
    for(int i=0; i<s.length(); ++i)
    {
        
        if(s[i] == '(' )
            ++an;
        if(s[i] == ')')
            --an;
        if (an < 0)
            return false;
    }
    if (an != 0)
        answer = false;

    return answer;
}