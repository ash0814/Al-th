#include <string>
#include <vector>
#include <iostream>
#include <map>
// using namespace std;
unsolved
int solution(std::vector<std::vector<std::string> > clothes) {
    int answer = 0;
    std::vector<int> i_list;
    std::map<std::string,int> i_map;
    for(int i =0; i<clothes.size(); ++i ) {
        i_map[clothes[i][1]] += 1;
    }
    std::map<std::string,int>::iterator it = i_map.begin();
    for(std::map<std::string,int>::iterator it = i_map.begin(); it != i_map.end(); ++it) {
        std::cout << it->second << std::endl;
    }
    return answer;
}