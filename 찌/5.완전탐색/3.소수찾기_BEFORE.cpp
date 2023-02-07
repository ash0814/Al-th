#include <string>
#include <vector>

using namespace std;

// 전에 품
int solution(string numbers) {
    int answer = 0;
    return answer;
}

// //next_permutation 을 사용해서 문제 풀기

// #include <string>
// #include <vector>
// #include <iostream>
// #include <algorithm>
// #include <string>
// #include <unordered_set>

// using namespace std;


// //소수확인!
// int primeCheck(int i)
// {
//     if (i == 1 || i == 0)
//         return (0);
//     for (int j = 2; j <= i / j; j++)
//     {
//         if (i % j == 0)
//             return (0);
//     }
//     return (i);
// }

// int solution(string numbers) {
    
//     unordered_set<int> primes;
//     //정렬되지 않음, 중복 안됨
//     sort(numbers.begin(), numbers.end());
//     //순열할수 있는 7843부터 시작이 아니라 3478부터 시작할수 있게끔
//     do{
//         for(int i = 1; i < numbers.size() + 1; i++)
//         {
//             // std::cout << numbers.substr(0, i) << std::endl;
//             primes.insert(primeCheck(stoi(numbers.substr(0, i))));
//             //문자열 잘라서 소수체크하고 넣기 ,, 중복이면 못넣음
//             //ex 3 34 347 3478 3 34 348 3487
//         }
// 	}while(next_permutation(numbers.begin(),numbers.end()));
//     //순열 돌리는 함수
    
//     //unordered_set 출력하는 방법
//     // for (unordered_set<int>::iterator it = primes.begin(); it != primes.end(); it++) {
// 	// 	cout << *it << " ";
// 	// }

//     //size-1 안되는 이유 0이 없을 수도 있으니까 2같은 경우
//     primes.erase(0);
        
//     return primes.size();
// }