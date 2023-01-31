function solution(array, commands) {
    var answer = [];
    let i;
    for (i = 0; i < commands.length; i++) {
        let cut = array.slice(commands[i][0] - 1, commands[i][1]);
        cut.sort((a, b) => a - b);
        answer[i] = cut[commands[i][2] - 1];
    }
    return answer;
}
