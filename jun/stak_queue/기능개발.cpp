#include <string>
#include <vector>
#include <iostream>
// using namespace std;

std::vector<int> solution(std::vector<int> progresses, std::vector<int> speeds) {
    std::vector<int> answer;
    std::vector<int> t_list;
    std::vector<int> an_list;
    
    for(int i=0; i<progresses.size(); ++i) {
        t_list.push_back(100 - progresses[i]);
    }
    std::vector<int> tt_list;
    int put;
    for(int i=0; i<speeds.size(); ++i) {
        put = t_list[i] / speeds[i];
        if (t_list[i] % speeds[i] != 0)
            ++put;
        tt_list.push_back(put);
    }
    
    for(int i=0; i<speeds.size(); ++i) {
        std::cout << tt_list[i] << " ";
    }
    std::cout << std::endl;
    std::cout << tt_list.size() << std::endl;
    int first=0;

    for(int i =0; i<tt_list.size(); ++i){
        if (tt_list[i] > 0) {
            first = tt_list[i];
            std::cout << "first : " << first <<" "<<tt_list[i] << std::endl;
        }
        else
            continue;
        for (int j =i; j<tt_list.size(); ++j){
            tt_list[j] =  tt_list[j] - first;
            std::cout << "TEST : " << tt_list[j] << "\n";
        }
        int an =0;
        for(int k =i; k<tt_list.size(); ++k) {
            std::cout << "k :" << k << std::endl;
            if(tt_list[k] <= 0)
                    ++an;
            if(tt_list[k] > 0)
                 break;
        }
        an_list.push_back(an);
    }
 
    for(int i=0; i<speeds.size(); ++i) {
        std::cout << tt_list[i] << " ";
    }
    std::cout << std::endl;

    for(int i=0; i<an_list.size(); ++i) {
        std::cout << an_list[i] << " ";
    }
    std::cout << std::endl;
    return an_list;
}