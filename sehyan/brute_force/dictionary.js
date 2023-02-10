
function solution(word) {
  var answer = 0;

  let result = [];

  let arr = ["", "A", "E", "I", "O", "U"];

  function recurtion(n, str) {
    if (n === 0) {
      result.push(str)
      return
    }
    for (let i = 0; i < 6; i++) {
      recurtion(n - 1, `${str}${arr[i]}`)
    }
  }
  recurtion(5, "");
  let data = [...new Set(result)].sort();
  console.log(data);
  answer = data.indexOf(word);
  return answer;
}

console.log(solution("AAAAE"));

