const getPermutations= function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index+1)] // 해당하는 fixed를 제외한 나머지 배열 
    const permutations = getPermutations(rest, selectNumber - 1); // 나머지에 대해 순열을 구한다.
    const attached = permutations.map((permutation) => [fixed, ...permutation]); // 돌아온 순열에 대해 떼 놓은(fixed) 값 붙이기
    results.push(...attached); // 배열 spread syntax 로 모두다 push
  });

  return results; // 결과 담긴 results return
};
// const example = [1,2,3,4];
// const result = getCombinations(example, 3);
// console.log(result);

function is_prime(num) {
  if (num == 1 || num == 0)
    return false;
  if (num == 2)
    return true;
  for (let i = 2; i < num; i++) {
    if (num % i == 0)
      return false;
  }
  return true;
}

function solution(numbers) {
    var answer = 0;
    let map = new Map();

    let n = [...numbers];
    for (let i = 1; i <= n.length; i++) 
    {
      const perm = getPermutations(n, i);
      for (let j = 0; j < perm.length; j++) {
        let num = "";
        for (let k = 0; k < perm[j].length; k++)
          num += perm[j][k];
        if (is_prime(parseInt(num)) == true) {
          if (map.has(parseInt(num)) == false) {
            map.set(parseInt(num), num);
            // console.log(num);
            answer++;
          }
        }
      }
    }
    return answer;
}

console.log(solution("011"));

// "17"	3
// "011"	2