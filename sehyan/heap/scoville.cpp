#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K)
{
  int answer = 0;
  int cnt = 0;
  sort(scoville.begin(), scoville.end());
  while (scoville[0] < K)
  {
    if (scoville.size() < 2)
      return -1;
    cnt = scoville[0] + (scoville[1] * 2);
    scoville.erase(scoville.begin());
    scoville.erase(scoville.begin());
    scoville.push_back(cnt);
    for (int i = 0; i < scoville.size(); i++)
      cout << scoville[i] << ", ";
    cout << endl;
    answer++;
    sort(scoville.begin(), scoville.end());
  }
  return answer;
}

int main()
{
  vector<int> test1;
  test1.push_back(1);
  test1.push_back(2);
  test1.push_back(3);
  test1.push_back(9);
  test1.push_back(10);
  test1.push_back(12);

  int res = solution(test1, 7);
  cout << res << endl;
}