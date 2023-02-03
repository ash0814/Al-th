#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
// using namespace std;
asdfdasf // 효율성 테스트 통과 못함 2/4
bool scompare(std::string &a, std::string &b){
    return a.length() < b.length() ;
}
bool diff(std::string &a, std::string &b) {
    std::string temp;
    // std::cout << a << "| "<< b << std::endl;
    int i =0;
    while(a[i]) {
        if (a[i] != b[i]) {
            // std::cout << "TEST :" << a[i]<<" : " << b[i] << std::endl;
            ++i;
            return false;
        }
        ++i;
    }
    return true;
}
bool solution(std::vector<std::string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(),phone_book.end(),scompare);
    int p_size = phone_book.size();
    for (int i =0; i<p_size-1; ++i) {
        for (int j=i+1; j<p_size; ++j) {
            if(diff(phone_book[i],phone_book[j]) == true) {
                return false;
            }
        }
    }
    return true;
}