#include <string>
#include <vector>
#include <iostream>
#include <map>
// using namespace std;
// aa b 일때
// 입고 안 입을 경우 2가지 각각 a,b에 대해서 근데 둘다 안 입는 경우는 안되닌까 
// (2+1)*(1+1) -1
int solution(std::vector<std::vector<std::string> > clothes) {
    int answer = 1;
    std::vector<int> i_list;
    std::map<std::string,int> i_map;
    for(int i =0; i<clothes.size(); ++i ) {
        i_map[clothes[i][1]] += 1;
    }
    std::map<std::string,int>::iterator it = i_map.begin();
    for(std::map<std::string,int>::iter4ator it = i_map.begin(); it != i_map.end(); ++it) {
        answer *= (it->second +1);
        std::cout << it->second << std::endl;
    }
    return answer-1;
}
