#include <string>
#include <vector>
#include <iostream>
// using namespace std;

std::vector<int> solution(std::vector<int> prices) {
    std::vector<int> answer;
    int temp;
    for (int i =0; i<prices.size(); ++i)
    {
        temp =0;
        for (int j =i+1; j<prices.size(); ++j)
        {
            // std::cout << prices[i] <<" "<< prices[j] << std::endl;
            if (prices[i] > prices[j]) {
                temp++;
                break;
            }
            else
                temp++;
        }
        // std::cout << temp << std::endl;
        answer.push_back(temp);
    }
    return answer;
}