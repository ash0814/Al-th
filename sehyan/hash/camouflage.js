HashMap = function () { this.map = new Array(); };
HashMap.prototype = {
  set: function (key) {
    if (this.map[key] == undefined)
      this.map[key] = 2;
    else
      this.map[key]++;
  },
  get: function (key) { return this.map[key] },
  size: function () {
    let size = 0;
    for (i in this.map) {
      size++;
    }
    return size;
  },
  result: function () {
    let arr = new Array();
    for (i in this.map) {
      arr.push(this.get(i));
    }
    return arr;
  }
}

function solution(clothes) {
  var answer = 1;
  let map = new HashMap();
  clothes.forEach(element => {
    map.set(element[1]);
  });
  map.result().forEach(element => {
    answer *= element;
  });
  answer--;
  return answer;
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]));
console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]));

// [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
// [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3