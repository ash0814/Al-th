#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int count;
    int max = 0;
    // 두번째 벡터를 처음부터 순열과 조합을 통해 정렬을 하고 
    // 거기서 두번째 벡터 두번째를 빼면서 들어갈 수 있는 횟수를 정하고
    // 그게 기준값 보다 크면 max를 교체!
    sort(dungeons.begin(), dungeons.end());
    do {
        count = 0;
        int line = k;
        for (int i = 0; i < dungeons.size(); i++) {
            
            if (line >= dungeons[i][0]) {
                line -= dungeons[i][1];
                ++count;
            }
        }
        max = max > count ? max : count;
    }
    while (next_permutation(dungeons.begin(), dungeons.end()))
        ;
    return max;
}