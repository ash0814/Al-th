function solution(arr) {
  var answer = [];
  arr.forEach((ele) => {
    if (answer[answer.length - 1] != ele)
      answer.push(ele);
  })
  return answer;
}