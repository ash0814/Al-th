function solution(numbers, target) {
  var answer = 0;
  let sign = [];
  let arr = ["a", "b"];

  function recurtion(n, str) {
    if (n === 0) {
      sign.push(str)
      return
    }
    for (let i = 0; i < 2; i++) {
      recurtion(n - 1, `${str}${arr[i]}`)
    }
  }
  recurtion(numbers.length, "");

  sign.forEach((element) => {
    let res = 0;
    for (let i = 0; i < element.length; i++) {
      if (element[i] == 'a') {
        res += numbers[i];
      } else {
        res -= numbers[i];
      }
    }
    if (res == target)
      answer++;
  })

  return answer;
}


console.log(solution([4, 1, 2, 1], 4));