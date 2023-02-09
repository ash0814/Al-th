import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var caseCount = 0

    func DFS(_ index: Int, _ sum: Int) {
        if (index == numbers.count) {
            if (sum == target) {caseCount += 1}
            return
        }
        DFS(index + 1, sum + numbers[index])
        DFS(index + 1, sum - numbers[index])
    }

    DFS(0, 0)

    return caseCount
}
