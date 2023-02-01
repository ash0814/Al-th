function solution(nums) {
  var answer = 0;
  let i;
  let map = new Map();

  for (i = 0; i < nums.length; i++) {
    map.set(nums[i], nums[i]);
  }
  if (map.size > nums.length / 2)
    answer = nums.length / 2;
  else
    answer = map.size;
  return answer;
}

solution([3, 1, 2, 3]);

// [3,1,2,3]	2
// [3,3,3,2,2,4]	3
// [3,3,3,2,2,2]	2