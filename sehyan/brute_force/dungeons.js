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

function solution(k, dungeons) {
  var answer = 0;
  let step = [];
  let max = 0;
  for (let i = 0; i < dungeons.length; i++)
    step.push(i);
  const perm = getPermutations(step, step.length);
  for (let i = 0; i < perm.length; i++){
    max = 0;
    let kk = k;
    for (let j = 0; j < step.length; j++) {
      console.log(dungeons[perm[i][j]]);
      if (kk >= dungeons[perm[i][j]][0]) {
        kk -= dungeons[perm[i][j]][1];
        max++;
      }
      else
        break;
      console.log(kk);
    }
    if (answer < max)
      answer = max;
    console.log("==");
  }
  return answer;
}

console.log(solution(80, ([[80,20],[50,40],[30,10]])));
// 80	[[80,20],[50,40],[30,10]]	3