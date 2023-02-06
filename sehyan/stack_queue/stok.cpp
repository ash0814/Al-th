#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices)
{
  vector<int> answer;
  for (int i = 0; i < prices.size(); i++)
  {
    answer.push_back(0);
    for (int j = i + 1; j < prices.size(); j++)
    {
      // cout << prices[i] << ", " << prices[j] << endl;
      if (prices[i] > prices[j])
      {
        answer[i] = j - i;
        break;
      }
      else
      {
        answer[i]++;
      }
    }
  }
  return answer;
}

int main()
{
  vector<int> test1;
  test1.push_back(1);
  test1.push_back(2);
  test1.push_back(3);
  test1.push_back(2);
  test1.push_back(3);

  vector<int> res = solution(test1);
  for (int i = 0; i < res.size(); i++)
    cout << res[i] << endl;
}
