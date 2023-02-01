// github fork check

#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int origianl_length = nums.size() / 2;
    // 이 부분이 없으면 N / 2마리의 폰켓몬 선택이 안되어서!

    // 중복을 제거해서 그냥 그 vector의 길이를 세면 될거 같다!

    sort(nums.begin(),nums.end());
    // unique는 연속된 중복 원소를 vector의 제일 뒷부분으로 쓰레기값으로 보내버립니다.
    // 그래서 정렬을 하고 unique를 해야!    
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    // unique가 끝났으면 반환되는 값은 vector의 쓰레기 값의 첫번째 위치!
    // erase 로 뒤에붙은 쓰레기값을 제거해주면 백터의 중복원소를 제거하는데 성공
    
    return nums.size() >= origianl_length ? origianl_length  : nums.size();
    // 중복제거의 길이와 처음 길이를 비교해서
    // 위 식이 참이면 N / 2종류를 넘어가니까 ori로 하고
    // 거짓이면 길이보다 작아서 종류의 수가 길이보디 작아서!
}