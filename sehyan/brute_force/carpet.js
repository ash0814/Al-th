function cal(b, y, x) {
    let a;
    if (b * x + 4 * x - 2*x * x == 2*b + 2*y)
        return x;
    return -1;
}

function solution(brown, yellow) {
    var answer = [];
    let x = 0;
    let y = 0;
    while (x < 2000)
    {
        if (cal(brown, yellow, x) != -1)
        {
            y = (brown + yellow) / x;
            break;
        }
        x++;
    }
    if (x > y) {
        answer[0] = x;
        answer[1] = y;
    } else {
        answer[0] = y;
        answer[1] = x;
    }
    return answer;
}
