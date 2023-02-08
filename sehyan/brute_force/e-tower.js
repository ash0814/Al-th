function solution(n, wires) {
  var answer = -1;

  for (let i = 0; i < n - 1; i++) {
    let a = new Set();
    let b = new Set();
    a.add(wires[i][0]);
    b.add(wires[i][1]);
    console.log("=============", wires[i]);
    let filtered = wires.filter((element, index) => index !== i);
    // filtered.forEach((ele, idx) => {
    //   console.log(ele);
    for (let j = 0; j < n - 2; j++) {
      // 두 숫자 다 아무 set에도 없을 때 => 보류해뒀다가 다시 처리?1
      if (a.has(filtered[j][0]) === true || a.has(filtered[j][1]) === true) {
        a.add(filtered[j][0]);
        a.add(filtered[j][1]);
      } else {
        b.add(filtered[j][0]);
        b.add(filtered[j][1]);
      }
    }

    // })
    console.log("a", a, "b", b, "\n\n")
    if (answer > Math.abs(a.size - b.size) || answer == -1)
      answer = Math.abs(a.size - b.size);
  }
  return answer;
}

console.log(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))




// function solution(n, wires) {
//   var answer = -1;
  
//   for (let i = 0; i < n-1; i++) {
//       let a = new Set();
//       let b = new Set();
//       let filtered = wires.filter((element, index) => index !== i);
//       filtered.forEach((ele, idx) => {
//           // console.log(idx, ele);
//           if (idx == 0) {
//               a.add(ele[0]);
//               a.add(ele[1]);
//           } else {
//               if (a.has(ele[0]) == false && a.has(ele[1]) == false) {
//                   b.add(ele[0]);
//                   b.add(ele[1]);
//               } else {
//                   a.add(ele[0]);
//                   a.add(ele[1]);
//               }  
//           }
//       })
//       if (answer > Math.abs(a.size - b.size) || answer == -1)
//           answer = Math.abs(a.size - b.size);
//   }
//   return answer;
// }