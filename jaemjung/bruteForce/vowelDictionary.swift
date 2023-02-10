import Foundation

func solution(_ word:String) -> Int {
    let vowels: [String] = ["A", "E", "I", "O", "U"]
    var count: Int = 0
    var matchedCount: Int = 0
    var isFound = false

    func findWordIndex(_ currentWord: String) {
        if currentWord == word {
            isFound = true
            matchedCount = count
        }
        if (currentWord.count == 5 || isFound) {return} else {
            for i in 0..<vowels.count {
                count += 1
                findWordIndex(currentWord + vowels[i])
            }
        }
    }

    findWordIndex("")

    return matchedCount
}

