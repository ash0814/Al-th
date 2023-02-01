function solution(participant, completion) {
  participant.sort();
  completion.sort();
  let i;
  for (i = 0; i < completion.length; i++) {
    if (participant[i] != completion[i])
      return participant[i];
  }
  return participant[completion.length];
}

// solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]);
console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]));
console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]));
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]));
// ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
// ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
// ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
