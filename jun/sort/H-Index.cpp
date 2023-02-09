#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
// using namespace std;
bool scompare(std::pair<int,int> &a, std::pair<int,int> &b)
{
    if(a.second < b.second)
        return false;
    return true;
}   
int solution(std::vector<int> citations) {
    int answer = 0;
    std::vector<int> temp_list;
    // std::map<int,int> an_map;
    std::vector<std::pair<int,int> > i_vec;
    int count=0;
    for (int i=0; i<citations.size(); ++i) {
        temp_list=citations;
        count =0;

        for(int j=0; j<citations.size(); ++j) {
            temp_list[j] = temp_list[j] - citations[i];
        }
        for(int k=0; k<citations.size(); ++k) {
            if (citations[i] == 0)
                continue;
            std::cout << temp_list[k] << " ";
        }
        std::cout << std::endl;
        std::cout <<"---------" << std::endl;
        for(int k=0; k<citations.size(); ++k) {
            if(citations[i] == 0)
                break;
            if(temp_list[k] >=0)
                count++;
        }
        std::cout << "TETS : " << count << std::endl;
        if (citations[i] == 0) {
            i_vec.push_back(std::pair(citations[i],0));
            continue;
        }
        // an_map[citations[i]] = count;
        i_vec.push_back(std::pair(citations[i],count));
    }
    
    for(int i=0; i<i_vec.size(); ++i) {
        std::cout << i_vec[i].second << " ";
    }
    std::cout << std::endl;
    sort(i_vec.begin(),i_vec.end(),scompare);
    std::cout << " sdlkflaskdlksdj " << std::endl;
    for(int i=0; i<i_vec.size(); ++i) {
        std::cout << i_vec[i].first <<" "<< i_vec[i].second << " ";
    }
    
    return answer;
}