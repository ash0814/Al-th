#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

bool comp(string a, string b)
{
  if (a.size() == b.size())
    return a < b;
  return a.size() < b.size();
}

bool solution(vector<string> phone_book)
{
  bool answer = true;

  std::sort(phone_book.begin(), phone_book.end(), comp);

  for (int i = 0; i < phone_book.size(); i++)
  {
    for (int j = i + 1; j < phone_book.size(); j++)
    {
      if (phone_book[i].length() < phone_book[j].length())
      {
        if (strncmp(phone_book[i].c_str(), phone_book[j].c_str(), phone_book[i].length()) == 0)
        {
          answer = false;
          break;
        }
      }
    }
    if (answer == false)
      break;
  }
  return answer;
}

int main()
{
  vector<string> test1;
  test1.push_back("119");
  test1.push_back("97674223");
  test1.push_back("11955244");

  cout << solution(test1) << endl;
}

// ["119", "97674223", "1195524421"]	false
// ["123","456","789"]	true
// ["12","123","1235","567","88"]	false