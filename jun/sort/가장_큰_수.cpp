#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
// using namespace std;
bool scompare(std::string &a, std::string &b) {
    int len=0;
    if (a.length() >= b.length())
        len = b.length();
    else 
        len = a.length();
    for(int i =0; i<len; ++i){
        if (a[i] > b[i]) {    
            std::cout << "TEST : " << a <<" "<< b <<std::endl;
            if (i == len-1)
            {
                if (len == a.length()) {
                    if (b[i+1] < a[i])
                        return true;
                    else
                        return false;
                }
                else {
                    if (a[i+1] < b[i])
                        return true;
                    else
                        return false;
                }
            }
            return true;
        }    
    }
    return false;
}
std::string solution(std::vector<int> numbers) {
    std::string answer = "";
    std::vector<std::string> temp_list;
    for (int i=0; i<numbers.size(); ++i) {
        temp_list.push_back(std::to_string(numbers[i]));
    }
    sort(temp_list.begin(),temp_list.end(),scompare);
    
    for (int i=0; i<numbers.size(); ++i) {
        std::cout << temp_list[i] << " ";
        answer += temp_list[i];
    }
    std::cout << std::endl;
    
    return answer;
}